#!/usr/bin/env python
#
# drafts2trello.py
# Sean Korzdorfer
# Mon 2013-05-04

import argparse
import requests
import sys
import json
import webbrowser
import pprint

pp = pprint.PrettyPrinter(indent=4)

def main(args):
    ### Please Set API Credentials ###
    # Set your Trello API Key
    args['key'] = ''
    # Set your Trello API Token
    args['token'] = ''
    # Set position of new card - top, or bottom, or an numerical value
    args['pos'] = 'top'
    bugger = True

    ### Do Not Edit Below This Line ###
    if bugger:
        print '\n\n---- drafts2trello starting ----\n\n'
        print 'Command Line Parsed As:\n\t'
        pp.pprint(args)
    # Trello API POST card URL
    card_add_url = "https://api.trello.com/1/cards"
    # Build argument payload for API card
    payload = {'name': args['card_text'], 'idList' : args['list_id'], 'key' : args['key'], 'token': args['token'], 'desc' : args['card_note'], 'pos' : args['pos']}

    #if args['card_note'] != "":
    #   payload = {'desc' : args['card_note']}

    if bugger:
        print '\n\nPayload for API call\n\n'
        pp.pprint(payload)
    # Make API call. r is the response.
    r = requests.post(card_add_url, data=payload)
    # Parse API response
    parsed_json = json.loads(r.content)
    # Test API response for expected results
    if r.status_code == requests.codes.ok and bugger:
        print '\n\nHTTP Response From Task Note Request:\n\t'
        pp.pprint(parsed_json)
        print('\n\n---- drafts2trello ending ----\n\n')
        webbrowser.open("drafts://")
    elif r.status_code == requests.codes.ok and not bugger:
        webbrowser.open("drafts://")
    else:
        print 'Sorry. There was an error. Your card was not created.'
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('list_id', metavar='N', nargs='+', help='The ID of the list to add tne new card to')
    parser.add_argument('-t', '--card', action='store', dest='card_text', nargs='+', help='The text which will appear in the card title')
    parser.add_argument('-n', '--note', action='store', dest='card_note', nargs='*', help='Card Description')
    parser.add_argument('-v','--version', action='version', version='%(prog)s 1.')
    results = parser.parse_args()

    # Will raise traceback error if missing
    if results.list_id > 0:
        args = {'list_id': ' '.join(results.list_id)}
    # There is a task note, add it to the dictionary
    if results.card_text:
        args['card_text'] = ' '.join(results.card_text)
    # If there is a task tag, add it to the dictionary
    if results.card_note:
        args['card_note'] = ' '.join(results.card_note)
    else:
        args['card_note'] = ""

    main(args)