# Juell's dotfiles 

The dotfiles (program configuration files) used in my Hyprland rice. These files are stored in a Git bare repository.

![image](https://github.com/juellsprott/dotfiles/blob/master/.config/examples/example1.png)
![image](https://github.com/juellsprott/dotfiles/blob/master/.config/examples/example3.png)
![image](https://github.com/juellsprott/dotfiles/blob/master/.config/examples/example2.png)

## Contents
This repository contains configuration files for the following packages
- ZSH
- oh-my-zsh
- Visual Studio Code
- Hyprland
- Hyprpaper
- Waybar
- Dunst
- Albert Launcher
- swaylock-effects
- swayidle
- Kitty
- Thunar
- Any program using GTK configurations (chromium-based browsers, file managers)

## Dependencies
In addition to the above packages, this repository also depends on the following packages for complete functionality and theming:
- oh-my-zsh plugins
  - autojump
  -  bgnotify
  -  zsh-autosuggestions
  -  zsh-autocomplete
  -  zsh-syntax-highlighting
  -  zsh-history-enquirer
-  [btop](https://archlinux.org/packages/extra/x86_64/btop/) for Waybar system monitoring
-  [Catpuccin Mocha GTK theme](https://github.com/catppuccin/gtk) for GTK theming
- [cava](https://aur.archlinux.org/packages/cava) for the visualizer in Waybar
- [polkit](https://wiki.archlinux.org/title/Polkit) for authentication agent (needed for VSCode, Edge and 1Password)
- [brightnessctl](https://github.com/Hummer12007/brightnessctl) For controlling brightness
- [wireplumber](https://archlinux.org/packages/?name=wireplumber) and [pipewire](https://archlinux.org/packages/?name=pipewire) for sound control
- 

Additionally, PyWal is also installed and initialized at startup, however is not utilized in this rice. For information on how to use PyWal, refer to [this](https://github.com/rchrdwllm/dotfiles/tree/master) and this [this](https://github.com/dylanaraps/pywal). (And [this](https://github.com/ErkHal/walbert) for Albert launcher) 

## Fonts, cursors and icons

All used fonts can be found in the fonts folder, aside from 'Iosevka', which must be installed manually (recommended to use AUR for this)

- Roboto for GTK and VSCode UI
- Monaspace Krypton for Waybar
- Iosevka Curly for Kitty/VSCode terminals
- bargraph for cava visualiser
- Monaspace Argon for VSCode editor

For the cursor [Bibata Modern Classic](https://github.com/ful1e5/Bibata_Cursor) is used. 

For icons, I use the Numix and [Numix Circle](https://github.com/numixproject/numix-icon-theme-circle) packs.

## Further configuration

## TODO
- [ ] Add proper clipboard with theming
- [ ] Further customize neofetch
- [ ] Switch to Neovim
  - [ ] Learn how to exit Neovim
- [ ] Add links to all packages
- [ ] Add shell script for installing packages and applying this repo's config files
  - [ ] Learn bash in order to create such a script
- [ ] Analyse power usage of waybar/hyprland modules/configurations to optimize laptop usage
- [ ] Add credits for all provided shell scripts and waybar configuration
