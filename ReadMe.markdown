# Drafts2Trello

Inspired by Tim Broder's [Automate Adding to Trello on iOS with Launch Center Pro and Pythonista][1].

## Differences:
 * This script adds support for adding text to the card's desription. (You can send Markdown formatted text.)
 * This script uses argparse.
 * This script uses Requests for the API calls.

## Expected Arguments:

	`list id -t this is the card text -n this is the card description text`

### Options:

	-n, --note :    Card Description (Optional)
	-t, --tag  :    Card text (Required)
	-v, --version : Script version
	-h, --help :    script help

## Installation
1. Get Trello API Key: [https://trello.com/1/appKey/generate][2]
2. Get Trello API Token:  https://trello.com/1/connect?key=YOUR-KEY&name=drafts2trello&response\_type=token&scope=read,write 
	* NB: Replace 'YOUR-KEY' with the key returned in step 1.
3. Retrieve List IDs: [See Tim Broders script][3].
4. Add the key and the token where specified below. (Lines 19 and 21.)
5. Set value for the position you want your created cards to be placed.
	* Line 23: args\['pos'] = (top, bottom, or numerical value)
6. Set if you want the script to output the arguments passed to the script,
the arguments collected for the API call, and the API response.
	* Line 24: bugger = (True or False)

## Example Drafts URL Action

	`pythonista://drafts2trello?action=run&args=YOUR\_LIST\_ID{{ -t }}\[[title]]{{ -n }}[[[body]]]`

Where YOUR\_LIST\_ID should be replaced by the list ID you want to add a card to. This allows you to use the same Pythonista script for multiple Draft URL actions.

## Change Log

Version 1 - 2013-05-04

## Additional Comments

* Try to keep the card description terse–the longer the card name and description, the longer it takes the script to run.
* I'm considering befing up the script with support for adding checklists, list items and labels.


[1]:	http://timbroder.com/2013/03/automating-adding-to-trello-on-ios.html
[2]:	https://trello.com/1/appKey/generate
[3]:	http://timbroder.com/2013/03/automating-adding-to-trello-on-ios.html