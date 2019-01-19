import rhinoscriptsyntax as r
from math import sin, cos


ptOrigin = r.GetPoint("plane origin")
ptX = r.GetPoint("point X", ptOrigin)
ptY = r.GetPoint("point y", ptOrigin)

dX = r.Distance(ptOrigin, ptX)
dY = r.Distance(ptOrigin, ptY)
arrPlane = r.PlaneFromPoints(ptOrigin, ptX, ptY)

r.AddPlaneSurface(arrPlane, dX, dY)
