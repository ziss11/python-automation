from PIL import Image
import os
import re

home = os.path.expanduser('~')
with open(home + '/image_filename.txt') as filename:
    for file in filename.readlines():
        img = Image.open(home + '/images/' + file.replace('\n', ''))

        filter_filename = re.findall(r'.+', file)
        filtered_filename = filter_filename[0].replace('.', '')

        img.rotate(90).resize((128, 128)).convert('RGB').save(
            '/opt/icons/' + filtered_filename + '.jpg')
