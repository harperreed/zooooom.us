import os
import json

base_config_file = 'screensaver_config.json'
config_file = 'static/config.json'
media_folder = 'static/media/'
domain = "suspicious-kirch-4c179d.netlify.com"

subfolders = [ f.path for f in os.scandir(media_folder) if f.is_dir() ]

with open(base_config_file) as json_file:
    config = json.load(json_file)
    print(config)

videos = []
for i in subfolders:
    dirhash = i.replace(media_folder,"")
    url = "https://" + domain + "/media/" + dirhash + "/prog_index.m3u8"
    videos.append(url)

config['videos'] = videos

with open(config_file, 'w') as outfile:
    json.dump(config, outfile)

