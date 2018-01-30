import os
import re
import argparse
from collections import Counter


def load_data(path, codec):
    if os.path.isfile(path):
        with open(path, 'r', encoding=codec) as file_to_read:
            return file_to_read.read()


def get_most_frequent_words(words):
    return Counter(words).most_common()


def extract_words(text):
    words = re.findall('[a-zа-я]+', text, re.IGNORECASE)
    return [word.lower() for word in words]


def get_args():
    parser = argparse.ArgumentParser(
        description='Frequency Analysis of Words'
    )
    parser.add_argument(
        'path',
        metavar='path',
        help='File path'
    )
    parser.add_argument(
        '-q',
        '--quantity',
        type=int,
        default=10,
        help='How many frequent words to display'
    )
    parser.add_argument(
        '-c',
        '--codec',
        default='utf_8',
        help='{}\n{}'.format(
            'Use for decode an original file. Popular codecs: ',
            'utf_8, cp1251, koi8_r, cp866, mac_cyrillic',
        )
    )
    parser.add_argument(
        '-r',
        '--reverse',
        action='store_true',
        help='Use for getting less frequent words',
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    print(args)
    try:
        text = load_data(args.path, args.codec)
        if text:
            words = extract_words(text)
            most_frequent_words = get_most_frequent_words(words)
            most_frequent_words = args.reverse and (
                most_frequent_words[:-args.quantity:-1]
            ) or most_frequent_words[:args.quantity]
            for word, entrances in most_frequent_words:
                print('{}\t{}'.format(word, entrances))
        else:
            print('Cannot open "{}" '.format(args.path))
    except (UnicodeDecodeError, LookupError) as error:
        print('{}\nCannot read file {} with {} codec\n{}'.format(
            error,
            args.path,
            args.codec,
            'Try to use other codec',
        ))
