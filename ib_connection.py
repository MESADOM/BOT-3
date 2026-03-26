from __future__ import annotations

import logging
import os
import time
from dataclasses import dataclass, field
from threading import Lock
from typing import Optional, Set

from ib_insync import IB


LOGGER = logging.getLogger("ib_connection")


@dataclass
class IBConfig:
    host: str = os.getenv("IB_HOST", "127.0.0.1")
    port: int = int(os.getenv("IB_PORT", "4002"))
    client_id: int = int(os.getenv("IB_CLIENT_ID", "1"))
    connect_timeout_sec: float = float(os.getenv("IB_CONNECT_TIMEOUT", "10"))
    max_retries: int = int(os.getenv("IB_CONNECT_RETRIES", "5"))
    retry_delay_sec: float = float(os.getenv("IB_CONNECT_RETRY_DELAY", "3"))


@dataclass
class IBConnectionManager:
    config: IBConfig = field(default_factory=IBConfig)
    ib: IB = field(default_factory=IB)
    _submitted_order_keys: Set[str] = field(default_factory=set)
    _submitted_lock: Lock = field(default_factory=Lock)

    def connect_ib(self) -> bool:
        """Connect to IB Gateway/TWS with retries, timeout and logs."""
        if self.ib.isConnected():
            LOGGER.info("IB already connected: %s:%s clientId=%s", self.config.host, self.config.port, self.config.client_id)
            return True

        for attempt in range(1, self.config.max_retries + 1):
            try:
                LOGGER.info(
                    "Connecting to IB Gateway (%s:%s, clientId=%s) attempt %s/%s",
                    self.config.host,
                    self.config.port,
                    self.config.client_id,
                    attempt,
                    self.config.max_retries,
                )
                self.ib.connect(
                    host=self.config.host,
                    port=self.config.port,
                    clientId=self.config.client_id,
                    timeout=self.config.connect_timeout_sec,
                    readonly=False,
                )
                if self.ib.isConnected():
                    LOGGER.info("Connected to IB successfully.")
                    return True
            except Exception as exc:
                LOGGER.error("IB connection attempt %s failed: %s", attempt, exc)

            if attempt < self.config.max_retries:
                LOGGER.warning("Retrying IB connection in %ss...", self.config.retry_delay_sec)
                time.sleep(self.config.retry_delay_sec)

        LOGGER.critical("Unable to connect to IB after %s attempts.", self.config.max_retries)
        return False

    def ensure_connection(self) -> bool:
        """Ensure active connection, wait for nextValidId, reconnect automatically if needed."""
        if not self.ib.isConnected():
            LOGGER.warning("IB disconnected. Starting automatic reconnect.")
            if not self.connect_ib():
                return False

        try:
            timeout = self.config.connect_timeout_sec
            self.ib.reqIds(-1)
            start = time.time()
            while not self.ib.client.isReady():
                if time.time() - start > timeout:
                    raise TimeoutError("Timeout waiting for nextValidId from IB.")
                self.ib.sleep(0.1)

            LOGGER.debug("IB connection healthy and nextValidId received.")
            return True
        except Exception as exc:
            LOGGER.error("Connection health-check failed: %s", exc)
            self.safe_disconnect()
            return self.connect_ib()

    def should_submit_order(self, order_key: str) -> bool:
        """Prevent duplicate order submission across reconnects with idempotent order keys."""
        with self._submitted_lock:
            if order_key in self._submitted_order_keys:
                LOGGER.warning("Duplicate order prevented for key=%s", order_key)
                return False
            self._submitted_order_keys.add(order_key)
            return True

    def reset_order_key(self, order_key: str) -> None:
        with self._submitted_lock:
            self._submitted_order_keys.discard(order_key)

    def safe_disconnect(self) -> None:
        if self.ib.isConnected():
            LOGGER.warning("Disconnecting IB session.")
            self.ib.disconnect()
            LOGGER.info("IB disconnected.")
