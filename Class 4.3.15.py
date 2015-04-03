#Two ways to makes loops:
#for x in Pts:
#    x
#OR

#for i in range (0,Len(pts))
#    pts[i]

import rhinoscriptsyntax as rs


def main ():
    objectIn = rs.GetObject("select a point", 1)
    object = rs.coerce3dpoint(objectIn)
    print str(object.X) + "," + str(object.Y) + "," + str(object.Z)

    curveIn = rs.GetObject("select a curve", 4)
    curve = rs.coercecurve(curveIn)
    #print "curve with" + str(curve.PointCount-1) + "points"

    boundingBox = curve.GetBoundingBox(True)
    center = boundingBox.Center
    #print "center of curve at" + str(object.X) + "," + str(object.Y) + "," + str(object.Z)

    rs.AddPoint(center)

    newCurves = rs.ExplodeCurves(curveIn)

    for curve in newCurves:
        pts = []
        pts.append(rs.CurveStartPoint(curve))
        pts.append(rs.CurveEndPoint(curve))
        pts.append(center)
        pts.append(rs.CurveStartPoint(curve))
        triangleCurve = rs.AddCurve(pts,1)
        surface = rs.AddPlanarSrf(triangleCurve)

        roundCurve = rs.AddCurve(pts,3)
        rs.SplitSurface




if __name__=="__main__":
    main()
