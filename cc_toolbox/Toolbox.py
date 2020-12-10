import maya.cmds as cmds


class ToolboxUI:
    def __init__(self):
        self.toolbox_window = 'ccToolWindow'
        self.rename_window = 'ccRename'

    def createWindow(self):
        # deletes window if it already is in use
        self.delete()

        self.toolbox_window = cmds.window(self.toolbox_window,
                                         title="Toolbox",
                                         widthHeight=(200, 200))

        self.col_layout = cmds.columnLayout(parent=self.toolbox_window,
                                            adjustableColumn=True)

        cmds.button(parent=self.col_layout, label='RenameTool', c=lambda *x: self.call_renameUI())
        cmds.button(parent=self.col_layout, label='Random Distributor', c=lambda *x: self.call_random_generatorUI())

        cmds.showWindow(self.toolbox_window)

    def delete(self):
        if cmds.window(self.toolbox_window, exists=True):
            cmds.deleteUI(self.toolbox_window)

    def call_renameUI(self):
        import RenameTool
        reload(RenameTool)
        RenameTool.RenameObjectTool.createWindow()

    def call_random_generatorUI(self):
        import RandomGeneration
        reload(RandomGeneration)

    def call_makePlanarUI(self):
        import FixNonPlanarGeo
        pass
