#!/bin/bash

echo "yay"
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si


echo "install pip"
yay -S python-pip --noconfirm
pip install psutil --break-system-packages


echo "install packages"
yay -Syyu
yay -S vim --noconfirm
yay -S picom --noconfirm
yay -S unclutter --noconfirm
yay -S feh --noconfirm
yay -S ttf-firacode-nerd --noconfirm
yay -S otf-firamono-nerd --noconfirm
yay -S zsh --noconfirm
yay -S alsa-utils --noconfirm
yay -S thunar --noconfirm
yay -S lightdm-gtk-greeter-settings --noconfirm
yay -S lxappearance --noconfirm
yay -S git --noconfirm
yay -S go --noconfirm
yay -S steam --noconfirm
yay -S rofi --noconfirm
yay -S qtile-extras --noconfirm
yay -S gruvbox-material --noconfirm
yay -S gruvbox-material-icon-theme-git --noconfirm
yay -S visual-studio-code-bin --noconfirm
yay -S zen-browser-bin --noconfirm

echo "dotfiles"
git clone https://github.com/AdenilsonPR/arch-qtile.git
cp -r -f /arch-qtile/.config/* .config/
cp /arch-qtile/.xprofile .


echo "oh my zsh"
cp arch-qtile/.zshrc .
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/spaceship-prompt/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt" --depth=1
ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"
