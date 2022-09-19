from utils import *

def main():

    print()

    #open excel file
    workbook = xlrd.open_workbook('ATP_ALL.xls')
    worksheet = workbook.sheet_by_name('Sheet1')

    #Rank Difference
    l_won = []#bool
    for i in range(1, worksheet.nrows):
        try:
            if int(worksheet.cell(i, 12).value) > int(worksheet.cell(i, 21).value):
                l_won.append(True)
            else:
                l_won.append(False)
        except:
            continue

    print(l_won.count(True)/len(l_won))

if __name__ == "__main__":
    main()