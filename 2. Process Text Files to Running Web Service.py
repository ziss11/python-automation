import os
import requests

txt_file_path = '/data/feedback/'
txt_files_list = os.listdir('/data/feedback/')

feedback_list = list()

for txt in txt_files_list:
    txt_file = txt_file_path + txt
    with open(txt_file) as feedback_file:
        feedback_json = dict()
        (feedback_json['title'],
         feedback_json['name'],
         feedback_json['date'],
         feedback_json['feedback']) = feedback_file.readlines()
        feedback_list.append(feedback_json)

for feedback in feedback_list:
    response = requests.post('http://35.223.111.118/feedback/', data=feedback)
    print(response.status_code)
