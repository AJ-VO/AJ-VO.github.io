from utils import *

def main():

    print()

    #open excel file
    workbook = xlrd.open_workbook('ATP_ALL.xls')
    worksheet = workbook.sheet_by_name('Sheet1')
    print("ATP_ALL.xls openend")
    #(worksheet.cell(i, 12).value

    #Rank Difference
    l_won = []#bool
    diff = []#int
    temps_de_jeu_g = []#String
    temps_de_jeu_p = []
    nationalite = []
    first_serve_g = []
    first_serve_p = []
    fserve_u = []
    for i in range(1, worksheet.nrows):
        nationalite.append(worksheet.cell(i, 10).value)
        if worksheet.cell(i, 29).value > 0:
            first_serve_g.append((worksheet.cell(i, 30).value/worksheet.cell(i, 29).value))#30 = AE
        if worksheet.cell(i, 35).value > 0:
            first_serve_p.append((worksheet.cell(i, 36).value/worksheet.cell(i, 35).value))#36 = AK
        try:
            if int(worksheet.cell(i, 12).value) > int(worksheet.cell(i, 21).value):
                l_won.append(True)
                diff.append(int(worksheet.cell(i, 12).value)-int(worksheet.cell(i, 21).value))
                temps_de_jeu_g.append(int(worksheet.cell(i, 26).value))
                fserve_u.append((worksheet.cell(i, 30).value/worksheet.cell(i, 29).value))
            else:
                l_won.append(False)
                temps_de_jeu_p.append(int(worksheet.cell(i, 26).value))
        except:
            continue
        nationalite.append(worksheet.cell(i, 10).value)

    analysisData = {}
    analysisData["moins_bien_classe_gagne"] = {}
    analysisData["moins_bien_classe_gagne"]["description"] = "Lorsque le joueur moins bien classé gagne le match"
    analysisData["moins_bien_classe_gagne"]["frequence"] = l_won.count(True)/(l_won.count(True)+l_won.count(False))
    analysisData["moins_bien_classe_gagne"]["moyenne"] = statistics.mean(diff)
    analysisData["moins_bien_classe_gagne"]["mediane"] = statistics.median(diff)
    analysisData["moins_bien_classe_gagne"]["max"] = max(diff)
    analysisData["moins_bien_classe_gagne"]["first_serve_avg"] = statistics.mean(fserve_u)
    analysisData["first_serve_avg_w"] = statistics.mean(first_serve_g)
    analysisData["first_serve_avg_l"] = statistics.mean(first_serve_p)

    with open("jsons/analysis.json", "w") as f:
        json.dump(analysisData, f, indent = 4)
        print("Dumped")

    

if __name__ == "__main__":
    main()