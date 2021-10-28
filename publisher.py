import time
import telegram
import os
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('TOKEN_BOT_TELEGRAM')
    delay = float(os.getenv('DELAY', 86400))
    images_filename = os.listdir('images/EPIC')

    bot = telegram.Bot(token=token)

    while True:
        for image in images_filename:
            bot.send_document(
                chat_id='@test_devman',
                document=open(f'images/EPIC/{image}', 'rb'),
            )
            time.sleep(delay)
