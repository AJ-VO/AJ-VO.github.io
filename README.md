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