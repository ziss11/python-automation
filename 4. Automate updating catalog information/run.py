#!/usr/bin/env python3

import os
import requests
import glob
import re

home = os.path.expanduser('~')
desc_dir = glob.glob(home + '/supplier-data/descriptions/*.txt')

fruits_list = list()
for txt in desc_dir:
    regex_result = re.findall(r'/descriptions/.+\.', txt)
    image_name = regex_result[0].replace('/descriptions/', '').replace('.', '')
    with open(txt) as txtfile:
        text = txtfile.readlines()
        fruits = dict()
        fruits['name'] = text[0].strip()
        fruits['weight'] = int(text[1].strip().replace(' lbs', ''))
        fruits['description'] = text[2].strip()
        fruits['image_name'] = image_name + '.jpeg'
        fruits_list.append(fruits)

print(fruits_list)
for fruits in fruits_list:
    response = requests.post('http://34.134.67.203/fruits/', data=fruits)
    print(response.ok)
