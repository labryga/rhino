import rhinoscriptsyntax as r
from rhinoscriptsyntax import frange as fr
from math import sin, cos, pi
from random import randint as ri
from random import uniform as uf



plane = r.WorldXYPlane()
kwadrat = r.AddRectangle(plane, 1, 1)

p01 = [(x, y, uf(-2, 2)) for x in range(-20,20)
        for y in range(-20,20)]

p02 = product(*[range(6,10) for i in range(3)])

def ordering(coord):
    kwadrat_copy = r.CopyObject(kwadrat, coord)
    zentrum = (coord[0]+0.5, coord[1]+0.5, coord[2]) 
    r.RotateObject(kwadrat_copy, zentrum, uf(0,360))


map(ordering, p01)
