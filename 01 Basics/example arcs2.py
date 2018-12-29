def RecursiveGrowth( ptStart, vecDir, props, generation):
    minTwigCount, maxTwigCount, maxGenerations, maxTwigLength, lengthMutation, maxTwigAngle,...      
        angleMutation = props
    if generation>maxGenerations: return

    #Copy and mutate the growth-properties
    newProps = props
    maxTwigLength *= lengthMutation
    maxTwigAngle *= angleMutation
    if maxTwigAngle>90: maxTwigAngle=90

    #Determine the number of twigs (could be less than zero)
    newprops = minTwigCount, maxTwigCount, maxGenerations, maxTwigLength, lengthMutation,...
        maxTwigAngle, angleMutation
    maxN = int( minTwigCount+random.random()*(maxTwigCount-minTwigCount) )
    for n in range(1,maxN):
        ptGrow = RandomPointInCone(ptStart, vecDir, 0.25*maxTwigLength, maxTwigLength,...
            maxTwigAngle)
        newTwig = AddArcDir(ptStart, ptGrow, vecDir)
        if newTwig:
            vecGrow = rs.CurveTangent(newTwig, rs.CurveDomain(newTwig)[1])
            RecursiveGrowth(ptGrow, vecGrow, newProps, generation+1)
