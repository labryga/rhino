import rhinoscriptsyntax as rs
import math as mt
from random import (randint as ri, uniform as uf)
import random
from itertools import product, starmap


map(lambda x: rs.ObjectColor(
    x[0](listPoints2), x[1]), [
        (rs.AddPolyline, (222,220,10)),
        (rs.AddCurve, (22,220,55)),
        (rs.AddInterpCurve, (0,100,50))
    ])

map(rs.AddPoint, listPoints2)

map(lambda x: rs.AddPoint(x*mt.cos(x), x*mt.sin(x), 0), 
        [x for x in rs.frange(0.0, 70.0, 0.2)])



rs.AddCurve(
        [ ((i*mt.cos(i)), (i*mt.sin(i)), i) 
            for i in rs.frange(0.0, 70.0, 0.2)]
        )

rs.AddCurve(
        [ tuple( map(lambda x: ri(-100,100), range(3)) ) 
            for i in range(30) ])


for x, y, z in product( *[range(0,256,10) for i in range(3)] ):
    rs.ObjectColor(
            rs.AddPoint([x,y,z]), [x,y,z])

#
# for x, y in product(*[rs.frange(0.0, 10.0, 0.1) for i in range(2)]):
#     rs.AddPoint(x, y, (mt.sin(x) * mt.cos(y)) )
#
#
# starmap(lambda x,y,z,r,g,b: rs.ObjectColor(
#     rs.AddPoint(x,y,z), [r,g,b]),
#     [(ri(0,100),)*3 + (uf(0,255),)*3) for i in range(30)]))
#
#
map(lambda x: rs.AddPoint(x[0],x[1],x[2]),
        [tuple(map(lambda x: ri(0,100), range(3))) + tuple(map(lambda x: uf(0,255), \
                range(3))) for i in range(10000)])


tuple(starmap(lambda x,y,z,r,g,b: rs.ObjectColor(
    rs.AddPoint(x,y,z), [r,g,b]),

    [tuple( map(lambda x: ri(0,100), range(3)) ) + \
            tuple( map(lambda x: uf(0,255), range(3)) ) 
            for i in range(10000)]
    ))
