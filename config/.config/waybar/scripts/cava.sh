#! /bin/bash

dict="s/;//g;s/0/0/g;s/1/1/g;s/2/2/g;s/3/3/g;s/4/4/g;s/5/5/g;s/6/6/g;s/7/7/g;s/8/8/g;s/9/9/g;"

# make sure to clean pipe
pipe="/tmp/cava.pipewire"
if [ -p $pipe ]; then
    unlink $pipe
fi
mkfifo $pipe

# write cava config
config_file="/tmp/waybar_cava_config"
echo "
[general]
bars = 12
[input]
method = pipewire
source = auto
[output]
method = raw
raw_target = $pipe
data_format = ascii
ascii_max_range = 9
bar_delimiter = 59
" > $config_file

# run cava in the background
cava -p $config_file &

# reading data from fifo
while read -r cmd; do
    echo $cmd | sed $dict
done < $pipe