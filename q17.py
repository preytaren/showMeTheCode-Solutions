# -*- coding=utf-8 -*-
import xlrd
import json
import os
import xml.etree.cElementTree as ET
from collections import defaultdict

from xml.etree import ElementTree


class CommentedTreeBuilder ( ElementTree.XMLTreeBuilder ):

    def __init__(self, html=0, target=None):
        ElementTree.XMLTreeBuilder.__init__(self, html, target)
        self._parser.CommentHandler = self.handle_comment

    def handle_comment ( self, data ):
        self._target.start( ElementTree.Comment, {} )
        self._target.data( data )
        self._target.end( ElementTree.Comment )


def run():
    # read xls file
    wkb = xlrd.open_workbook('test/students.xls')
    sheet = wkb.sheets()[0]
    data = defaultdict(list)
    for row in range(sheet.nrows):
        for col in range(1, sheet.ncols):
            data[str(row)].append(sheet.cell(row, col).value)
    students_data = json.dumps(data, indent=4)

    # write xml file
    root = ET.Element('root')
    tree = ET.ElementTree(root)
    students = ET.SubElement(root, 'students')
    comment = ET.Comment(u'{space}学生信息表 "id" : [名字, 数学, 语文, 英文]{space}'.format(space=os.linesep))
    students.text = u'{students_data}'.format(students_data=students_data.__str__())
    students.insert(1, comment)
    tree.write('test/students.xml', encoding='utf-8', xml_declaration=True)

if __name__ == '__main__':
    run()
