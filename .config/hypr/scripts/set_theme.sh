#!/usr/bin/env bash

set_theme () {
    gsettings set org.gnome.desktop.interface color-scheme 'prefer-light'
    gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'
}

set_theme

