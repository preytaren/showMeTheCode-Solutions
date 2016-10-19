import requests
import re

IMAGE_PATTERN = re.compile(r'<img pic_type="0" class="BDE_Image" src="(.*?)".*?>')


def getSrc(url="http://tieba.baidu.com/p/2166231880"):
    return requests.get(url).text


def func():
    content = getSrc()
    images = IMAGE_PATTERN.findall(content)
    return download(images)


def download(urls, path='images'):
    filenames = []
    for url in urls:
        filename = url.split('/')[-1]
        r = requests.get(url, stream=True)
        with open('{}/{}'.format(path, filename), 'wb') as fp:
            for chunk in r.iter_content(chunk_size=1024):
                fp.write(chunk)
                fp.flush()
                filenames.append(filename)
    return filenames


if __name__ == '__main__':
    print func()
