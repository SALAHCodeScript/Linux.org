function prompt {
    "SALAH@Code [$PWD]`n>> "
}

function Update-Profile {
    . $PROFILE
}

Set-Alias -Name reload -Value Update-Profile
