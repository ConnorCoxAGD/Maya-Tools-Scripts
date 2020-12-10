import maya.cmds as cmds
import random

class RandomGenPlacement:
    def __init__(self):
        self.rand_gen_window = 'RandomGenerator'

    def createWindow(self):
        # deletes window if it already is in use
        self.delete()

        self.rand_gen_window = cmds.window(self.rand_gen_window,
                                         title="Random Distributor",
                                         widthHeight=(200, 200))

        self.col_layout = cmds.columnLayout(parent=self.rand_gen_window,
                                            adjustableColumn=True)
        self.name_field = cmds.textField(parent=self.col_layout,
                                            placeholderText="New name...")
        self.size_slider = cmds.intSliderGrp(parent=self.col_layout,
                                             minValue=0,
                                             maxValue=25)

        cmds.button(parent=self.col_layout, label='Generate and Place', c=lambda *x: self.RandomGen())

        cmds.showWindow(self.rand_gen_window)

    def delete(self):
        if cmds.window(self.rand_gen_window, exists=True):
            cmds.deleteUI(self.rand_gen_window)


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

#RandomGen(10, -10, 10, -10, 10, -10, 10, 0, 360, 0, 360, 0, 360)

