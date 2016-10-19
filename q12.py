import re

from q11 import get_filter_words


def replace_filter():
    word = ''
    filter_words = get_filter_words()
    while word != 'END':
        word = raw_input()
        for filter_word in filter_words:
            word = word.replace(filter_word, '*'*(len(filter_word)/3))
        print word


if __name__ == '__main__':
    replace_filter()
