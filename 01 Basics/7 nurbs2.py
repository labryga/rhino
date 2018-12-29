def addcurvaturegraphsection(idCrv, t0, t1, samples, scale):
    if (t1-t0)<=0.0: return
    tstep = (t1-t0)/samples
    points = []
    objects = []
    for t in rs.frange(t0,t1+(0.5*tstep),tstep):
        if t>=t1:t = t1-1e-10
        cData = rs.CurveCurvature(idCrv, t)
        if not cData:
            points.append(rs.EvaluateCurve(idCrv, t))
        else:
            c = rs.VectorScale(cData[4], scale)
            a = cData[0]
            b = rs.VectorSubtract(a, c)
            objects.append(rs.AddLine(a,b))
            points.append(b)

    objects.append(rs.AddInterpCurve(points))
    return objects
