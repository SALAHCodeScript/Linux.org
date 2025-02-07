@echo off
title Programming ^| SALAH

set lang="%1"

set dir1="%2"
set dir2="%3"
set dir3="%4"

set lang_name=Programming

cd %programming%

if %lang% == "asm" (
   set lang_name=Assembly x86
) else if %lang% == "sh" (
   set lang_name=Bash
) else if %lang% == "bat" (
   set lang_name=Batch
) else if %lang% == "c" (
   set lang_name=C
) else if %lang% == "cpp" (
   set lang_name=C++
) else if %lang% == "css" (
   set lang_name=CSS
) else if %lang% == "git" (
   set lang_name=Git
) else if %lang% == "html" (
   set lang_name=HTML
) else if %lang% == "java" (
   set lang_name=Java
) else if %lang% == "js" (
   set lang_name=JavaScript
) else if %lang% == "json" (
   set lang_name=JSON
) else if %lang% == "linux" (
   set lang_name=Linux
) else if %lang% == "md" (
   set lang_name=Markdown
) else if %lang% == "mysql" (
   set lang_name=MySQL
) else if %lang% == "node" (
   set lang_name=Nodejs
) else if %lang% == "perl" (
   set lang_name=Perl
) else if %lang% == "php" (
   set lang_name=PHP
) else if %lang% == "pwsh" (
   set lang_name=Powershell
) else if %lang% == "py" (
   set lang_name=Python
) else if %lang% == "sqlite" (
   set lang_name=SQLite3
) else if %lang% == "svg" (
   set lang_name=SVG
) else if %lang% == "toml" (
   set lang_name=TOMAL
) else if %lang% == "vbs" (
   set lang_name=VBScript
) else if %lang% == "xml" (
   set lang_name=XML
) else if %lang% == "yml" (
   set lang_name=YAML
) else if %lang% == "yara" (
   set lang_name=YARA
)

if exist "%programming%\%lang_name%" (
   title %lang_name% ^| SALAH
   cd "%programming%\%lang_name%"
   if %dir1% == "dev" (
      title %lang_name% ^> Developer ^| SALAH
      cd "%programming%\%lang_name%\Developer"
      if %dir2% == "pack" (
         title %lang_name% ^> Developer ^> Package ^| SALAH
         cd "%programming%\%lang_name%\Developer\Package"
      ) else if %dir2% == "proj" (
         title %lang_name% ^> Developer ^> Project ^| SALAH
         cd "%programming%\%lang_name%\Developer\Project"
         if %dir3% == "cmd" (
            title %lang_name% ^> Developer ^> Project ^> Command ^| SALAH
            cd "%programming%\%lang_name%\Developer\Project\Command"
         )
      ) else if %dir2% == "qk" (
         title %lang_name% ^> Developer ^> Quick ^| SALAH
         cd "%programming%\%lang_name%\Developer\Quick"
      ) else if %dir2% == "tut" (
         title %lang_name% ^> Developer ^> Tutorial ^| SALAH
         cd "%programming%\%lang_name%\Developer\Tutorial"
         if %dir3% == "basic" (
            title %lang_name% ^> Developer ^> Tutorial ^> Basic ^| SALAH
            cd "%programming%\%lang_name%\Developer\Tutorial\Basic"
         ) else if %dir3% == "learn" (
            title %lang_name% ^> Developer ^> Tutorial ^> Learn ^| SALAH
            cd "%programming%\%lang_name%\Developer\Tutorial\Learn"
         )
      )
   ) else if %dir1% == "proj" (
      title %lang_name% ^> Project ^| SALAH
      cd "%programming%\%lang_name%\Project"
   ) else if %dir1% == "venv" (
      title %lang_name% ^> Virtual Environment ^| SALAH
      cd "%programming%\%lang_name%\Virtual Environment"
      if %dir2% == "mypack" (
         title %lang_name% ^> Virtual Environment > My packages ^| SALAH
         cd "%programming%\%lang_name%\Virtual Environment\lib\python3.13\my-packages"
      )
   ) else if %dir1% == "web" (
      title %lang_name% ^> Web ^| SALAH
      cd "%programming%\%lang_name%\Web"
   )
)
