import math as m
from itertools import starmap as sm
import rhinoscriptsyntax as rs


def getCoordinates(v):
    x = v * round(m.cos(m.radians(v)), 2)
    y = v * round(m.sin(m.radians(v)), 2)
    z = v * 0.1
    return (x, y, z)

# map(rs.AddPoints, [getCoordinates(i) for i in range(0,360,10)]);
# map(rs.AddPoints, [(i * m.sin(i), i * m.cos(i), i) for i in rs.frange(-40,80, 0.5)]) 
# p01 = [(i * m.sin(i), i * m.cos(i), i) for i in rs.frange(-40,80, 0.5)] 

p01 = [(m.cos(i), m.sin(i), m.cos(m.sin(i)))
        for i in rs.frange(0.00, 6.280, 0.157)] 
rs.AddInterpCurve(p01)

# colors = [tuple(map(lambda x: i*1.275, range(3))) for i in range(0,200)]
# points = [(x * m.cos(x), x * m.sin(x), x * 0.5) for x in rs.frange(0.0, 20.0, 0.1)]
#
# values = [((x * m.cos(x), x * m.sin(x), x * 0.5),
#             (tuple(map(lambda e: int(x)*1.275, range(3))))) 
#             for x in rs.frange(0.0, 20.0, 0.1)]
#
# values = [((x * m.cos(x), x * m.sin(x), x * 0.5),
#             (list(map(lambda e: int(x)*1.275, range(3))))) 
#             for x in rs.frange(0.0, 20.0, 0.1)]
# # map(lambda k, c: rs.ObjectColor(rs.AddPoints(k), c), points, colors)
# tuple(sm(
#     lambda v, c: rs.ObjectColor(rs.AddPoints(v), c), values
#     ))
