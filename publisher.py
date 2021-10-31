import time
import telegram
import os
from dotenv import load_dotenv
from pathlib import Path
import fetch_spacex
import fetch_nasa


def post_images_in_telegram(image_filenames, bot_token, folder):
    bot = telegram.Bot(token=bot_token)
    delay = float(os.getenv('DELAY', 86400))

    for image_filename in image_filenames:
        with open('{}/{}'. format(folder, image_filename), 'rb') as file:
            bot.send_document(chat_id=os.getenv('BOT_NAME'), document=file)

        time.sleep(delay)


def main():
    folder = 'images'
    Path(folder).mkdir(parents=True, exist_ok=True)

    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    flight_number = os.getenv('FLIGHT_NUMBER')

    # fetch_nasa.fetch_nasa_images(nasa_token, folder)
    # fetch_nasa.fetch_epic_images(nasa_token, folder)
    fetch_spacex.fetch_spacex_one_launch(flight_number, folder)

    image_filenames = os.listdir('images')

    while True:
        post_images_in_telegram(image_filenames, bot_token, folder)


if __name__ == '__main__':
    main()
