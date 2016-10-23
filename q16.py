import xlwt
import json



def run():
    with open('test/numbers.txt') as fp:
        numbers_list = json.load(fp)
    wkb = xlwt.Workbook()
    sheet = wkb.add_sheet('sheet 1')
    for row, numbers in enumerate(numbers_list):
        for col, number in enumerate(numbers):
            sheet.write(row, col, number)
    wkb.save('test/numbers.xls')


if __name__ == '__main__':
    run()