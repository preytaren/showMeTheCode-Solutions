# -*- coding=utf-8 -*-
import xlrd
import json
import os
import codecs
from collections import OrderedDict

import xml.dom.minidom as dom


def run():
    wkb = xlrd.open_workbook('test/city.xls')
    sheet = wkb.sheets()[0]
    data = OrderedDict()
    for row in range(sheet.nrows):
        for col in range(1, sheet.ncols):
            data[str(row+1)] = sheet.cell(row, col).value
    city_data = json.dumps(data, indent=4, ensure_ascii=False)

    document = dom.Document()
    document.toxml('utf-8')
    root = document.createElement('root')
    comment = document.createComment(u'{space}    城市信息   {space}'.format(space=os.linesep))
    citys = document.createElement('citys')
    city_text = document.createTextNode(city_data)
    citys.appendChild(city_text)
    citys.appendChild(comment)
    root.appendChild(citys)
    document.appendChild(root)

    with codecs.open('test/city.xml', 'w', encoding='utf-8') as fp:
        document.toprettyxml(indent='')
        fp.write(document.toprettyxml(indent='').replace('&quot;', '"'))


if __name__ == '__main__':
    run()

