# VERSION 2.2.7 PAPER

Bot preparado para operar con **IB Gateway** en cuenta **Paper Trading** sin cambiar la lógica de entrada/salida de la estrategia.

## 1) Requisitos
- Python 3.10+
- IB Gateway instalado
- Cuenta IBKR Paper activa

Instalación:
```bash
pip install -r requirements.txt
cp .env.example .env
```

## 2) Configuración de entorno
Variables en `.env`:
```env
IB_HOST=127.0.0.1
IB_PORT=4002
IB_CLIENT_ID=1
IB_CONNECT_TIMEOUT=10
IB_CONNECT_RETRIES=5
IB_CONNECT_RETRY_DELAY=3
BOT_RUN_INTERVAL_SECONDS=60
BOT_LOG_LEVEL=INFO
```

- **Paper IB Gateway**: `IB_PORT=4002`
- **Real IB Gateway**: `IB_PORT=4001`

Para pasar a real más adelante, cambia solo:
```env
IB_PORT=4001
```

## 3) Arrancar IB Gateway
1. Abrir IB Gateway.
2. Iniciar sesión en la cuenta Paper.
3. Verificar en configuración API:
   - **Enable ActiveX and Socket Clients**: habilitado.
   - Puerto socket = `4002` para paper.
   - Permitir conexión localhost `127.0.0.1`.
4. Mantener IB Gateway abierto y autenticado durante toda la ejecución del bot.

## 4) Comprobar API activa
Con IB Gateway abierto, ejecutar:
```bash
python run_paper_bot.py
```
Si la API está activa verás logs de conexión y `nextValidId`.

## 5) Arrancar bot manualmente
- Linux:
```bash
./start_bot.sh
```
- Windows:
```bat
start_bot.bat
```

## 6) Arranque automático al iniciar sistema
### Linux (systemd)
Archivo de servicio: `deploy/linux/bot-paper.service`.

Pasos:
```bash
sudo cp deploy/linux/bot-paper.service /etc/systemd/system/bot-paper.service
sudo systemctl daemon-reload
sudo systemctl enable bot-paper.service
sudo systemctl start bot-paper.service
sudo systemctl status bot-paper.service
```

### Windows
Ver guía: `deploy/windows/SUPERVISOR_WINDOWS.md`.

## 7) Recuperación tras reinicio del servidor
1. Asegurar que IB Gateway también se inicia y queda autenticado.
2. Validar que el servicio/tarea del bot está en autoarranque.
3. Revisar logs del servicio para confirmar reconexión automática.

## 8) Conexión robusta implementada
- `connect_ib()` con reintentos, timeout y logs.
- `ensure_connection()` verifica conexión activa, fuerza recepción de `nextValidId`, y reconecta si cae.
- Protección básica anti-duplicado de órdenes con claves idempotentes (`should_submit_order`).
- Logs claros para conexión, desconexión, error y reconexión.

## 9) Ejecución 24/5 VPS
- Ejecutar mediante `systemd`/Task Scheduler/NSSM con reinicio automático.
- Mantener reloj del sistema sincronizado (NTP).
- Monitorizar consumo de recursos y logs.

