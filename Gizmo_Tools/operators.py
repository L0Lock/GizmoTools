import bpy
from bpy.types import Operator

# -----------------------------------------------------------------------------
#    Operator : Decrease size
# -----------------------------------------------------------------------------

class VIEW3D_OT_decease_gizmo_size(Operator):
    bl_idname = "view3d.decease_gizmo_size"
    bl_label = "Decrease Gizmo Size"

    def execute(self, context):

        prefs = context.preferences
        addon_prefs = prefs.addons[__package__].preferences
        view = prefs.view
        gs = view.gizmo_size
        print("Gizmo size =", gs)
        print("Increment =", addon_prefs.inc)

        gs -= int(addon_prefs.inc)
        view.gizmo_size = gs
        print("New Gizmo size =", gs)
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Increase size
# -----------------------------------------------------------------------------


class VIEW3D_OT_incease_gizmo_size(Operator):
    bl_idname = "view3d.incease_gizmo_size"
    bl_label = "Increase Gizmo Size"

    def execute(self, context):

        prefs = context.preferences
        addon_prefs = prefs.addons[__package__].preferences
        view = prefs.view
        gs = view.gizmo_size
        print("Gizmo size =", gs)
        print("Increment =", addon_prefs.inc)

        gs += int(addon_prefs.inc)
        view.gizmo_size = gs
        print("New Gizmo size =", gs)
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Move Local X
# -----------------------------------------------------------------------------


class VIEW3D_OT_move_local_x(Operator):
    bl_idname = "view3d.move_local_x"
    bl_label = "Move on the local X axis"
    bl_options = {"REGISTER","UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__package__].preferences
        ot = bpy.ops.transform.translate
        ot(value=(addon_prefs.tinc, 0, 0), orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Move Local nX
# -----------------------------------------------------------------------------


class VIEW3D_OT_move_local_nx(Operator):
    bl_idname = "view3d.move_local_nx"
    bl_label = "Move on the local -X axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__package__].preferences
        ot = bpy.ops.transform.translate
        ot(value=(addon_prefs.tinc*-1, 0, 0), orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Move Local Y
# -----------------------------------------------------------------------------


class VIEW3D_OT_move_local_y(Operator):
    bl_idname = "view3d.move_local_y"
    bl_label = "Move on the local Y axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__package__].preferences
        ot = bpy.ops.transform.translate
        ot(value=(0, addon_prefs.tinc, 0), orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Move Local nY
# -----------------------------------------------------------------------------


class VIEW3D_OT_move_local_ny(Operator):
    bl_idname = "view3d.move_local_ny"
    bl_label = "Move on the local -Y axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__package__].preferences
        ot = bpy.ops.transform.translate
        ot(value=(0, addon_prefs.tinc*-1, 0), orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Move Local Z
# -----------------------------------------------------------------------------


class VIEW3D_OT_move_local_z(Operator):
    bl_idname = "view3d.move_local_z"
    bl_label = "Move on the local Z axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__package__].preferences
        ot = bpy.ops.transform.translate
        ot(value=(0, 0, addon_prefs.tinc), orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Move Local nZ
# -----------------------------------------------------------------------------


class VIEW3D_OT_move_local_nz(Operator):
    bl_idname = "view3d.move_local_nz"
    bl_label = "Move on the local -Z axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__package__].preferences
        ot = bpy.ops.transform.translate
        ot(value=(0, 0, addon_prefs.tinc*-1), orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Rotate Local X
# -----------------------------------------------------------------------------


class VIEW3D_OT_rotate_local_x(Operator):
    bl_idname = "view3d.rotate_local_x"
    bl_label = "Rotate on the local X axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__package__].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc, orient_axis='X', orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Rotate Local nX
# -----------------------------------------------------------------------------


class VIEW3D_OT_rotate_local_nx(Operator):
    bl_idname = "view3d.rotate_local_nx"
    bl_label = "Rotate on the local -X axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__package__].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc*-1, orient_axis='X', orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Rotate Local Y
# -----------------------------------------------------------------------------


class VIEW3D_OT_rotate_local_y(Operator):
    bl_idname = "view3d.rotate_local_y"
    bl_label = "Rotate on the local Y axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__package__].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc, orient_axis='Y', orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Rotate Local nY
# -----------------------------------------------------------------------------


class VIEW3D_OT_rotate_local_ny(Operator):
    bl_idname = "view3d.rotate_local_ny"
    bl_label = "Rotate on the local -Y axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__package__].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc*-1, orient_axis='Y', orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Rotate Local Z
# -----------------------------------------------------------------------------


class VIEW3D_OT_rotate_local_z(Operator):
    bl_idname = "view3d.rotate_local_z"
    bl_label = "Rotate on the local Z axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__package__].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc, orient_axis='Z', orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Rotate Local nZ
# -----------------------------------------------------------------------------


class VIEW3D_OT_rotate_local_nz(Operator):
    bl_idname = "view3d.rotate_local_nz"
    bl_label = "Rotate on the local -Z axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__package__].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc*-1, orient_axis='Z', orient_type='LOCAL')
        return {'FINISHED'}