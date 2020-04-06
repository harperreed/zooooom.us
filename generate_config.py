import os
import json
config_file = 'static/config.json'
media_folder = 'static/media/'
domain = "suspicious-kirch-4c179d.netlify.com"

subfolders = [ f.path for f in os.scandir(media_folder) if f.is_dir() ]
config = {}

videos = []
for i in subfolders:
    dirhash = i.replace(media_folder,"")
    url = "https://" + domain + "/media/" + dirhash + "/prog_index.m3u8"
    videos.append(url)
config['videos'] = videos

with open(config_file, 'w') as outfile:
    json.dump(config, outfile)

