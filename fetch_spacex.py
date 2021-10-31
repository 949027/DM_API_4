import requests
import download


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/74'
    path = 'images/spacex'
    response = requests.get(url)
    response.raise_for_status()

    image_urls = response.json()['links']['flickr_images']

    for image_number, image_url in enumerate(image_urls):
        download.download_image(image_url, path, image_number, '.jpg')
