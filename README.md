# PyScrumTrello

These Python codes aims to get Scrum metrics from the Trello tool.

## Features

* Instanciates a client for Trello.
* Gets data boards from Trello.

## Installation

Steps:

1. Execute `$ make install` into your console.
2. Get your app key and app secret by logging into Trello and visiting `https://trello.com/app-key`.
3. Copy and paste these infromations into file `constants.py`. You must replace the strings `YOUR_APP_KEY` and `YOUR_APP_SECRET` respectively.
4. Save `constants.py` with your changes.
5. Now you are ready to enjoy!.

## Example get-all-boards command usage

Steps:

1. Execute `$ make get-all-boards` into your console.
2. Visit the URL suggested using your browser.
3. Give permission to the client to access your boards.
4. Copy and paste the verification code into your console.
5. Press `Enter` and wait the crawler conclued process.
6. Analyze the downloaded file named `data/YYY-mm-dd/boards.json`. The directory `/YYYY-mm-dd` will change according to current day.

## Example get-board-by-id command usage

Steps:

1. Choose a specific board in file named `data/YYY-mm-dd/boards.json` and copy its `id`. The directory `/YYYY-mm-dd` will change according to current day.
2. Execute `$ make get-board-by-id ARGS=id ` into your console. Replace `id` by value copied previously.
3. Visit the URL suggested using your browser.
4. Give permission to the client to access your boards.
5. Copy and paste the verification code into your console.
6. Press `Enter` and wait the crawler conclued process.
7. Analyze the downloaded file named `data/YYY-mm-dd/cards.json`. The directory `/YYYY-mm-dd` will change according to current day.
8. Analyze the downloaded file named `data/YYY-mm-dd/lists.json`. The directory `/YYYY-mm-dd` will change according to current day.
