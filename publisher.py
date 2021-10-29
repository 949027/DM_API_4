import time
import telegram
import os
from dotenv import load_dotenv
from pathlib import Path
import fetch_nasa
import fetch_spacex


def main():
    Path('images').mkdir(parents=True, exist_ok=True)
    load_dotenv()
    token_nasa = os.getenv('TOKEN_NASA')
    token_bot = os.getenv('TOKEN_BOT_TELEGRAM')
    delay = float(os.getenv('DELAY', 86400))

    # fetch_nasa.fetch_nasa_image('https://api.nasa.gov/planetary/apod', token_nasa)
    # fetch_nasa.fetch_epic_image('https://api.nasa.gov/EPIC/api/natural/images', token_nasa)
    # fetch_spacex.fetch_spacex_last_launch('https://api.spacexdata.com/v3/launches/74')

    image_filenames = os.listdir('images')

    bot = telegram.Bot(token=token_bot)

    while True:
        for image_filename in image_filenames:
            with open(f'images/{image_filename}', 'rb') as file:
                bot.send_document(chat_id=os.getenv('NAME_BOT'), document=file)

            time.sleep(delay)


if __name__ == '__main__':
    main()
