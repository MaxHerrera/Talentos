import urllib.request
import random


def downloader(image_url):
    file_name = random.randrange(1,10000)
    full_file_name = str(file_name) + '.jpg'
    urllib.request.urlretrieve(image_url,full_file_name)


downloader("https://apod.nasa.gov/apod/image/1501/hs-2015-01m16pillarsHST.jpg")