import re
import math
import glob

from collections import Counter, defaultdict


def tf_idf(all_):
    tf_list = []
    counters = []
    # tf part
    for item in all_:
        words = re.findall(string=item.lower(), pattern=r'[a-zA-Z\'\-]+')
        counter = Counter(words)
        counters.append(counter)
        tf_list.append({k: (v + 0.0)/len(words) for k,v in counter.iteritems()})

    # idf part
    word_count = {}
    idf_counter = Counter()
    for counter in counters:
        idf_counter += counter
    for word in idf_counter.keys():
        for counter in counters:
            if word in counter:
               if word in word_count:
                  word_count[word] += 1
               else:
                  word_count[word] = 1
    idf = {word: math.log((len(all_)+0.0)/count) for word, count in word_count.iteritems()}

    # tf-idf part
    tfidf_list = []
    for tf in tf_list:
        tfidf = {}
        for word in tf:
            tfidf[word] = tf[word] * idf[word]
        tfidf_list.append(tfidf)

    result = []
    for item in tfidf_list:
        max_value = 0
        max_key = None
        for k,v in item.iteritems():
            if v > max_value:
                max_value = v
                max_key = k
        result.append(max_key)
    return result

if __name__ == '__main__':
    data = []
    for file in glob.glob('*.txt'):
        with open(file) as fp:
            data.append(fp.read())
    print tf_idf(data)
