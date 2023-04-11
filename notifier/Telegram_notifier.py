import configparser
import json
import os

import requests


def send_telegram_message(message: str):
    config = configparser.ConfigParser()

    with open('notifier/notifier.properties') as f:
        config.read_file(f)

    chat_id = os.environ.get('TELEGRAM_CHAT_ID') or config.get(
        'TelegramCredentials', 'telegram.chatId')
    api_key = os.environ.get('TELEGRAM_API_KEY') or config.get(
        'TelegramCredentials', 'telegram.api.token')

    url = f'https://api.telegram.org/bot{api_key}/sendMessage'

    headers = {'Content-Type': 'application/json',
               'Proxy-Authorization': 'Basic base64'}
    data = {'chat_id': chat_id,
            'text': message,
            'parse_mode': 'html',
            'disable_notification': True}

    try:
        response = requests.post(url,
                                 json=data,
                                 headers=headers,
                                 verify=False)
        response.raise_for_status()
        print('Notification sent successfully')
    except requests.exceptions.HTTPError as e:
        print(f'Error sending notification: {e}')
        response = None

    return response


def send_telegram_image(message: str, image_path: str):
    config = configparser.ConfigParser()

    with open('notifier/notifier.properties') as f:
        config.read_file(f)

    chat_id = os.environ.get('TELEGRAM_CHAT_ID') or config.get(
        'TelegramCredentials', 'telegram.chatId')
    api_key = os.environ.get('TELEGRAM_API_KEY') or config.get(
        'TelegramCredentials', 'telegram.api.token')

    url = f'https://api.telegram.org/bot{api_key}/sendPhoto'

    headers = {'Proxy-Authorization': 'Basic base64'}
    files = {'photo': open(image_path, 'rb')}
    data = {'chat_id': chat_id,
            'parse_mode': 'html',
            'caption': message}

    try:
        response = requests.post(url,
                                 data=data,
                                 files=files,
                                 headers=headers,
                                 verify=False)
        response.raise_for_status()
        print('Notification sent successfully')
    except requests.exceptions.HTTPError as e:
        print(f'Error sending notification: {e}')
        response = None

    return response
