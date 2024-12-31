# Linux-Mint
### 1. Customize Linux:
##### Change your settings and theme as you like.
### 2. Update:
##### Check for a new updates in.
```bash
sudo apt update
sudo apt upgrade
```
### 3. Install Drivers:
##### Verify if there is drivers to download in driver manager.
### 4. Install Packages:
##### Tools:
```bash
sudo apt install -y curl git zsh neovim tmux bat tree xclip fzf yarn yt-dlp adb scrcpy android-tools-adb android-tools-fastboot ffmpeg
```
##### Networks:
```bash
sudo apt install -y nmap traceroute openssh-server scp samba
```
##### Programming Languages:
```bash
sudo apt install -y build-essential nasm mysql-server mysql-client sqlite3 nodejs npm default-jdk php apache2 libapache2-mod-php ruby-full docker.io perl yara jq
sudo apt install -y python3-pip python3-venv python3-pil python3-tk python3-requests
```
##### Programs:
```bash
sudo apt install -y gimp audacity
flatpak install -y flathub org.kde.krita
flatpak install -y flathub md.obsidian.Obsidian
```
##### Office:
```bash
sudo apt install -y libreoffice-math libreoffice-base
```
##### Windows:
```bash
sudo apt install -y wine wine winetricks
winetricks vcrun2003 vcrun2005 vcrun2008 vcrun2010 vcrun2012 vcrun2013 vcrun2022 d3dx9 directx9 dotnet20 dotnet35 dotnet40 dotnet48
```
### 5. Switch to ZSH Shell:
```bash
sudo chsh -s $(which zsh)
```
### 6. Restart Linux:
##### Reboot your system to display the changes.
```bash
sudo apt reboot now
```
### 7. Improve ZSH Shell:
##### Oh My Zsh Installation:
```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
##### Install Powerlevel10k:
```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k
```
##### Install Plugins:
```bash
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-history-substring-search $ZSH_CUSTOM/plugins/zsh-history-substring-search
```
##### Edit .zshrc File:
```bash
# Enable Powerlevel10k Theme
ZSH_THEME="powerlevel10k/powerlevel10k"

# Plugins
plugins=(
  git                       # Helpful Git commands and shortcuts
  zsh-syntax-highlighting   # Syntax highlighting for better readability
  zsh-autosuggestions       # Suggestions based on previous commands
  history                   # Better history management
)
```
### 8. Get PowerShell:
##### Install Powershell:
```bash
sudo apt install -y wget apt-transport-https software-properties-common
wget -q "https://packages.microsoft.com/config/ubuntu/24.04/packages-microsoft-prod.deb"
sudo dpkg -i packages-microsoft-prod.deb
sudo apt update
sudo apt install -y powershell
```
##### Install Oh My Posh:
```bash
wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/posh-linux-amd64 -O oh-my-posh
chmod +x oh-my-posh
sudo mv oh-my-posh /usr/local/bin/
```
##### Install Themes:
```bash
mkdir ~/.poshthemes
wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/themes.zip
unzip themes.zip -d ~/.poshthemes
chmod u+rw ~/.poshthemes/*.json
```
##### Edit $PROFILE File:
```powershell
oh-my-posh init pwsh | Invoke-Expression
oh-my-posh init pwsh --config ~/.poshthemes/paradox.omp.json | Invoke-Expression
```
### 9. Get Python:
##### Install python3.13
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.13
```
##### Install pip:
```bash
python3.13 -m ensurepip --upgrade
# if didn't work try this:
curl -O https://bootstrap.pypa.io/get-pip.py
python3.13 get-pip
```
##### Install python's packages:
```bash
pip install Essentials Faker panda3d APScheduler Streamlit Celery Gunicorn SymPy Plotly Dash PyBrain NLTK unittest pytest pillow opencv-python mysql-connector-python python-dateutil python-docx docopt argparse-subcommand cement python-fire prompt-toolkit rich yara-python customtkinter typer requests pyPDF2 sqlalchemy json_schema lxml beautifulsoup4 numpy pandas matplotlib scikit-learn scipy flask fastapi pygame twisted argparse django pyautogui selenium openpyxl click argparse-subcommand PythonTurtle
```
### 10. Install Programs:
##### Browser:
###### 'Google Chrome' | 'Midori'
##### Text Editor:
###### 'VSCode'
##### Games:
###### 'Godot 3.6' | 'TLauncher'
##### Others:
###### 'Free Download Manager' | 'Ventoy'
### 11. Get your Data:
##### Now your machine is ready to get data.

