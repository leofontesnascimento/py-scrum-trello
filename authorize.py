# -*- coding: utf-8 -*-

from constants import Constants
from json import dump


def main():
    print('Visit this url: ', Constants.api_key_url)
    api_key = input('Enter API-KEY from browser: ')
    print('Visit this url: ', ''.join(Constants.api_token_url).format(Constants.app_name, api_key))
    api_token = input('Enter API-TOKEN from browser: ')
    with open('credentials.json', 'w') as output_file:
        dump({
            'api_key': api_key,
            'api_token': api_token
        }, output_file)
    print('API-KEY and API-TOKEN saved successfully into file credentials.json')


if __name__ == '__main__':
    main()
