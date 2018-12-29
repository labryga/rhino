def FitSurface(idSrf, Samples, dTranslation, dProximity):
    P = rs.SurfacePoints(idSrf)
    G = rs.SurfaceEditPoints(idSrf, True, True)
    N = GrevilleNormals(idSrf)
    S = ConvertToUVW(idSrf, Samples)
    [Forces, Factors] = InstantiateForceLists(len(P))

    dProximity = 0.0
    dTranslation = 0.0

    for i in range(len(S)):
        dProximity = dProximity + abs(S[i][2])
        for j in range(len(P)):
            LocalDist = math.pow((S[i][0] - G[j][0]),2) +  math.pow((S[i][1] - G[j][1]),2)
            if (LocalDist < 0.01): LocalDist = 0.01
            LocalFactor = 1 / LocalDist
            LocalForce = rs.VectorScale(N[j], LocalFactor * S[i][2])
            Forces[j] = rs.VectorAdd(Forces[j], LocalForce)
            Factors[j] = Factors[j] + LocalFactor
    Forces = DivideVectorList(Forces, Factors)

    for i in range(len(P)):
        P[i] = rs.PointAdd(P[i], Forces[i])
        dTranslation = dTranslation + rs.VectorLength(Forces[i])

    srf_N = rs.SurfacePointCount(idSrf)
    srf_K = rs.SurfaceKnots(idSrf)
    srf_W = rs.SurfaceWeights(idSrf)
    srf_D = []
    srf_D.append(rs.SurfaceDegree(idSrf, 0))
    srf_D.append(rs.SurfaceDegree(idSrf, 1))

    FS = rs.AddNurbsSurface(srf_N, P, srf_K[0], srf_K[1], srf_D, srf_W)
    return (FS, Samples, dTranslation, dProximity)
