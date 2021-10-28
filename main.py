import os.path
import telegram
import requests
from pathlib import Path
from urllib import parse
import os
from dotenv import load_dotenv
from datetime import datetime


def fetch_spacex_last_launch(url):
    path = 'images/spacex'
    response = requests.get(url)
    response.raise_for_status()

    images_url = (response.json())['links']['flickr_images']

    for image_number, image_url in enumerate(images_url):
        response = requests.get(image_url)
        response.raise_for_status()

        with open('{}{}{}'.format(path, image_number, '.jpg'), 'wb') as file:
            file.write(response.content)


def fetch_nasa_image(url):
    path = 'images/NASA/'
    payload = {'api_key': token, 'count': 30}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    pictures = response.json()

    for picture_number, picture in enumerate(pictures):
        picture_url = picture['url']
        picture_extension = get_extension(picture_url)
        with open('{}{}{}'.format(path, picture_number, picture_extension), 'wb') as file:
            response = requests.get(picture_url)
            response.raise_for_status()
            file.write(response.content)


def fetch_epic_image(url):
    path = 'images/EPIC/'
    payload = {'api_key': token}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    images = response.json()

    for number, image in enumerate(images):
        name = image['image']
        date_str = image['date']
        date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        date_format = date.strftime('%Y/%m/%d')
        url = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png'.format(date_format, name)

        with open('{}{}.png'.format(path, number), 'wb') as file:
            response = requests.get(url, params=payload)
            response.raise_for_status()
            file.write(response.content)


def get_extension(url):
    path = (parse.urlsplit(url))[2]
    extension = os.path.splitext(path)[1]
    return extension


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('TOKEN_NASA')
    load_dotenv()
    Path('images').mkdir(parents=True, exist_ok=True)
    Path('images/NASA').mkdir(parents=True, exist_ok=True)
    Path('images/EPIC').mkdir(parents=True, exist_ok=True)

    bot = telegram.Bot(token='2005968531:AAGcx7Y7InAxTGgoJTV84RfBT3Yu0uZpkPk')
    bot.send_message(chat_id='@test_devman', text="I'm sorry Dave I'm afraid I can't do that.")