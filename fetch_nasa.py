from datetime import datetime
import os
from urllib import parse

import requests

import download


def fetch_nasa_images(token, folder):
    url = 'https://api.nasa.gov/planetary/apod'
    path = f'{folder}/nasa'
    payload = {'api_key': token, 'count': 30}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    pictures = response.json()

    for picture_number, picture in enumerate(pictures):
        picture_url = picture['url']
        picture_extension = get_extension(picture_url)

        download.download_image(
            picture_url,
            path,
            picture_number,
            picture_extension,
            payload,
        )


def fetch_epic_images(token, folder):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    path = f'{folder}/epic'
    payload = {'api_key': token}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    images = response.json()

    for number, image in enumerate(images):
        name = image['image']
        date = datetime.strptime(image['date'], '%Y-%m-%d %H:%M:%S')
        formatted_date = date.strftime('%Y/%m/%d')
        url = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png'.format(
            formatted_date,
            name,
        )

        download.download_image(url, path, number, '.png', payload)


def get_extension(url):
    path = parse.urlsplit(url)[2]
    extension = os.path.splitext(path)[1]
    return extension
