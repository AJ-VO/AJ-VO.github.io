from utils import *

def main():

    print()

    #open excel file
    workbook = xlrd.open_workbook('ATP_ALL.xls')
    worksheet = workbook.sheet_by_name('Sheet1')
    #(worksheet.cell(i, 12).value

    #Rank Difference
    l_won = []#bool
    diff = []#int
    temps_de_jeu_g = []#String
    temps_de_jeu_p = []
    for i in range(1, worksheet.nrows):
        try:
            if int(worksheet.cell(i, 12).value) > int(worksheet.cell(i, 21).value):
                l_won.append(True)
                diff.append(int(worksheet.cell(i, 12).value)-int(worksheet.cell(i, 21).value))
                temps_de_jeu_g.append(int(worksheet.cell(i, 26).value))
            else:
                l_won.append(False)
                temps_de_jeu_p.append(int(worksheet.cell(i, 26).value))
        except:
            continue

    print(l_won.count(True)/len(l_won))
    print(statistics.mean(temps_de_jeu_g))
    print(statistics.mean(temps_de_jeu_p))

if __name__ == "__main__":
    main()