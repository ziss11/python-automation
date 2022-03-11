#!/usr/bin/env python3

import os
import mimetypes
import smtplib
import email.message


def generate_email(sender, recipient, subject, body, attachment=None):
    message = email.message.EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    if attachment:
        attachment_filename = os.path.basename(attachment)
        mime_type, _ = mimetypes.guess_type(attachment)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachment, 'rb') as ap:
            message.add_attachment(
                ap.read(),
                maintype=mime_type,
                subtype=mime_subtype,
                filename=attachment_filename,
            )

    return message


def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
