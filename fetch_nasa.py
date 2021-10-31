import requests
from urllib import parse
import os
from datetime import datetime
import download


def fetch_nasa_images(token):
    url = 'https://api.nasa.gov/planetary/apod'
    path = 'images/nasa'
    payload = {'api_key': token, 'count': 30}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    pictures = response.json()

    for picture_number, picture in enumerate(pictures):
        picture_url = picture['url']
        picture_extension = get_extension(picture_url)

        download.download_image(picture_url, path, picture_number, picture_extension, payload)


def fetch_epic_images(token):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    path = 'images/epic'
    payload = {'api_key': token}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    images = response.json()

    for number, image in enumerate(images):
        name = image['image']
        date_str = image['date']
        date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        date_format = date.strftime('%Y/%m/%d')
        url = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png'.format(
            date_format,
            name,
        )

        download.download_image(url, path, number, '.png', payload)


def get_extension(url):
    path = parse.urlsplit(url)[2]
    extension = os.path.splitext(path)[1]
    return extension



