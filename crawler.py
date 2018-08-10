# -*- coding: utf-8 -*-

from datetime import datetime
import getopt
import json
import os
import requests
import sys

from constants import Constants


def write_json(file_name, data):
    now = datetime.now().strftime('%Y-%m-%d')
    directory = 'data/{}/'.format(now)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(directory + file_name, 'w') as f_output:
        json.dump(
            data,
            f_output,
            indent=4,
            sort_keys=True,
            ensure_ascii=False)


def get_data(credentials, route_url, file_name):
    response = requests.get(
        ''.join(Constants.api_url) +
        route_url +
        ''.join(Constants.credentials_url).format(
            credentials['api_key'],
            credentials['api_token']
        ))

    if response.status_code == requests.codes.ok:
        data = response.json()
        write_json(file_name, data)
    else:
        response.raise_for_status()


def main(argv):
    # Getting credentials
    with open('credentials.json') as f_input:
        credentials = json.load(f_input)

    # Getting all boards data
    get_data(
        credentials,
        ''.join(Constants.boards_route_url),
        ''.join(Constants.boards_file_name))

    # Getting command-line arguments
    board_id = ''
    if len(argv) > 0:
        try:
            opts, args = getopt.getopt(argv, 'hi:', ['boardid='])
        except getopt.GetoptError:
            print('crawler.py -i <boardid>')
            sys.exit(2)
        for opt, arg, in opts:
            if opt == '-h':
                print('crawler.py -i <boardid>')
                sys.exit()
            elif opt in ('-i', '--boardid'):
                board_id = arg

        # Getting all cards data of a board
        get_data(
            credentials,
            ''.join(Constants.cards_route_url).format(board_id),
            ''.join(Constants.cards_file_name))

        #  Gettinf all lists of a board
        get_data(
            credentials,
            ''.join(Constants.lists_route_url).format(board_id),
            ''.join(Constants.lists_file_name))


if __name__ == '__main__':
    main(sys.argv[1:])
