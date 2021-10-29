import requests
from pathlib import Path


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
