import xlwt
import json


def run():
    with open('test/city.txt') as fp:
        city_info = json.load(fp)
    wkb = xlwt.Workbook()
    sheet = wkb.add_sheet('sheet 1')
    for idx, city in city_info.iteritems():
        row = int(idx) - 1
        sheet.write(row, 0, idx)
        sheet.write(row, 1, city)
    wkb.save('test/city.xls')


if __name__ == '__main__':
    run()