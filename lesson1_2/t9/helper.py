import re
import sys


keymap= {
    '2 ': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

def get_key_for_char(char):
    for key, chars in keymap.items():
        if char in chars:
            return key


def ask_for_numbers():
    while True:
        response = str(input('What numbers have you pressed? ')).strip()
        if len(response) < 3:
            print('You need to enter at least three numbers.')
        elif re.search("[^2-9]", response):
            print("You entered a character that isn't one of 2, 3, 4, 5, 6, 7, 8, or 9. Please try again.")
        else:
            return response


def read_content(filename='words.txt'):
    with open(filename, 'r') as f:
        return f.read().strip().replace(',', ' ')

