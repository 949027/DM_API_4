import requests
from urllib import parse
import os
from datetime import datetime


def fetch_nasa_image(url, token):
    path = 'images/nasa'
    payload = {'api_key': token, 'count': 30}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    pictures = response.json()

    for picture_number, picture in enumerate(pictures):
        picture_url = picture['url']
        picture_extension = get_extension(picture_url)
        response = requests.get(picture_url)
        response.raise_for_status()
        with open(
                '{}{}{}'.format(path, picture_number, picture_extension),
                'wb',
        ) as file:
            file.write(response.content)


def fetch_epic_image(url, token):
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
        response = requests.get(url, params=payload)
        response.raise_for_status()
        with open('{}{}.png'.format(path, number), 'wb') as file:
            file.write(response.content)


def get_extension(url):
    path = (parse.urlsplit(url))[2]
    extension = os.path.splitext(path)[1]
    return extension



