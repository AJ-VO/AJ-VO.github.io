# AJ-VO.github.io
Tennis Vert &amp; Or
## Ligue Maison
Chaque joueur commence la ligue avec 1500 points. [référence : utils.py.def get_eloGain(matchDelta)](utils.py)
```
y = Points gagnés ou perdus
x = Points du gagnant - points du perdant
y = {
    180 si x < -500
    -4/25x + 100 si -500 <= x <= 500
    20 si x > 500
}
```