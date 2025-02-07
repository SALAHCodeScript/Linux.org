$Host.UI.RawUI.WindowTitle = "Programming | SALAH"

$lang = $($args[0])

$dir1 = $($args[1])  
$dir2 = $($args[2])  
$dir3 = $($args[3])

$lang_name = "Programming"

Set-Location $env:programming

if ($lang -eq "asm"){
   $lang_name = "Assembly x86"
} elseif ($lang -eq "sh"){
   $lang_name = "Bash"
} elseif ($lang -eq "bat"){
   $lang_name = "Batch"
} elseif ($lang -eq "c"){
   $lang_name = "C"
} elseif ($lang -eq "cpp"){
   $lang_name = "C++"
} elseif ($lang -eq "css"){
   $lang_name = "CSS"
} elseif ($lang -eq "git"){
   $lang_name = "Git"
} elseif ($lang -eq "html"){
   $lang_name = "HTML"
} elseif ($lang -eq "java"){
   $lang_name = "Java"
} elseif ($lang -eq "js"){
   $lang_name = "JavaScript"
} elseif ($lang -eq "json"){
   $lang_name = "JSON"
} elseif ($lang -eq "linux"){
   $lang_name = "Linux"
} elseif ($lang -eq "md"){
   $lang_name = "Markdown"
} elseif ($lang -eq "mysql"){
   $lang_name = "MySQL"
} elseif ($lang -eq "node"){
   $lang_name = "Nodejs"
} elseif ($lang -eq "perl"){
   $lang_name = "Perl"
} elseif ($lang -eq "php"){
   $lang_name = "PHP"
} elseif ($lang -eq "pwsh"){
   $lang_name = "Powershell"
} elseif ($lang -eq "py"){
   $lang_name = "Python"
} elseif ($lang -eq "sqlite"){
   $lang_name = "SQLite3"
} elseif ($lang -eq "svg"){
   $lang_name = "SVG"
} elseif ($lang -eq "toml"){
   $lang_name = "TOMAL"
} elseif ($lang -eq "vbs"){
   $lang_name = "VBScript"
} elseif ($lang -eq "xml"){
   $lang_name = "XML"
} elseif ($lang -eq "yml"){
   $lang_name = "YAML"
} elseif ($lang -eq "yara"){
   $lang_name = "YARA"
}

if (Test-Path "$env:programming\$lang_name"){
   $Host.UI.RawUI.WindowTitle = "$lang_name | SALAH"
   Set-Location "$env:programming\$lang_name"
   if ($dir1 -eq "dev"){
      $Host.UI.RawUI.WindowTitle = "$lang_name > Developer | SALAH"
      Set-Location "$env:programming\$lang_name\Developer"
      if ($dir2 -eq "pack"){
         $Host.UI.RawUI.WindowTitle = "$lang_name > Developer > Package | SALAH"
         Set-Location "$env:programming\$lang_name\Developer\Package"
      } elseif ($dir2 -eq "proj"){
         $Host.UI.RawUI.WindowTitle = "$lang_name > Developer > Project | SALAH"
         Set-Location "$env:programming\$lang_name\Developer\Project"
         if ($dir3 -eq "cmd"){
            $Host.UI.RawUI.WindowTitle = "$lang_name > Developer > Project > Command | SALAH"
            Set-Location "$env:programming\$lang_name\Developer\Project\Command"
         }
      } elseif ($dir2 -eq "qk"){
         $Host.UI.RawUI.WindowTitle = "$lang_name > Developer > Quick | SALAH"
         Set-Location "$env:programming\$lang_name\Developer\Quick"
      } elseif ($dir2 -eq "tut"){
         $Host.UI.RawUI.WindowTitle = "$lang_name > Developer > Tutorial | SALAH"
         Set-Location "$env:programming\$lang_name\Developer\Tutorial"
         if ($dir3 -eq "basic"){
            $Host.UI.RawUI.WindowTitle = "$lang_name > Developer > Tutorial > Basic | SALAH"
            Set-Location "$env:programming\$lang_name\Developer\Tutorial\Basic"
         } elseif ($dir3 -eq "learn"){
            $Host.UI.RawUI.WindowTitle = "$lang_name > Developer > Tutorial > Learn | SALAH"
            Set-Location "$env:programming\$lang_name\Developer\Tutorial\Learn"
         }
      }
   } elseif ($dir1 -eq "proj"){
      $Host.UI.RawUI.WindowTitle = "$lang_name > Project | SALAH"
      Set-Location "$env:programming\$lang_name\Project"
   } elseif ($dir1 -eq "venv"){
      $Host.UI.RawUI.WindowTitle = "$lang_name > Virtual Environment | SALAH"
      Set-Location "$env:programming\$lang_name\Virtual Environment"
      if ($dir2 -eq "mypack"){
         $Host.UI.RawUI.WindowTitle = "$lang_name > Virtual Environment > My Packages | SALAH"
         Set-Location "$env:programming\$lang_name\Virtual Environment\lib\python3.13\my-packages"
      }
   } elseif ($dir1 -eq "web"){
      $Host.UI.RawUI.WindowTitle = "$lang_name > Web | SALAH"
      Set-Location "$env:programming\$lang_name\Web"
   }
}
