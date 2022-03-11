#!/usr/bin/env python3

import requests
import os
import glob

home = os.path.expanduser('~')
url = 'http://localhost/upload/'
images_dir = glob.glob(home + '/supplier-data/images/*.jpeg')

for image in images_dir:
    with open(image, 'rb') as image_file:
        response = requests.post(url, files={'file': image_file})
