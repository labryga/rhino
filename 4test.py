import rhinoscriptsyntax as r
from math import sin, cos


# map(lambda x: r.ObjectColor(
#     r.AddPoints(x), [128,128,255] ),
#     [(x, cos(sin(x) * 1.57), 0) for x in r.frange(0.0, 6.28, 0.157)] )

map(lambda x: r.ObjectColor(
    r.AddPoints(x), [128,255,128] ),
    [(sin(x/4), cos(x/4), sin(x)*0.5) for x in r.frange(0.0, 25.12, 0.157)] )

map(lambda x: r.ObjectColor(
    r.AddPoints(x), [0,255,255] ),
    [(sin(x/8), cos(x/8), sin(x)*0.5) for x in r.frange(0.0, 50.24, 0.157)] )


p02 = [(sin(x/8), cos(x/8), sin(x)*0.5) for x in r.frange(0.0, 50.24, 0.157)]
r.AddInterpCurve(p02)

# map(lambda x: r.ObjectColor(
#     r.AddPoints(x), [255,128,128] ),
#     [(sin(x), cos(x), cos(sin(x))) for x in r.frange(0.0, 6.28, 0.157)] )
