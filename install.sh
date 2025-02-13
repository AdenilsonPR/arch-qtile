#!/bin/bash

echo "install pip"
sudo pacman -S python-pip --noconfirm
pip install psutil --break-system-packages


echo "yay"
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si


echo "install packages"
sudo pacman -Syyu
sudo pacman -S vim --noconfirm
sudo pacman -S picom --noconfirm
sudo pacman -S unclutter --noconfirm
sudo pacman -S feh --noconfirm
sudo pacman -S ttf-firacode-nerd --noconfirm
sudo pacman -S otf-firamono-nerd --noconfirm
sudo pacman -S zsh --noconfirm
sudo pacman -S alsa-utils --noconfirm
sudo pacman -S qtile-extras
sudo pacman -S thunar
sudo pacman -S lightdm-gtk-greeter-settings
sudo pacman -S lxappearance
sudo pacman -S git
sudo pacman -S go
sudo pacman -S steam
yay gruvbox-material
yay gruvbox-material-icon-theme-git
yay -S visual-studio-code-bin


echo "dotfiles"
git clone https://github.com/AdenilsonPR/arch-qtile.git
cp -r -f /arch-qtile/.config/* .config/
cp /arch-qtile/.xprofile .


echo "oh my zsh"
cp arch-qtile/.zshrc .
ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"
git clone https://github.com/spaceship-prompt/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt" --depth=1
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"