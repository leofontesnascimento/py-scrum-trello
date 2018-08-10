# -*- coding: utf-8 -*-

from constants import Constants
from json import dump


def write_json(file_name, data):
    with open(file_name, 'w') as f_output:
        dump(data, f_output, indent=4, sort_keys=True, ensure_ascii=False)


def main():
    # Getting the Key
    print('Visit this url: ', Constants.api_key_url)
    api_key = input('Enter API-KEY from browser: ')

    # Getting the Token
    print('Visit this url: ', ''.join(Constants.api_token_url).format(Constants.app_name, api_key))
    api_token = input('Enter API-TOKEN from browser: ')

    # Saving credentials
    data = {
        'api_key': api_key,
        'api_token': api_token
    }
    write_json('credentials.json', data)
    print('API-KEY and API-TOKEN saved successfully into file credentials.json')


if __name__ == '__main__':
    main()
