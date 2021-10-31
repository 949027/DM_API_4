def download_image(response, path, picture_number, picture_extension):
    with open(
            '{}{}{}'.format(path, picture_number, picture_extension),
            'wb',
    ) as file:
        file.write(response.content)