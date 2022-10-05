# Wallhaven-Wallpapers-Downloader
## This script automatically downloads desktop wallpapers from the Wallhaven service

## Tags for running the script

[Tags - wallhaven.cc](https://wallhaven.cc/tags/popular)
```bash
pathon3 main.py "Tags"
```


## By default, images are downloaded only with an aspect ratio of 16/9
## If you want to change to something else, correct this line

```python
if res[0] / res[1] == 16 / 9:
```
## By default, it downloads from 20 pages, 
## if you want to increase or decrease this value, change the second digit here.
```python
for page in range(1, 20):
```
