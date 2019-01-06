import rhinoscriptsyntax as r
from math import sin, cos


map(lambda x: r.ObjectColor(
    r.AddPoints(x), [128,255,128] ),
    [(sin(x/4), cos(x/4), sin(x)*0.5) for x in r.frange(0.0, 25.12, 0.157)] )

map(lambda x: r.ObjectColor(
    r.AddPoints(x), [0,0,255] ),
    [(sin(x/8), cos(x/8), sin(x)) for x in r.frange(0.0, 50.24, 0.157)] )
