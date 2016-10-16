import re
from functools import partial


def find_content(html, tag):
    tag_pattern = re.compile('\<{}\>(.*?)\<\/{}\>'.format(tag, tag), re.S)
    return tag_pattern.findall(html)

find_body = partial(find_content, tag='body')


if __name__ == '__main__':
    with open('test/q8.html') as fp:
        content = fp.read()
        print find_body(content)
