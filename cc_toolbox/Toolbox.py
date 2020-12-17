import maya.cmds as cmds


class ToolboxUI:
    def __init__(self):
        self.toolbox_window = 'ccToolWindow'
        self.rename_window = 'ccRename'

    def createWindow(self):
        # deletes window if it already is in use
        self.delete()

        self.toolbox_window = cmds.window(self.toolbox_window, title="Toolbox", widthHeight=(200, 200))
        self.col_layout = cmds.columnLayout(parent=self.toolbox_window, adjustableColumn=True)
        self.rig_layout = cmds.columnLayout(parent=self.toolbox_window, adjustableColumn=True)

        cmds.button(parent=self.col_layout, label='RenameTool', c=lambda *x: self.call_renameUI())
        cmds.button(parent=self.col_layout, label='Random Distributor', c=lambda *x: self.call_random_generatorUI())
        cmds.button(parent=self.col_layout, label='Delete history', c=lambda *x: self.delete_history())
        cmds.button(parent=self.col_layout, label='Freeze Transformations', c=lambda *x: self.freeze_transforms())

        cmds.button(parent=self.rig_layout, label='Create Parent Groups', c=lambda *x: self.create_parent_group())
        cmds.button(parent=self.rig_layout, label='Apply Constraints', c=lambda *x: self.apply_constraints())

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

    def freeze_transforms(self):
        cmds.makeIdentity(apply=True)

    def delete_history(self):
        cmds.delete(ch=True)

    def create_parent_group(self):
        selection_list=cmds.ls(sl=True)

        for i in selection_list:
            new_group = cmds.group(i, n=i+"_Grp", r=True)
            cmds.matchTransform(new_group, i)

    def apply_constraints(self):
        selected_objects=cmds.ls(sl=True)
        selection_count = len(selected_objects)

        for i in range(0, selection_count, 2):
            cmds.parentConstraint(selected_objects[i+1], selected_objects[i], mo=True)
            cmds.scaleConstraint(selected_objects[i + 1], selected_objects[i], mo=True)