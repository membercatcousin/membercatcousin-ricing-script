#!/bin/bash

# -- membercatcousin's ricing script --

echo "membercatcousin's ricing script Installer!"

# -- yay installer --

# Check if yay is ALREADY installed so we don't waste time
if command -v yay &> /dev/null; then
    echo "✅ yay is already installed! Skipping..."
else
    echo "⚠️ yay not found. Installing..."
    
    sudo pacman -Syu
    sudo pacman -S --needed base-devel git
    # Clone into /tmp so we don't clutter the user's home folder
    git clone https://aur.archlinux.org/yay.git /tmp/yay
    cd /tmp/yay
    makepkg -si --noconfirm
    
    # Clean up the installation files
    cd ~
    rm -rf /tmp/yay
fi


echo "verfiying yay..."
yay --version
