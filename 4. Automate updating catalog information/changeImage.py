#!/usr/bin/env python3

from PIL import Image
import os
import subprocess
import glob
import re

home = os.path.expanduser('~')
image_save_dir = home+'/supplier-data/images/'
images_dir = glob.glob(home + '/supplier-data/images/*.tiff')

for image in images_dir:
    regex_result = re.findall(r'/images/.+\.', image)
    image_name = regex_result[0].replace('/images/', '').replace('.', '')
    img = Image.open(image)
    img.convert('RGB').resize((600, 400)).save(
        image_save_dir + image_name + '.jpeg', 'JPEG')
