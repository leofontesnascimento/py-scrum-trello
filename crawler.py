# -*- coding: utf-8 -*-

from datetime import datetime
import getopt
import json
import os
from rauth import OAuth1Service
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


def get_data(session, route_url, file_name):
    response = session.get(
        ''.join(Constants.api_url) + route_url,
        params={},
        verify=True)
    data = response.json()
    write_json(file_name, data)


def main(argv):
    # Getting the token
    trello = OAuth1Service(
        name=Constants.app_name,
        consumer_key=Constants.app_key,
        consumer_secret=Constants.app_secret,
        request_token_url=Constants.request_token_url,
        access_token_url=Constants.access_token_url,
        authorize_url=Constants.authorize_token_url,
        base_url=Constants.base_url)

    request_token, request_token_secret = trello.get_request_token()
    print('request_token: ', request_token)
    print('request_token_secret: ', request_token_secret)

    # Allowing for the crawler
    authorize_url = trello.get_authorize_url(request_token)
    print('Visit this url: ', authorize_url)
    code = input('Enter PIN from browser: ')
    session = trello.get_auth_session(
        request_token,
        request_token_secret,
        method='POST',
        data={'oauth_verifier': code})

    # Getting all boards data
    get_data(
        session,
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
            session,
            ''.join(Constants.cards_route_url).format(board_id),
            ''.join(Constants.cards_file_name))

        #  Gettinf all lists of a board
        get_data(
            session,
            ''.join(Constants.lists_route_url).format(board_id),
            ''.join(Constants.lists_file_name))


if __name__ == '__main__':
    main(sys.argv[1:])
