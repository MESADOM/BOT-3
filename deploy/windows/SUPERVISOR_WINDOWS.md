# Supervisor en Windows (Task Scheduler / NSSM)

## Opción A: Programador de tareas
1. Abrir **Task Scheduler**.
2. Crear tarea: `BOT-3-Paper`.
3. Trigger: **At startup**.
4. Action: iniciar `start_bot.bat` desde la carpeta del proyecto.
5. Marcar **Run whether user is logged in or not**.
6. Marcar **Restart every 1 minute** si falla.

## Opción B: NSSM
1. Instalar NSSM.
2. Ejecutar (CMD como admin):
   - `nssm install BOT3Paper C:\ruta\BOT-3\start_bot.bat`
   - `nssm set BOT3Paper Start SERVICE_AUTO_START`
   - `nssm start BOT3Paper`
3. Validar logs estándar y reinicio automático.
