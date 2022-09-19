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
    nationalite = []
    first_serve_g = []
    first_serve_p = []
    for i in range(1, worksheet.nrows):
        nationalite.append(worksheet.cell(i, 10).value)
        if worksheet.cell(i, 29).value > 0:
            first_serve_g.append((worksheet.cell(i, 30).value/worksheet.cell(i, 29).value))#30 = AE
        if worksheet.cell(i, 36).value > 0:
            first_serve_p.append((worksheet.cell(i, 36).value/worksheet.cell(i, 36).value))#36 = AK
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
        nationalite.append(worksheet.cell(i, 10).value)

    print(statistics.mean(first_serve_p))

    

if __name__ == "__main__":
    main()