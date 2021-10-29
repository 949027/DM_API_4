import time
import telegram
import os
from dotenv import load_dotenv
from pathlib import Path
import fetch_spacex
import fetch_nasa


def download_image(response, path, picture_number, picture_extension):
    with open(
            '{}{}{}'.format(path, picture_number, picture_extension),
            'wb',
    ) as file:
        file.write(response.content)


def main():
    Path('images').mkdir(parents=True, exist_ok=True)
    load_dotenv()
    token_nasa = os.getenv('TOKEN_NASA')
    token_bot = os.getenv('TOKEN_BOT_TELEGRAM')
    delay = float(os.getenv('DELAY', 86400))

    fetch_nasa.fetch_nasa_image(token_nasa)
    fetch_nasa.fetch_epic_image(token_nasa)
    fetch_spacex.fetch_spacex_last_launch()

    image_filenames = os.listdir('images')

    bot = telegram.Bot(token=token_bot)

    while True:
        for image_filename in image_filenames:
            with open(f'images/{image_filename}', 'rb') as file:
                bot.send_document(chat_id=os.getenv('NAME_BOT'), document=file)

            time.sleep(delay)


if __name__ == '__main__':
    main()
