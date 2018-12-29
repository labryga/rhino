import rhinoscriptsyntax as rs
import math as mt
import random
from random import (randint as ri, uniform as uf)
from itertools import product, starmap


tuple(starmap( lambda k, r, c: rs.ObjectColor(
    rs.AddCircle(k, r,), c),
    [ ( (0 + i, ri(2,20), 0), 
        ri(2,10), 
        tuple(map(lambda x: ri(0,255), range(3)))) 
        for i in range(0,200,10) ]))


