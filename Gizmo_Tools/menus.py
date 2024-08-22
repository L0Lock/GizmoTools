import bpy
from bpy.types import Menu

# -----------------------------------------------------------------------------
#    Gizmo Menu
# -----------------------------------------------------------------------------


class VIEW3D_MT_gizmo_size_menu(Menu):
    bl_label = "Gizmo"
    bl_idname = "VIEW3D_MT_gizmo_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("view3d.incease_gizmo_size", icon="ZOOM_IN")
        layout.operator("view3d.decease_gizmo_size", icon="ZOOM_OUT")


def draw_gizmo_menu(self, context):
    layout = self.layout
    layout.menu(VIEW3D_MT_gizmo_size_menu.bl_idname)