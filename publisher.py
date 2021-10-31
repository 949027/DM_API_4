import time
import telegram
import os
from dotenv import load_dotenv
from pathlib import Path
import fetch_spacex
import fetch_nasa


def main():
    Path('images').mkdir(parents=True, exist_ok=True)
    load_dotenv()
    token_nasa = os.getenv('NASA_TOKEN')
    token_bot = os.getenv('TELEGRAM_BOT_TOKEN')
    delay = float(os.getenv('DELAY', 86400))

    fetch_nasa.fetch_nasa_images(token_nasa)
    fetch_nasa.fetch_epic_images(token_nasa)
    fetch_spacex.fetch_spacex_last_launch()

    image_filenames = os.listdir('images')

    bot = telegram.Bot(token=token_bot)

    while True:
        for image_filename in image_filenames:
            with open(f'images/{image_filename}', 'rb') as file:
                bot.send_document(chat_id=os.getenv('BOT_NAME'), document=file)

            time.sleep(delay)


if __name__ == '__main__':
    main()
