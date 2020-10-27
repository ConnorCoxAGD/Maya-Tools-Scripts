import maya.cmds as cmds

if not cmds.commandPort(':4434', query=True):
    cmds.commandPort(name=':4434')

cmds.polySphere(sx=15, sy=15, r=1.5)
cmds.move(0, 1.5, 0)
cmds.polySphere(sx=15, sy=15, r=1.2)
cmds.move(0, 3.5, 0)
cmds.polySphere(sx=15, sy=15, r=.8)
cmds.move(0, 5.2, 0)
button=cmds.polySphere(sx=6, sy=6, r=.1)
cmds.move(0,3,1.1)
button2=cmds.duplicate(button, rr=True)
cmds.select(button2)
cmds.move(0, .6, .1, r=True)
cmds.duplicate(button2, rr=True)
cmds.move(0, .53, -.2, r=True)
cmds.polyCylinder(r=.6, h=1.5)
cmds.select("hat")
cmds.move(y=6)