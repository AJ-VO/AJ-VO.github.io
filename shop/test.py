from utilities import *

s_1 = 'Mohan Mehta'
s_2 = 'Mohan Meh'
print(SequenceMatcher(a=s_1,b=s_2).ratio())


