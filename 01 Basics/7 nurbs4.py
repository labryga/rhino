import rhinoscriptsyntax as rs
import sys
import math

def ProximityAnalysis():
    mesh_id = rs.GetObject("Mesh for proximity analysis", 32, True, True)
    if not mesh_id: return

    brep_id = rs.GetObject("Surface for proximity test", 8+16, False, True)
    if not brep_id: return

    vertices = rs.MeshVertices(mesh_id)
    faces = rs.MeshFaceVertices(mesh_id)
    listD = VertexValueArray(vertices, brep_id)

    minD = sys.float_info.min
    maxD = sys.float_info.max
    for ct in range(len(listD)):
        if minD>listD[ct]: minD = listD[ct]
        if maxD<listD[ct]: maxD = listD[ct]

    colors = []
    for i in range(len(vertices)):
        proxFactor = (listD[i]-minD)/(maxD-minD)
        colors.append((255, 255*proxFactor, 255*proxFactor))
    rs.AddMesh(vertices, faces, vertex_colors=colors)
    rs.DeleteObject(mesh_id)
