import requests


def download_image(url, path, picture_number, picture_extension, payload=''):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(
        '{}{}{}'.format(path, picture_number, picture_extension),
        'wb',
    ) as file:
        file.write(response.content)
