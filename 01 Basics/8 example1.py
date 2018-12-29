import rhinoscriptsyntax as rs

def main():
    curve_id = rs.GetObject("Select a curve to sample", 4, True, True)
    if not curve_id: return

    rs.EnableRedraw(False)
    t = 0
    while t<=1.0:
        addpointat_r1_parameter(curve_id,t)
        t+=0.01
    rs.EnableRedraw(True)

def addpointat_r1_parameter(curve_id, parameter):
    domain = rs.CurveDomain(curve_id)


    r1_param = domain[0] + parameter*(domain[1]-domain[0])
    r3point = rs.EvaluateCurve(curve_id, r1_param)
    if r3point:
        point_id = rs.AddPoint(r3point)
        rs.ObjectColor(point_id, parametercolor(parameter))

def parametercolor(parameter):
    red = 255 * parameter
    if red<0: red=0
    if red>255: red=255
    return (red,0,255-red)

def vain():
    surface_id = rs.GetObject("Select a surface to sample", 8, True)
    if not surface_id: return

    curve_id = rs.GetObject("Select a curve to measure", 4, True, True)
    if not curve_id: return

    points = rs.DivideCurve(curve_id, 500)
    rs.EnableRedraw(False)
    for point in points: evaluatedeviation(surface_id, 1.0, point)
    rs.EnableRedraw(True)

def evaluatedeviation( surface_id, threshold, sample ):
    r2point = rs.SurfaceClosestPoint(surface_id, sample)
    if not r2point: return

    r3point = rs.EvaluateSurface(surface_id, r2point[0], r2point[1])
    if not r3point: return

    deviation = rs.Distance(r3point, sample)
    if deviation<=threshold: return

    rs.AddPoint(sample)
    rs.AddLine(sample, r3point)

if __name__=="__main__":
    main()
    vain()
