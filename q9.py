from HTMLParser import HTMLParser


class LinkParser(HTMLParser):

    links = {}
    temp_tag = None
    temp_link = None

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.temp_link = attr[1]
        self.temp_tag = tag

    def handle_endtag(self, tag):
        self.temp_tag = None

    def handle_data(self, data):
        if self.temp_tag == 'a':
            self.links[data] = self.temp_link


def find_links(html):
    """
    Find all links in an html format string
    :param html: html string
    :return: a dict contains all links in html,
             :key link name :value link itself
    """
    parser = LinkParser()
    parser.feed(html)
    return parser.links


if __name__ == '__main__':
    with open('test/q8.html') as fp:
        print find_links(fp.read())

