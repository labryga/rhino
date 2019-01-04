import math as m
import rhinoscriptsyntax as rs


def getCoordinates(v):
    x = 10 * round(m.cos(m.radians(v)), 2)
    y = 10 * round(m.sin(m.radians(v)), 2)
    z = v * 0.1
    return (x, y, z)

map(rs.AddPoints, [getCoordinates(i) for i in range(0,360,10)]);
