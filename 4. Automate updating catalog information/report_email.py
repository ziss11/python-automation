#!/usr/bin/env python3

import reports
import emails
import datetime
import glob
import os

if __name__ == "__main__":
    home = os.path.expanduser('~')
    desc_dir = glob.glob(home + '/supplier-data/descriptions/*.txt')

    paragraph = ''
    for desc_file in desc_dir:
        with open(desc_file) as file:
            text = file.readlines()
            name = text[0]
            weight = text[1]
            desc = text[2]
            weight = int(weight.replace(' lbs', ''))
            paragraph += '<br/>name: {}<br/>weight: {} lbs'.format(
                name, weight)

    date = datetime.date.today()
    month = date.strftime('%B')
    day = date.strftime('%d')
    year = date.strftime('%Y')

    title = 'Processed Update on {} {}, {}'.format(month, day, year)
    reports.generate_report('/tmp/processed.pdf', title, paragraph)

    sender = 'automation@example.com'
    recipient = '{}@example.com'.format(os.environ.get('USER'))
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    attachment_file = '/tmp/processed.pdf'

    message = emails.generate_email(
        sender, recipient, subject, body, attachment_file)
    emails.send_email(message)
