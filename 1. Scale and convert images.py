from PIL import Image
import os
import re

home = os.path.expanduser('~')
with open(home + '/image_filename.txt') as filename:
    for file in filename.readlines():
        image_filename = file.replace('\n', '')
        img = Image.open(home + '/images/' + image_filename)

        img.rotate(90).resize((128, 128)).convert('RGB').save(
            '/opt/icons/' + image_filename, 'JPEG')
