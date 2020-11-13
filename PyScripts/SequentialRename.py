import maya.cmds as cmds


def RenameInOrder(side, part, padding_amount, node_type):
    selected = cmds.ls(sl=True)
    if side == "Left" or "L" or "left" or "l":
        side = "L_"
    if side == "Right" or "R" or "right" or "r":
        side = "R_"
    part = part + "_"
    if node_type == "joint" or "Joint" or "jnt" or "Jnt":
        node_type = "_Jnt"
    if node_type == "geo" or "Geo" or "geometry" or "Geometry":
        node_type == "_Geo"

    current_number = 0

    for o in selected:
        current_number = current_number + 1
        txt = str(current_number)
        cmds.rename([o], side + part + txt.zfill(padding_amount) + node_type)


RenameInOrder("left", "Leg", 2, "geo")
