import xlwt
import json


def run():
    with open('test/students.txt') as fp:
        stu_info = json.load(fp)
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('sheet 1')
        for idx, student in stu_info.iteritems():
            # name, score1, score2, score3 = student
            row = int(idx) - 1
            sheet.write(row,0,idx)
            for colomn, item in enumerate(student):
                sheet.write(row, (colomn+1), item)
        wbk.save('test/students.xls')


if __name__ == '__main__':
    run()
