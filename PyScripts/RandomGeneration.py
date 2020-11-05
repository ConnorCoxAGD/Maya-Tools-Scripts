import maya.cmds as cmds
import random

def RandomGen(amount, minX, maxX, minY, maxY, minZ, maxZ, minRotX, maxRotX, minRotY, maxRotY, minRotZ, maxRotZ):
    obj = cmds.ls(sl=True)

    for each in range(amount):
        cmds.duplicate(obj)
        cmds.move(random.randint(minX, maxX),
                  random.randint(minY,maxY),
                  random.randint(minZ, maxZ),
                  obj, ws=True)
        cmds.rotate(random.randint(minRotX, maxRotX),
                  random.randint(minRotY,maxRotY),
                  random.randint(minRotZ, maxRotZ),
                  obj, ws=True)

    RandomGen(10, -10, 10, -10, 10, -10, 10, 0, 360, 0, 360, 0, 360)

