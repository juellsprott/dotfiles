get_icon_theme_name () {
    grep "gtk-icon-theme-name" ~/.config/gtk-3.0/settings.ini | cut -d "=" -f 2
}

get_brightness () {
    current=$(brightnessctl -d intel_backlight g)
    max=$(brightnessctl -d intel_backlight m)
    value=$(awk -v current="$current" -v max="$max" 'BEGIN { printf "%.0f", (current / max) * 100 }')
    echo "$value"
}

get_brightness_icon () {
    ICON_THEME=$(get_icon_theme_name)
    if ((0==$1))
    then
        echo "/usr/share/icons/Numix/48/notifications/notification-display-brightness-off.svg"
    elif ((1<=$1 && $1<=33))
    then
        echo "/usr/share/icons/Numix/48/notifications/notification-display-brightness-low.svg"
    elif ((34<=$1 && $1<=66))
    then
        echo "/usr/share/icons/Numix/48/notifications/notification-display-brightness-medium.svg"
    else
        echo "/usr/share/icons/Numix/48/notifications/notification-display-brightness-high.svg"
    fi
}

raise_brightness () {
    brightnessctl -d intel_backlight set +$1
    # show_notification
}

lower_brightness () {
    brightnessctl -d intel_backlight set $1-
   # show_notification
}

show_notification () {
    BRIGHTNESS=$(get_brightness)
    ICON=$(get_brightness_icon $BRIGHTNESS)
    bar=$(seq -s "─" 0 $((BRIGHTNESS / 6)) | sed 's/[0-9]//g')
    dunstify --appname="Brightness" -i $ICON -t 1000 -r 5555 -u normal "${bar} $BRIGHTNESS %"
}

case $1 in
    raise) raise_brightness $2 ;;
    lower) lower_brightness $2 ;;
esac