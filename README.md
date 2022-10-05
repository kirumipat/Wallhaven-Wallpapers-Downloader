# Wallhaven-Wallpapers-Downloader
## This script automatically downloads desktop wallpapers from the Wallhaven service

## Tags for running the script

```bash
pathon3 main.py "Tags"
```

<mark>TAGS</mark>

[Tags - wallhaven.cc](https://wallhaven.cc/tags/popular)

By default, images are downloaded only with an aspect ratio of 16/9

If you want to change to something else, correct this line

```python
if res[0] / res[1] == 16 / 9:
```
