import os
import json
import logging
import random


# Logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# Config

base_config_file = 'screensaver_config.json'
config_file = 'static/config.json'

hearing_media_folder_url = "/media/hearing/"
deaf_media_folder_url = "/media/deaf/"

deaf_media_files_folder = 'static' + deaf_media_folder_url
hearing_media_files_folder = 'static' + hearing_media_folder_url


#Root?
#domain = "zooooom.us"

#CDN?
domain = "d2brqd0zfu9kp3.cloudfront.net"

# Let's get functions

def get_videos(media_folder, folder_url):
    subfolders = [ f.path for f in os.scandir(media_folder) if f.is_dir() ]
    videos = []
    for i in subfolders:
        dirhash = i.replace(media_folder,"")
        url = "https://" + domain + folder_url + dirhash + "/prog_index.m3u8"
        videos.append(url)
    return videos
    
# Let's do it

logger.debug("Generating config.json")

deaf_videos = get_videos(deaf_media_files_folder, deaf_media_folder_url)
hearing_videos = get_videos(hearing_media_files_folder, hearing_media_folder_url)
videos = deaf_videos + hearing_videos
random.shuffle(videos)

with open(base_config_file) as json_file:
    config = json.load(json_file)

config['videos'] = videos
config['hearing_videos'] = hearing_videos
config['deaf_videos'] = deaf_videos

with open(config_file, 'w') as outfile:
    json.dump(config, outfile, indent=2)

