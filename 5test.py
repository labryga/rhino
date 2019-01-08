import rhinoscriptsyntax as r
from rhinoscriptsyntax import frange
from math import sin, cos, pi

p4 = [(sin(x)*((e**2)/1200), cos(x)*((e**2)/1200), (e/35)**2) for e, x in enumerate(frange(0.0, 8*pi, (2*pi)/50))] 
# map(r.AddPoints, p4)
r.AddCurve(p4)


# p1 = [(sin(i)*2, cos(i)*2, 0) for i in frange(0.0, 6.28, 0.157)]
#
#
# p2 = [(sin(i) * (x**2/8), cos(i) * (x**2/8), x/4)
#         for i in frange(0.0, (2*pi), (2*pi/12))
#         for x in range(10)]
#
#
# for i in range(10):
#     for v, a in enumerate(frange(0.0, pi*2, 0.0785)):
#         r.ObjectColor(
#             r.AddPoint(sin(a)*(i**2), cos(a)*(i**2), i/5),
#                         [(255/80)*v/2, (25.5)*i, (255/80)*v/3])
