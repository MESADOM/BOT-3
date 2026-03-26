from __future__ import annotations

import logging
import os
import signal
import sys
import time
from datetime import datetime, timezone

from dotenv import load_dotenv

from ib_connection import IBConnectionManager
from META_BOT import VERSION_SISTEMA, ejecutar_bot


RUN_INTERVAL_SECONDS = int(os.getenv("BOT_RUN_INTERVAL_SECONDS", "60"))
LOG_LEVEL = os.getenv("BOT_LOG_LEVEL", "INFO").upper()

_shutdown_requested = False


def _setup_logging() -> None:
    logging.basicConfig(
        level=LOG_LEVEL,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


def _handle_shutdown(signum: int, _frame) -> None:
    global _shutdown_requested
    logging.getLogger("runner").warning("Signal %s received. Graceful shutdown requested.", signum)
    _shutdown_requested = True


def main() -> int:
    load_dotenv()
    _setup_logging()
    logger = logging.getLogger("runner")

    logger.info("Starting VERSION %s in IBKR Paper mode.", VERSION_SISTEMA)
    logger.info("Tip: set IB_PORT=4001 in .env for IBKR real account.")

    manager = IBConnectionManager()
    if not manager.connect_ib():
        logger.critical("Unable to start bot: IB connection could not be established.")
        return 1

    signal.signal(signal.SIGINT, _handle_shutdown)
    signal.signal(signal.SIGTERM, _handle_shutdown)

    while not _shutdown_requested:
        if not manager.ensure_connection():
            logger.error("Connection verification failed. Waiting for next cycle.")
            time.sleep(RUN_INTERVAL_SECONDS)
            continue

        try:
            now = datetime.now(timezone.utc).isoformat()
            logger.info("Tick start at %s", now)
            # NOTE: Trading entry/exit strategy remains unchanged.
            ejecutar_bot()
            logger.info("Tick completed.")
        except Exception as exc:
            logger.exception("Error during bot execution tick: %s", exc)

        time.sleep(RUN_INTERVAL_SECONDS)

    manager.safe_disconnect()
    logger.info("Bot stopped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
