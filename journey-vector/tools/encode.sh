#!/bin/sh
# usage: tools/encode.sh <framesDir> <out.mp4> [fps]   (needs an ffmpeg with libx264; brew install ffmpeg)
FPS=${3:-30}
[ -f "$1/COMPLETE" ] || { echo "frames incomplete: no COMPLETE marker in $1"; exit 1; }
ffmpeg -y -hide_banner -loglevel error -framerate "$FPS" -i "$1/f%05d.png" -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -movflags +faststart "$2"
