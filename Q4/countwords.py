import re

WORD_PATTERN = re.compile(r'[a-zA-Z\-\']+')


def word_count(filename):
    with open(filename) as fp:
        global WORD_PATTERN
        words = []
        for line in fp:
            for word in WORD_PATTERN.finditer(line):
                words.append(word)
    return len(words)


if __name__ == '__main__':
    print word_count('test.txt')
