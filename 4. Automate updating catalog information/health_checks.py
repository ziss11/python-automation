#!/usr/bin/env python3

import psutil
import socket
import os
import emails

max_cpu = 80
min_disk = 20
min_memory = 500
localhost = '127.0.0.1'


def check_CPU():
    cpu_usage = psutil.cpu_percent()
    return cpu_usage > max_cpu


def check_disk():
    disk_usage = psutil.disk_usage('/').percent
    return disk_usage > (100 - min_disk)


def check_memory():
    mb = 2 ** 20
    memory_usage = psutil.virtual_memory().available
    return memory_usage < (mb * min_memory)


def check_connectivity():
    localhost_ip = socket.gethostbyname('localhost')
    return localhost_ip != localhost


def send_alert(message):
    sender = 'automation@example.com'
    recipient = '{}@example.com'.format(os.environ.get('USER'))
    subject = alert
    body = 'Please check your system and resolve the issue as soon as possible.'

    try:
        message = emails.generate_email(sender, recipient, subject, body)
        emails.send_email(message)
    except:
        print(alert)
        exit(1)


if __name__ == '__main__':
    alert = ''

    if check_CPU():
        alert = 'Error - CPU usage is over {}%'.format(max_cpu)
    elif check_disk():
        alert = 'Error - Available disk space is less than {}%'.format(
            min_disk)
    elif check_memory():
        alert = 'Error - Available memory is less than {}MB'.format(min_memory)
    elif check_connectivity():
        alert = 'Error - localhost cannot be resolved to {}'.format(localhost)

    if alert:
        send_alert(alert)
    else:
        print('Everything is ok.')
