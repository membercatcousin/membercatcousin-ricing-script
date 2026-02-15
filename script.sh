#!/bin/bash

# -- membercatcousin's ricing script --

echo "membercatcousin's ricing script Installer!"
echo "Thank you for using our product >w<"
# --Python installer-- :D
#noice tysm for adding python
sudo pacman -Syu
sudo pacman -S python

# -- yay installer --

# Check if yay is ALREADY installed so we don't waste time and not get enuf food in the asian buffet
if command -v yay &> /dev/null; then
    echo "✅ yay is already installed! Skipping..
    "
else
    echo "⚠️ yay not found."
    read -p "Install yay?(y/n):" -n 1 -r
    if [[ $REPLY =~ [Yy]$ ]] then    
        sudo pacman -Syu
        sudo pacman -S --needed base-devel git
        # Clone into /tmp so we don't clutter the user's home folder and they call 911
        git clone https://aur.archlinux.org/yay.git /tmp/yay
        cd /tmp/yay
        makepkg -si --noconfirm
        # Clean up the installation files bcoz we gotta leave no evidence :skull:
        cd ~
        rm -rf /tmp/yay
        fi
fi


echo "verfiying yay..."
yay --version

# -- ALL IN ONE SCRIPT --#
python script.py
