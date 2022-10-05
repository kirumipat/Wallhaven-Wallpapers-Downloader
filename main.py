import os
import re
import sys
from time import sleep
import requests
import random
import pathlib
import string

DOWNLOAD_DIR = f"{str(pathlib.Path.home())}/WALL"


def generate_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))


def get_ext(url):
    ext = os.path.splitext(url)[1]
    return ext


def download_wallpaper(url):
    print(f"Downloading {url}")
    res = requests.get(url, allow_redirects=True)
    download_path = f"{DOWNLOAD_DIR}/{generate_id()}{get_ext(url)}"
    open(download_path, 'wb').write(res.content)
    print(f"Downloading done of {url}")


def wallpaper_search_api(query, page_id):
    query_url = f"https://wallhaven.cc/api/v1/search?q={query}/{page_id}"
    res = requests.get(query_url)
    response = res.json()
    dl_links = []
    for wallpaper in response["data"]:
        res = [int(s) for s in re.findall(r'-?\d+\.?\d*', wallpaper["resolution"])]
        if res[0] / res[1] == 16 / 9:
            dl_links.append(wallpaper["path"])

    return dl_links


os.makedirs(DOWNLOAD_DIR, exist_ok=True)
if len(sys.argv) < 2:
    print("Usage main.py <search_query>")
    quit()

query = sys.argv[1].replace(' ', '+')

for page in range(1, 20):
    print(page)
    wallpapers = wallpaper_search_api(query, page)
    for wallpaper in wallpapers:
        download_wallpaper(wallpaper)
        sleep(3)
    sleep(3)
