import maya.cmds as cmds

if not cmds.commandPort(':4434', query=True):
    cmds.commandPort(name=':4434')
#body
cmds.polySphere(sx=15, sy=15, r=1.5)
cmds.move(0, 1.5, 0)
cmds.polySphere(sx=15, sy=15, r=1.2)
cmds.move(0, 3.5, 0)
cmds.polySphere(sx=15, sy=15, r=.8)
cmds.move(0, 5.2, 0)

#buttons
button = cmds.polySphere(sx=6, sy=6, r=.1)
cmds.move(0,3,1.1)
button2 = cmds.duplicate(button, rr=True)
cmds.select(button2)
cmds.move(0, .6, .1, r=True)
cmds.duplicate(button2, rr=True)
cmds.move(0, .53, -.2, r=True)

eye = cmds.polySphere(sx=8, sy=8, r=.15)
cmds.move(-.25, 5.4, .7)
cmds.polyMirrorFace(axis=0, cutMesh=0, mergeMode=3,)



#cmds.polyCylinder(r=.6, h=1.5)
