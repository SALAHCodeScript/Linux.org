@echo off

set name=%1

:func
setlocal
    if "%name%" == "SALAH" (
        echo "you have access"
    ) else if "%name%" == "Programmer" (
        echo "maybe you have access"
    ) else (
        echo "you don't have access"
    )
@REM endlocal
@REM goto :eof
:end
