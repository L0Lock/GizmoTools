# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Gizmo Size",
    "description": "Allows you to increase or decrease the Gizmo size using keyboard shortcuts.",
    "author": "Loïc \"L0Lock\" Dautry",
    "version": (0, 0, 2),
    "blender": (2, 82, 7),
    "location": "View3D → Header → View → Gizmo",
    "warning": "",
    "wiki_url": "not yet",
    "tracker_url": "not yet",
    "category": "3D View"
}

import bpy
import rna_keymap_ui
from bpy.props import FloatProperty
from bpy.types import (
    AddonPreferences,
    Operator,
    Menu,
)

# -----------------------------------------------------------------------------
#    Operator : Decrease size    
# -----------------------------------------------------------------------------
class VIEW3D_OT_decease_gizmo_size(bpy.types.Operator):
    bl_idname = "view3d.decease_gizmo_size"
    bl_label = "Decrease Gizmo Size"
    
    def execute(self, context):
        
        prefs = context.preferences
        addon_prefs = prefs.addons[__name__].preferences
        view = prefs.view
        gs = view.gizmo_size
        print ("Gizmo size =", gs)
        print ("Increment =", addon_prefs.inc)
        
        gs = gs - addon_prefs.inc
        view.gizmo_size = gs
        print ("New Gizmo size =", gs)
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Increase size    
# -----------------------------------------------------------------------------
class VIEW3D_OT_incease_gizmo_size(bpy.types.Operator):
    bl_idname = "view3d.incease_gizmo_size"
    bl_label = "Increase Gizmo Size"
    
    def execute(self, context):
        
        prefs = context.preferences
        addon_prefs = prefs.addons[__name__].preferences
        view = prefs.view
        gs = view.gizmo_size
        print ("Gizmo size =", gs)
        print ("Increment =", addon_prefs.inc)
        
        gs = gs + addon_prefs.inc
        view.gizmo_size = gs
        print ("New Gizmo size =", gs)
        return {'FINISHED'}


# -----------------------------------------------------------------------------
#    Preferences      
# -----------------------------------------------------------------------------
class VIEW3D_PT_gizmo_size_preferences(AddonPreferences):
    bl_idname = __name__

    # Increment value
    inc : FloatProperty(
        name="Increment",
        description="Increment in px.",
        default=10,
        min=1,
        max=100,
        step=100,
        precision=0,
        subtype="PIXEL"
        )

    # Draws addon preferences
    def draw(self, context):
        layout = self.layout

        # Increment value
        row = layout.row(align=True)
        row.prop(self, "inc", toggle=True)

# -----------------------------------------------------------------------------
#    Gizmo Menu      
# -----------------------------------------------------------------------------
class VIEW3D_MT_gizmo_size_menu(bpy.types.Menu):
    bl_label = "Gizmo"
    bl_idname = "VIEW3D_MT_gizmo_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("view3d.incease_gizmo_size", icon="ZOOM_IN")
        layout.operator("view3d.decease_gizmo_size", icon="ZOOM_OUT")

def draw_gizmo_menu(self, context):
    layout = self.layout
    layout.menu(VIEW3D_MT_gizmo_size_menu.bl_idname)

# -----------------------------------------------------------------------------
#    Keymap   
# -----------------------------------------------------------------------------
addon_keymaps = []


# -----------------------------------------------------------------------------
#    Register   
# -----------------------------------------------------------------------------

def register():
    bpy.utils.register_class(VIEW3D_PT_gizmo_size_preferences)
    bpy.utils.register_class(VIEW3D_OT_incease_gizmo_size)
    bpy.utils.register_class(VIEW3D_OT_decease_gizmo_size)
    bpy.utils.register_class(VIEW3D_MT_gizmo_size_menu)
    bpy.types.VIEW3D_MT_view.append(draw_gizmo_menu)
    
    # Keymap reg
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new("view3d.decease_gizmo_size", type='PAGE_DOWN', value='PRESS')
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new("view3d.incease_gizmo_size", type='PAGE_UP', value='PRESS')
        addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_gizmo_size_preferences)
    bpy.utils.unregister_class(VIEW3D_OT_incease_gizmo_size)
    bpy.utils.unregister_class(VIEW3D_OT_decease_gizmo_size)
    bpy.utils.unregister_class(VIEW3D_MT_gizmo_size_menu)
    bpy.types.VIEW3D_MT_view.remove(draw_gizmo_menu)

    # Keymap unreg
    for km,kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()