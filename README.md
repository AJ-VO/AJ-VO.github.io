# AJ-VO.github.io
Tennis Vert &amp; Or
## Ligue Maison
Chaque joueur commence la ligue avec 1500 points. [référence : utils.py.def get_eloGain(matchDelta)](utils.py)
```
y = Points gagnés ou perdus
x = Points du gagnant - points du perdant
```
```
y = {
    = 180 si x < -500
    = -4/25x + 100 si -500 <= x <= 500
    = 20 si x > 500
}
```
Si une fille gagne contre un garçon
```
Points gagnés par la fille = y*2
```
Si un garçon gagne contre une fille
```
Points gagnés par le garçon = y/2
Points perdus par la fille = y/-2
```

# Analyse ATP_ALL
[ATP_ALL](ATP_ALL.xls) est un fichier contenant de l'information sur des matchs de tennis professionnel joués entre 2008 et 2017. *n = 27148*

### À quelle fréquence est-ce que le joueur moins bien classé gagne le match?
```
outcome = []#bool
for i in range(1, n):
    if Rang_G < Rang_P:
        outcome.append(True)
    else:
        outcome.append(False)
frequence = outcome.count(True)/n
```
> 33.06%