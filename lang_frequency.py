import os
import re
import string
import argparse
from collections import Counter


def load_data(path, codec):
    if os.path.isfile(path):
        with open(path, 'r', encoding=codec) as file_to_read:
            return file_to_read.read()


def get_most_frequent_words(text, quantity):
    words = text.split(' ')
    return Counter(words).most_common(quantity)


def clear_text(text):
    long_dash_utf8 = '—'
    long_dash_cp1251 = '–'
    for char in '{}{}{}'.format(
        string.punctuation,
        long_dash_utf8,
        long_dash_cp1251,
    ):
        text = text.replace(char, ' ')
    text = re.sub('\s+', ' ', text)
    return text


def get_args(list_of_allowable_codecs):
   parser = argparse.ArgumentParser(
        description='Frequency Analysis of Words'
   )
   parser.add_argument(
        'path',
        metavar='path',
        type=str,
        help='File path'
   )
   parser.add_argument(
        '-q',
        '--quantity',
        action='store',
        nargs='?',
        type=int,
        default=10,
        help='How many frequent words to display'
   )
   parser.add_argument(
        '-c',
        '--codec',
        action='store',
        nargs='?',
        default='utf_8',
        choices=list_of_allowable_codecs,
        help='Use for decode a original file',
   )
   return parser.parse_args()


if __name__ == '__main__':
    codecs = [
        'utf_8',
        'cp1251',
        'koi8_r',
        'cp866',
        'mac_cyrillic',
    ]
    args = get_args(codecs)
    try:
        text = load_data(args.path, args.codec)
    except UnicodeDecodeError as error:
        print('{}\nCannot read file {} with {} codec\n{}'.format(
            error,
            args.path,
            args.codec,
            'Try to use other codec',
        ))
    else:
        if text is not None:
            text = clear_text(text)
            most_frequent_words = get_most_frequent_words(text, args.quantity)
            for word, entrances in most_frequent_words:
                print('{}\t{}'.format(word, entrances))
        else:
            print('Cannot open "{}" '.format(args.path))
