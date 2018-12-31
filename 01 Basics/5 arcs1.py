def createArcDirection(ptStart, ptEnd, vecDir):
    vecBase = rs.PointSubtract(ptEnd, ptStart)
    if rs.VectorLength(vecBase)==0.0: return

    if rs.IsVectorParallelTo(vecBase, vecDir): return

    vectorBase = rs.VectorUnitize(vecBase)
    vectorDirection = rs.VectorUnitize(vecDir)

    vecBisector = rs.VectorAdd(vecDir, vecBase)
    vecBisector = rs.VectorUnitize(vecBisector)

    dotProd = rs.VectorDotProduct(vecBisector, vecDir)
    midLength = (0.5*rs.Distance(ptStart, ptEnd))/dotProd

    vecBisector = rs.VectorScale(vecBisector, midLength)
    return rs.AddArc3Pt(ptStart, rs.PointAdd(ptStart, vecBisector), ptEnd)
