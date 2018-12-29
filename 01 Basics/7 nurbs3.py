def createcurvaturegraph():
    curve_ids = rs.GetObjects("Curves for curvature graph", 4, False, True, True)
    if not curve_ids: return

    samples = 10
    scale = 1.0

    preview = []
    while True:
        rs.EnableRedraw(False)
        for p in preview: rs.DeleteObjects(p)
        preview = []
        for id in curve_ids:
            cg = addcurvaturegraph(id, samples, scale)
            preview.append(cg)
        rs.EnableRedraw(True)

        result = rs.GetString("Curvature settings", "Accept", ("Samples", "Scale", "Accept"))
        if not result:
            for p in preview: rs.DeleteObjects(p)
            break
        result = result.upper()
        if result=="ACCEPT": break
        elif result=="SAMPLES":
            numsamples = rs.GetInteger("Number of samples per knot-span", samples, 3, 100)
            if numsamples: samples = numsamples
        elif result=="SCALE":
            sc = rs.GetReal("Scale of the graph", scale, 0.01, 1000.0)
            if sc: scale = sc
