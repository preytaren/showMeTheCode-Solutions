# -*- coding=utf-8 -*-
import xlrd
import json
import os
import xml.etree.cElementTree as ET
from collections import defaultdict


def run():
    # read xls file
    wkb = xlrd.open_workbook('test/students.xls')
    sheet = wkb.sheets()[0]
    data = defaultdict(list)
    for row in range(sheet.nrows):
        for col in range(1, sheet.ncols):
            data[str(row+1)].append(sheet.cell(row, col).value)
    students_data = json.dumps(data, indent=4, ensure_ascii=False)

    # write xml file
    root = ET.Element('root')
    tree = ET.ElementTree(root)
    students = ET.SubElement(root, 'students')
    comment = ET.Comment(u'{space}学生信息表 "id" : [名字, 数学, 语文, 英文]{space}'.format(space=os.linesep))
    students.text = students_data
    students.insert(1, comment)
    tree.write('test/students.xml', encoding='utf-8', xml_declaration=True)


if __name__ == '__main__':
    run()
