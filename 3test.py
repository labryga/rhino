import rhinoscriptsyntax as r
import math as m


p01 = [(m.cos(i), m.sin(i), m.cos(m.sin((i)) * 1.57))
        for i in r.frange(0.00, 12.560, 0.0785)] 

p02 = [(m.cos(i), m.sin(i), m.sin((i)))
        for i in r.frange(0.00, 6.280, 0.157)] 

r.AddInterpCurve(p01)
map(r.AddPoints, p01)
