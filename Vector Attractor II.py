#WHAT IS RANDOM??
#Example of how to randomize variables

import rhinoscriptsyntax as rs
import random

point = rs.GetPoint()

for i in range(0,10):

    a = random.randint (0,10)
    b = random.randint (0,10)
    c = 0

    StartPoint = (a,b,c)
    NewVecEnd = (point)
    NewVecStart = (0,0,0)
    origin = StartPoint

    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    color = [r,g,b]

    vector = rs.VectorCreate(NewVecEnd, NewVecStart)
    line = rs.AddLine(StartPoint, NewVecEnd)
    line = rs.ScaleObject(line, origin, (0.5,0.5,0.5))

    rs.ObjectColor (line, color)
    segments = rs.DivideCurve(line,9)
    rs.AddLine(StartPoint, segments[1])

    rs.ObjectColor (segments, color)

print (segments[0])
