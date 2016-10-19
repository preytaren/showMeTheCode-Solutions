#-*- encoding=utf-8 -*-


def get_filter_words(file='test/filter_words.txt'):
    word_list = []
    if not word_list:
        with open(file) as fp:
            for line in fp:
                word_list.append(line[:-1])
    return word_list


def filters():
    word = ''
    filter_word_list = get_filter_words()
    while word != 'END':
        output = 'Human Rights'
        word = raw_input()
        for filter_word in filter_word_list:
            if filter_word in word:
                output = 'Freedom'
                break
        print output

if __name__ == '__main__':
    filters()
