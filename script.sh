#!/bin/bash

# -- membercatcousin's ricing script --

echo "membercatcousin's ricing script Installer!"

# -- yay installer --

# Check if yay is ALREADY installed so we don't waste time and not get enuf food in the asian buffet
if command -v yay &> /dev/null; then
    echo "✅ yay is already installed! Skipping..."
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

# --browser installer (crying emoji)--#
read -p "Install a Browser? (y/n) " -n 1 -r
if [[ $REPLY =~ [Yy]$ ]]; then
  echo "Select a Browser"
  echo "1.Mozilla Firefox"
  echo "2.Chromium"
  echo "3.Google Chrome"
  echo "4.Brave"
  echo "5.Opera"
  echo "6.Microsoft Edge"

read -p "Enter your choice (1-6): " choice

case $choice in
  1) sudo pacman -S firefox --noconfirm ;;
  2) sudo pacman -S chromium --noconfirm ;;
  3) sudo pacman -S google-chrome --noconfirm ;;
  4) sudo pacman -S brave-browser --noconfirm ;;
  5) sudo pacman -S opera --noconfirm ;;
  6) sudo pacman -S microsoft-edge --noconfirm;;
  *) echo "Invalid choice:" ;;
esac

#DE installation (someone do it i cant)
