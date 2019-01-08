import rhinoscriptsyntax as r
from rhinoscriptsyntax import frange
from math import sin, cos, pi

p4 = [(sin(x)*((e**2)/1200), cos(x)*((e**2)/1200), (e/35)**2) for e, x in enumerate(frange(0.0, 8*pi, (2*pi)/50))] 
# map(r.AddPoints, p4)
r.AddCurve(p4)
