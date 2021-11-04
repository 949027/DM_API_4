import time
import os
from pathlib import Path

import requests
from dotenv import load_dotenv
import telegram

import fetch_spacex
import fetch_nasa


def post_images(image_filenames, bot_token, channel_id, folder, delay):
    bot = telegram.Bot(token=bot_token)

    for image_filename in image_filenames:
        with open('{}/{}'. format(folder, image_filename), 'rb') as file:
            bot.send_document(chat_id=channel_id, document=file)

        time.sleep(delay)


def main():
    folder = 'images'
    Path(folder).mkdir(parents=True, exist_ok=True)

    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    channel_id = os.getenv('CHANNEL_ID')
    flight_number = os.getenv('FLIGHT_NUMBER')
    delay = float(os.getenv('DELAY', 86400))

    fetch_nasa.fetch_nasa_images(nasa_token, folder)
    fetch_nasa.fetch_epic_images(nasa_token, folder)
    fetch_spacex.fetch_spacex_one_launch(flight_number, folder)

    image_filenames = os.listdir('images')

    while True:
        post_images(image_filenames, bot_token, channel_id, folder, delay)


if __name__ == '__main__':
    main()
