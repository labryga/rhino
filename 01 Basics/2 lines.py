import rhinoscriptsyntax as rs
import math as mt
import random
from random import (randint as ri, uniform as uf)
from itertools import product, starmap


map(lambda x: rs.AddLine(x[0], x[1]), 
        [ ( (0+i, ri(0,20), 0), (0+i, ri(-20,0), 0) ) 
            for i in range(0,400,5)])
