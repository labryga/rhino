import rhinoscriptsyntax as r
from rhinoscriptsyntax import frange as fr
from math import sin, cos, pi


# map(r.AddPoints,
#         [(x, 0.05*(x**3)+(x**2)+3, 0) for x in fr(-22,9, 0.5)])

p01 = [(x, (x**3)+5*(x**2), x**2) for x in fr(-8,4, 0.5)]
r.ObjectColor(r.AddInterpCurve(p01), [255, 0, 0])

p02 = [(x, 5*(x**2), x**2) for x in fr(-8,4, 0.5)]
r.ObjectColor(r.AddInterpCurve(p02), [0,0,255])
