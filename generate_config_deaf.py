import os
import json
import logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

base_config_file = 'screensaver_config.json'
config_file = 'static/config.json'
media_folder_url = "/media/deaf/"

media_folder = 'static' + media_folder_url

domain = "zooooom.us"
domain = "d2brqd0zfu9kp3.cloudfront.net"


logger.debug("Generating config.json")
subfolders = [ f.path for f in os.scandir(media_folder) if f.is_dir() ]

with open(base_config_file) as json_file:
    config = json.load(json_file)

videos = []
for i in subfolders:
    dirhash = i.replace(media_folder,"")
    url = "https://" + domain + media_folder_url + dirhash + "/prog_index.m3u8"
    videos.append(url)

config['videos'] = videos

with open(config_file, 'w') as outfile:
    json.dump(config, outfile)

