#!/bin/bash

source_dir="/Users/harper/Dropbox/src/zooooom/deaf/source_videos/"
render_dir="static/media/deaf/"

for i in ${source_dir}/*;
  do name=`basename "$i" `
  name=`echo "$name" | cut -d'.' -f1`
  name=`echo "$name" | md5`
  destination_file="${render_dir}/${name}.mp4"
  destination_folder="${render_dir}/${name}"

  if [ ! -f "$destination_file" ]; then
    ffmpeg -i "$i" -vcodec libx264 -crf 30  -an "${destination_file}"
    if [ ! -d "$destination_folder" ]; then
      mkdir "${destination_folder}"
      mediafilesegmenter "${destination_file}" -f "${destination_folder}" -t 5
    fi
  fi

done
