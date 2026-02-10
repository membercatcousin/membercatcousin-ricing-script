# -- membercatcousin's ricing script --

echo "membercatcousin's ricing script Installer!"

# -- yay installer --

sudo pacman -Syu
sudo pacman -S --needed base-devel git
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
echo "verfiying yay..."
yay --version
