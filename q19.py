# -*- coding=utf-8 -*-
import xlrd
import json
import os
import codecs
from collections import OrderedDict

import xml.dom.minidom as dom


def run():
    wkb = xlrd.open_workbook('test/numbers.xls')
    sheet = wkb.sheets()[0]
    data = []
    for row in range(sheet.nrows):
        temp = []
        for col in range(sheet.ncols):
            temp.append(sheet.cell(row, col).value)
        data.append(temp)
    number_data = json.dumps(data, indent=4, ensure_ascii=False)

    document = dom.Document()
    document.toxml('utf-8')
    root = document.createElement('root')
    comment = document.createComment(u'{space}    数字信息    {space}'.format(space=os.linesep))
    numbers = document.createElement('numbers')
    number_text = document.createTextNode(number_data)
    numbers.appendChild(number_text)
    numbers.appendChild(comment)
    root.appendChild(numbers)
    document.appendChild(root)

    with codecs.open('test/numbers.xml', 'w', encoding='utf-8') as fp:
        document.toprettyxml(indent='')
        fp.write(document.toprettyxml(indent='').replace('&quot;', '"'))


if __name__ == '__main__':
    run()

