# -*- coding: utf-8 -*-

import getopt
import json
import os
import sys

import numpy as np
import matplotlib.pyplot as plt


def get_subdirectories(directory):
    subs = os.listdir(directory)
    subs.remove('__init__.py')
    return subs


def parse_json(file_name):
    with open(file_name, 'r') as json_data:
        return json.load(json_data)


def get_dict_cards(directory, list_ids):
    days = get_subdirectories(directory)
    dict_cards = {}
    for day in days:
        cards = parse_json('{}{}/cards.json'.format(directory, day))
        cards_day = []
        for card in cards:
            if card['idList'] in list_ids:
                cards_day.append(card)
        dict_cards[day] = cards_day

    return dict_cards


def generate_burndown(backlog_cards):
    days = list(backlog_cards.keys())
    days.sort()
    total_cards = []

    for day in days:
        print(day, ': ', len(backlog_cards[day]))
        total_cards.append(len(backlog_cards[day]))

    y_pos = np.arange(len(days))
    plt.bar(y_pos, total_cards, color='darkblue')
    plt.xticks(y_pos, days)
    plt.show()


def main(argv):
    # Getting command-line arguments
    ids = ''
    if len(argv) > 0:
        try:
            opts, args = getopt.getopt(argv, 'hl:', ['listids='])
        except getopt.GetoptError:
            print('burndown-generator.py -l <listids>')
            sys.exit(2)
        for opt, arg, in opts:
            if opt == '-h':
                print('burndown-generator.py -l <listids>')
                sys.exit()
            elif opt in ('-l', '--listids'):
                ids = arg

    list_ids = ids.split(',')

    # Getting a dictionary of all backlog cards
    backlog_cards = get_dict_cards('data/', list_ids[:-1])

    # Plotting the burndown chart
    generate_burndown(backlog_cards)


if __name__ == '__main__':
    main(sys.argv[1:])
