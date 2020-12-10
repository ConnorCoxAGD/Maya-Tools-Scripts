import maya.cmds as cmds
import random

class RandomGenPlacement:
    def __init__(self):
        self.rand_gen_window = 'RandomGenerator'


    def createWindow(self):
        # deletes window if it already is in use
        self.delete()

        self.rand_gen_window = cmds.window(self.rand_gen_window, title="Random Distributor", widthHeight=(200, 300))
        self.column_layout = cmds.columnLayout(parent=self.rand_gen_window, adjustableColumn=True, rowSpacing=10, columnWidth=250)
        self.grid_layout = cmds.gridLayout(parent=self.rand_gen_window, numberOfColumns=4, cellWidthHeight=(75, 50))

        cmds.text(label="Amount of Duplicates", parent=self.column_layout)
        self.amount = cmds.intSliderGrp(parent=self.column_layout, minValue=0, maxValue=50)

        cmds.text(label="Min X", parent=self.grid_layout)
        self.minX = cmds.intField(parent=self.grid_layout)
        cmds.text(label="Max X", parent=self.grid_layout)
        self.maxX = cmds.intField(parent=self.grid_layout)
        cmds.text(label="Min Y", parent=self.grid_layout)
        self.minY = cmds.intField(parent=self.grid_layout)
        cmds.text(label="Max Y", parent=self.grid_layout)
        self.maxY = cmds.intField(parent=self.grid_layout)
        cmds.text(label="Min Z", parent=self.grid_layout)
        self.minZ = cmds.intField(parent=self.grid_layout)
        cmds.text(label="Max Z", parent=self.grid_layout)
        self.maxZ = cmds.intField(parent=self.grid_layout)

        cmds.text(label="Min Rotate X", parent=self.grid_layout)
        self.minRotX = cmds.intField(parent=self.grid_layout)
        cmds.text(label="Max Rotate X", parent=self.grid_layout)
        self.maxRotX = cmds.intField(parent=self.grid_layout)
        cmds.text(label="Min Rotate Y", parent=self.grid_layout)
        self.minRotY = cmds.intField(parent=self.grid_layout)
        cmds.text(label="Max Rotate Y", parent=self.grid_layout)
        self.maxRotY = cmds.intField(parent=self.grid_layout)
        cmds.text(label="Min Rotate Z", parent=self.grid_layout)
        self.minRotZ = cmds.intField(parent=self.grid_layout)
        cmds.text(label="Max Rotate Z", parent=self.grid_layout)
        self.maxRotZ = cmds.intField(parent=self.grid_layout)

        cmds.button(parent=self.column_layout, label='Generate and Place', c=lambda *x: self.RandomGen())

        cmds.showWindow(self.rand_gen_window)

    def delete(self):
        if cmds.window(self.rand_gen_window, exists=True):
            cmds.deleteUI(self.rand_gen_window)


    def RandomGen(self):
        obj = cmds.ls(sl=True)

        amount = cmds.intSliderGrp(self.amount, q=True, value=True)
        minX = cmds.intField(self.minX, q=True, value=True)
        maxX = cmds.intField(self.maxX, q=True, value=True)
        minY = cmds.intField(self.minY, q=True, value=True)
        maxY = cmds.intField(self.maxY, q=True, value=True)
        minZ = cmds.intField(self.maxZ, q=True, value=True)
        maxZ = cmds.intField(self.maxZ, q=True, value=True)

        minRotX = cmds.intField(self.minRotX, q=True, value=True)
        maxRotX = cmds.intField(self.maxRotX, q=True, value=True)
        minRotY = cmds.intField(self.minRotY, q=True, value=True)
        maxRotY = cmds.intField(self.maxRotY, q=True, value=True)
        minRotZ = cmds.intField(self.maxRotZ, q=True, value=True)
        maxRotZ = cmds.intField(self.maxRotZ, q=True, value=True)


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


rand_gen_window = RandomGenPlacement()
rand_gen_window.createWindow()



