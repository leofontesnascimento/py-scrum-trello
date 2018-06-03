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


def get_dict_cards(directory, list_ids, list_labels):
    list_ids.reverse()
    list_labels.reverse()
    days = get_subdirectories(directory)
    dict_cards = {}

    for day in days:
        cards = parse_json('{}{}/cards.json'.format(directory, day))
        dict_list = {}
        for i in range(0, len(list_ids)):
            list_cards = []
            for card in cards:
                if card['idList'] == list_ids[i]:
                    list_cards.append(card)
            dict_list[str(i) + list_labels[i]] = len(list_cards)
        dict_cards[day] = dict_list

    return dict_cards


def generate_cfd(dict_cards):
    days = list(dict_cards.keys())
    days.sort()
    labels = list(dict_cards[days[0]].keys())
    labels.sort()
    y = []

    # Printing values
    for day in days:
        for label in labels:
            print(day, ': ', label[1:], ': ', dict_cards[day][label])
        print('-----------------------------')

    # Building y axis
    for label in labels:
        list_cards = []
        for day in days:
            list_cards.append(dict_cards[day][label])
        y.append(list_cards)

    # Building x axis
    x = np.arange(len(days))

    # Plotting chart
    plt.stackplot(x, y, labels=[l[1:] for l in labels])
    plt.legend(loc='upper left')
    plt.xticks(x, days)
    plt.show()


def main(argv):
    # Getting command-line arguments
    ids = ''
    labels = ''
    if len(argv) > 0:
        try:
            opts, args = getopt.getopt(argv, 'hi:l:', ['listids=', 'listlabels='])
        except getopt.GetoptError:
            print('cfd-generator.py -i <listids> -l <listlabels>')
            sys.exit(2)
        for opt, arg, in opts:
            if opt == '-h':
                print('cfd-generator.py -i <listids> -l <listlabels>')
                sys.exit()
            elif opt in ('-i', '--listids'):
                ids = arg
            elif opt in ('-l', '--listlabels'):
                labels = arg

    list_ids = ids.split(',')
    list_labels = labels.split(',')

    # Getting a dictionary of all list cards
    dict_cards = get_dict_cards('data/', list_ids, list_labels)

    # Plotting the cumulative flow diagram (cfd) chart
    generate_cfd(dict_cards)


if __name__ == '__main__':
    main(sys.argv[1:])
