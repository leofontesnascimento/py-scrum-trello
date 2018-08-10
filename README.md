# PyScrumTrello

These Python codes aims to get Scrum metrics from the Trello tool.

## Features

* Instanciates a client for Trello.
* Gets data boards from Trello.
* Generates the Burndown chart.
* Generates the Burnup chart.
* Generates the CFD (Cumulative Flow Diagram) chart.

## Installation

Steps:

1. Execute `$ make install` into your console.
2. Get your app key and app secret by logging into Trello and visiting `https://trello.com/app-key`.
3. Copy and paste these infromations into file `constants.py`. You must replace the strings `YOUR_APP_KEY` and `YOUR_APP_SECRET` respectively.
4. Save `constants.py` with your changes.
5. Now you are ready to enjoy!.

## Example authorize command usage

Steps:

1. Execute `$ make authorize` into your console.
2. Visit the URL suggested using your browser.
3. Get your api key by logging into Trello in web page opened by last command.
4. Copy and paste this information into your console.
5. Press `Enter`
6. Visit the other URL suggested using your browser.
7. Give permission to the client to access your boards.
8. Get your permanent api token in web page opened by last command.
9. Copy and paste this information into your console.
10. Press `Enter`
11. Close the web pages opened previously.

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

## Example generate-burndown-chart command usage

Steps:

1. Execute `$ make generate-burndown-chart ARGS=todo_list_id,wip_list_id,in_review_list_id,done_list_id` into your console, ids separated by commas only. Replace `todo_list_id,wip_list_id,in_review_list_id,done_list_id` by all list ids representing the completed workflow of your cards on the board. You might find theses informations analyzing the downloaded file named `data/YYY-mm-dd/lists.json`. The directory `/YYYY-mm-dd` will change according to the day of download.
2. Analyze the plotted Burndown chart. You save into a file if you want.
3. Verify the cards informations into your console.
4. Save this command to use again in the future.

Result:

![Alt text](/chart/burndown.png?raw=true "Burndown")

## Example generate-burnup-chart command usage

Steps:

1. Execute `$ make generate-burnup-chart ARGS=done_list_id` into your console. Replace `done_list_id` by list id representing the completed cards on the board. You might find this information analyzing the downloaded file named `data/YYY-mm-dd/lists.json`. The directory `/YYYY-mm-dd` will change according to the day of download.
2. Analyze the plotted Burnup chart. You save into a file if you want.
3. Verify the cards informations into your console.
4. Save this command to use again in the future.

Result:

![Alt text](/chart/burnup.png?raw=true "Burnup")

## Example generate-cfd-chart command usage

Steps:

1. Execute `$ make generate-cfd-chart IDS=todo_list_id,wip_list_id,in_review_list_id,done_list_id LABELS=todo_list_label,wip_list_label,in_review_list_label,done_list_label` into your console, ids and labels separated by commas only. Replace these informations according to all list representing the completed workflow of your cards, in the order in which a card enters, walking and leaves the board. You might find this informations analyzing the downloaded file named `data/YYY-mm-dd/lists.json`. The directory `/YYYY-mm-dd` will change according to the day of download.
2. Analyze the plotted CFD chart. You save into a file if you want.
3. Verify the cards informations into your console.
4. Save this command to use again in the future.

Result:

![Alt text](/chart/cfd.png?raw=true "Cumulative Flow Diagram")

## More informations

These Python codes was developed based in this  [article](https://www.excella.com/insights/burndown-chart-vs-cumulative-flow-diagram-cfd).
