import requests

import download


def fetch_spacex_one_launch(flight_number, folder):
    url = f'https://api.spacexdata.com/v3/launches/{flight_number}'
    path = f'{folder}/spacex'
    response = requests.get(url)
    response.raise_for_status()

    image_urls = response.json()['links']['flickr_images']

    for image_number, image_url in enumerate(image_urls):
        download.download_image(image_url, path, image_number, '.jpg')
