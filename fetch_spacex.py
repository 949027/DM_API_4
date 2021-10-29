import requests
import publisher


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/74'
    path = 'images/spacex'
    response = requests.get(url)
    response.raise_for_status()

    images_url = response.json()['links']['flickr_images']

    for image_number, image_url in enumerate(images_url):
        response = requests.get(image_url)
        response.raise_for_status()

        publisher.download_image(response, path, image_number, '.jpg')
