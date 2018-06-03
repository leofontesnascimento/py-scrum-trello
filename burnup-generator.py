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


def get_dict_cards(directory, list_id):
    days = get_subdirectories(directory)
    dict_cards = {}
    for day in days:
        cards = parse_json('{}{}/cards.json'.format(directory, day))
        cards_day = []
        for card in cards:
            if card['idList'] == list_id:
                cards_day.append(card)
        dict_cards[day] = cards_day

    return dict_cards


def generate_burnup(done_cards):
    days = list(done_cards.keys())
    days.sort()
    total_cards = []

    for day in days:
        print(day, ': ', len(done_cards[day]))
        total_cards.append(len(done_cards[day]))

    y_pos = np.arange(len(days))
    plt.bar(y_pos, total_cards, color='darkgreen')
    plt.xticks(y_pos, days)
    plt.savefig('chart/burnup.png')
    plt.show()


def main(argv):
    # Getting command-line arguments
    listid = ''
    if len(argv) > 0:
        try:
            opts, args = getopt.getopt(argv, 'hl:', ['listid='])
        except getopt.GetoptError:
            print('burnup-generator.py -l <listid>')
            sys.exit(2)
        for opt, arg, in opts:
            if opt == '-h':
                print('burnup-generator.py -l <listid>')
                sys.exit()
            elif opt in ('-l', '--listid'):
                listid = arg

    # Getting a dictionary of all done cards
    done_cards = get_dict_cards('data/', listid)

    # Plotting the burnup chart
    generate_burnup(done_cards)


if __name__ == '__main__':
    main(sys.argv[1:])
