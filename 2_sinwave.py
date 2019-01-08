import rhinoscriptsyntax as r
from rhinoscriptsyntax import frange as fr
from math import sin, cos, pi


# map(r.AddPoints,
#         [(x, 0.05*(x**3)+(x**2)+3, 0) for x in fr(-22,9, 0.5)])

p01 = [(x, 0.05*(x**3)+(x**2)+3, 0) for x in fr(-22,9, 0.5)]
r.ObjectColor(r.AddInterpCurve(p01), [255, 255, 0])

p02 = [(x, x**2, 0) for x in fr(-22,9, 0.5)]
r.ObjectColor(r.AddInterpCurve(p02), [0,255,255])
