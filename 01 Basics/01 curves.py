import rhinoscriptsyntax as rs
import math as mt
import random
from random import (randint as ri, uniform as uf)
from itertools import product, starmap


map(lambda x: (rs.AddCurve(x), rs.AddPolyline(x)), 
        [( 
            ( (0+i)+ri(-5,5) , ri(0,70), i), 
            (0+i, 0, 0),
            ( (0+i)+ri(-5,5), ri(-70,0), i*2) ) 
            for i in range(0,400,5)] )

