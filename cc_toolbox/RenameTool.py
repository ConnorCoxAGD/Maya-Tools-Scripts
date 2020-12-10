import maya.cmds as cmds

class RenameObjectTool:
    def __init__(self):
        self.rename_window = 'RenameWindow'

    def createWindow(self):
        # deletes window if it already is in use
        self.delete()

        self.rename_window = cmds.window(self.rename_window, title="Rename Window", widthHeight=(200, 200))

        self.col_layout = cmds.columnLayout(parent=self.rename_window, adjustableColumn=True)
        self.name_field = cmds.textField(parent=self.col_layout, placeholderText="Ex. Name_##_Geo")
        self.written_name = cmds.text(self.name_field, q=True, text=True)

        cmds.button(parent=self.col_layout, label='RenameTool', c=lambda *x: self.rename_selected())

        cmds.showWindow(self.rename_window)

    def delete(self):
        if cmds.window(self.rename_window, exists=True):
            cmds.deleteUI(self.rename_window)

    def rename_selected(self):
        selected = cmds.ls(sl=True)
        object_name = self.written_name
        print self.written_name
        padding_amount = object_name.count("#")

        current_number = 0

        for o in selected:
            current_number = current_number + 1
            txt = object_name.replace("#" * padding_amount, str(current_number).zfill(padding_amount))
            cmds.rename([o], txt)


rename_window = RenameObjectTool()
rename_window.createWindow()