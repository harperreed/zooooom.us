#!/bin/bash

source_dir="/Users/harper/Dropbox/src/zooooom/source_videos/"
render_dir="static/media"

for i in ${source_dir}/*;
  do name=`basename "$i" `
  name=`echo "$name" | cut -d'.' -f1`
  name=`echo "$name" | md5`

  ffmpeg -i "$i" -vcodec libx264 -crf 30  -an "${render_dir}/${name}.mp4"
  mkdir "${render_dir}/${name}"
  mediafilesegmenter "${render_dir}/${name}.mp4" -f "${render_dir}/${name}" -t 5

done
