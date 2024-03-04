#!/bin/bash

echo "install pip"
sudo pacman -S python-pip --noconfirm
pip install psutil --break-system-packages


echo "install packages"
sudo pacman -S vim --noconfirm
sudo pacman -S picom --noconfirm
sudo pacman -S unclutter --noconfirm
sudo pacman -S feh --noconfirm
sudo pacman -S nerd-fonts --noconfirm
sudo pacman -S zsh --noconfirm


echo "dotfiles"
git clone https://github.com/AdenilsonPR/arch-qtile.git
cp -r -f /arch-qtile/.config/* .config/
cp /arch-qtile/.xprofile .


echo "oh my zsh"
cp arch-qtile/.zshrc .
ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"
git clone https://github.com/spaceship-prompt/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt" --depth=1
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"