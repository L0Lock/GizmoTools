# SPDX-License-Identifier: GPL-3.0-or-later

from .menus import *
from .operators import *
from .preferences import *
# from .utils import *
import rna_keymap_ui
import bpy

bl_info = {
    "name": "Gizmo Tools",
    "description": "Allows you to do simple gizmo operations using keyboard shortcuts.",
    "author": "Loïc \"Lauloque\" Dautry",
    "version": (0, 1, 3),
    "blender": (4, 2, 0),
    "location": "View3D/UV Editor → Header → View → Gizmo",
    "warning": "Under development.",
    "wiki_url": "https://github.com/L0Lock/GizmoTools",
    "tracker_url": "https://github.com/L0Lock/GizmoTools/issues",
    "category": "Interface"
}

# -----------------------------------------------------------------------------
#    Keymap
# -----------------------------------------------------------------------------
addon_keymaps = []

# -----------------------------------------------------------------------------
#    Register
# -----------------------------------------------------------------------------

classes = (
    VIEW3D_PT_gizmo_size_preferences,
    VIEW3D_OT_incease_gizmo_size,
    VIEW3D_OT_decease_gizmo_size,
    VIEW3D_MT_gizmo_size_menu,
    VIEW3D_OT_move_local_x,
    VIEW3D_OT_move_local_nx,
    VIEW3D_OT_move_local_y,
    VIEW3D_OT_move_local_ny,
    VIEW3D_OT_move_local_z,
    VIEW3D_OT_move_local_nz,
    VIEW3D_OT_rotate_local_x,
    VIEW3D_OT_rotate_local_nx,
    VIEW3D_OT_rotate_local_y,
    VIEW3D_OT_rotate_local_ny,
    VIEW3D_OT_rotate_local_z,
    VIEW3D_OT_rotate_local_nz,

)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.VIEW3D_MT_view.append(draw_gizmo_menu)
    bpy.types.IMAGE_MT_view.append(draw_gizmo_menu)
    
    # Keymap reg
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.incease_gizmo_size", type='PAGE_UP', value='PRESS')# GIZMO +
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.decease_gizmo_size", type='PAGE_DOWN', value='PRESS')# GIZMO -
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.move_local_x", type='LEFT_ARROW', alt=True, value='PRESS')# MOVE X
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.move_local_nx", type='RIGHT_ARROW', alt=True, value='PRESS')# MOVE -X
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.move_local_y", type='UP_ARROW', alt=True, value='PRESS')# MOVE Y
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.move_local_ny", type='DOWN_ARROW', alt=True, value='PRESS')# MOVE -Y
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.move_local_z", type='PAGE_UP', alt=True, value='PRESS')# MOVE Z
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.move_local_nz", type='PAGE_DOWN', alt=True, value='PRESS')# MOVE -Z
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.rotate_local_x", type='LEFT_ARROW', alt=True, shift=True, value='PRESS')# ROTATE X
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.rotate_local_nx", type='RIGHT_ARROW', alt=True, shift=True, value='PRESS')# ROTATE -X
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.rotate_local_y", type='UP_ARROW', alt=True, shift=True, value='PRESS')# ROTATE Y
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.rotate_local_ny", type='DOWN_ARROW', alt=True, shift=True, value='PRESS')# ROTATE -Y
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.rotate_local_z", type='PAGE_UP', alt=True, shift=True, value='PRESS')# ROTATE Z
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.rotate_local_nz", type='PAGE_DOWN', alt=True, shift=True, value='PRESS')# ROTATE -Z
        addon_keymaps.append((km, kmi))


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    bpy.types.VIEW3D_MT_view.remove(draw_gizmo_menu)
    bpy.types.IMAGE_MT_view.remove(draw_gizmo_menu)

    # Keymap unreg
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
