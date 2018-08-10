# -*- coding: utf-8 -*-


class Constants:
    app_name = 'PyScrumTrello'
    api_key_url = 'https://trello.com/app-key'
    api_token_url = 'https://trello.com/1/authorize?expiration=never&name={}&scope=read&response_type=token&key={}'
    api_url = 'https://api.trello.com'
    credentials_url = '?key={}&token={}'
    boards_route_url = '/1/members/me/boards'
    cards_route_url = '/1/boards/{}/cards'
    lists_route_url = '/1/boards/{}/lists'
    boards_file_name = 'boards.json'
    cards_file_name = 'cards.json'
    lists_file_name = 'lists.json'
