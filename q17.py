import xlrd
import json
import xml.dom.minidom as minidom
from collections import defaultdict


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
    impl = minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'students', None)
    root = dom.documentElement
    students = dom.createElement('students')
    root.appendChild(students)


if __name__ == '__main__':
    run()
