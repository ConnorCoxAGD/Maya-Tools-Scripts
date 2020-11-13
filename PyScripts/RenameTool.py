import maya.cmds as cmds


def rename_tool(object_name):
    selected = cmds.ls(sl=True)

    padding_amount = object_name.count("#")

    current_number = 0

    for o in selected:
        current_number = current_number + 1
        txt = object_name.replace("#" * padding_amount, str(current_number).zfill(padding_amount))
        cmds.rename([o], txt)


rename_tool("R_Arm_##_Geo")
