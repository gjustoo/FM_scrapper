import configparser
import json

import requests


def send_telegram_message(message: str):
    config = configparser.RawConfigParser()
    requests.packages.urllib3.disable_warnings()
    config.read('fm.properties')

    chat_id = config.get('TelegramCredentials', 'telegram.chatId')
    api_key = config.get('TelegramCredentials', 'telegram.api.token')

    responses = {}

    headers = {'Content-Type': 'application/json',
               'Proxy-Authorization': 'Basic base64'}
    data_dict = {'chat_id': chat_id,
                 'text': message,
                 'parse_mode': 'html',
                 'disable_notification': True}
    data = json.dumps(data_dict)
    url = f'https://api.telegram.org/bot{api_key}/sendMessage'
    response = requests.post(url,
                             data=data,
                             headers=headers,
                             verify=False)
    if response.status_code == 200:
        print('Notification sent successfully')
    return response
