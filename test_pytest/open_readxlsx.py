import xlrd


def read_xlsx():
    xlsx=list()
    book=xlrd.open_workbook('login01.xls')
    sheet=book.sheet_by_index(0)
    for line in range(1,sheet.nrows):
        # print(sheet.row_values(line))
        xlsx.append(sheet.row_values(line))
    # print(xlsx)
    # print([0][])
    return xlsx

if __name__=='__main__':
    read_xlsx()