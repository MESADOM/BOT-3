@echo off
setlocal
cd /d %~dp0

if exist .env (
  for /f "usebackq tokens=1,* delims==" %%A in (".env") do (
    if not "%%A"=="" set "%%A=%%B"
  )
)

python -u run_paper_bot.py
endlocal
