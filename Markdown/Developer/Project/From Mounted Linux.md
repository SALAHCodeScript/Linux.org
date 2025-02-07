## Get Home Folders:
```bash
sudo rm ~/.bashrc
sudo rm -r ~/Documents/ ~/Videos/ ~/Pictures/ ~/Music/
sudo ln -s /media/linux/home/salah/.bashrc ~/.
sudo ln -s /media/linux/home/salah/Documents/ ~/.
sudo ln -s /media/linux/home/salah/Videos/ ~/.
sudo ln -s /media/linux/home/salah/Pictures/ ~/.
sudo ln -s /media/linux/home/salah/Music/ ~/.
```
## Get Fonts:
```bash
sudo ln -s /media/linux/home/salah/.local/share/fonts/ ~/.local/share
```
## Get Flatpak Programs:
```bash
sudo rm -r "/home/mint/.local/share/flatpak"
sudo rm -rfd "/var/lib/flatpak"
sudo ln -s "/media/linux/home/salah/.cache/flatpak" "/home/mint/.cache"
sudo ln -s "/media/linux/home/salah/.local/share/flatpak" "/home/mint/.local/share"
sudo ln -s "/media/linux/var/lib/flatpak" "/var/lib"```
