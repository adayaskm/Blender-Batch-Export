import bpy
import os
from bpy.types import AddonPreferences, PropertyGroup, Operator, Panel
from bpy.props import (
    BoolProperty, StringProperty, EnumProperty, PointerProperty
)

bl_info = {
    "name": "Batch Export",
    "author": "Adayas",
    "version": (2, 4, 0),
    "blender": (1, 0, 0),
    "category": "Import-Export",
    "location": "Top Bar > Batch Export",
    "description": "Batch export selected objects or their collection to individual files with format selection.",
}

# ----------------------- Utility Functions ----------------------- #

def ensure_dir(path: str):
    """Ensure the export directory exists."""
    if not os.path.exists(path):
        os.makedirs(path)

# ----------------------- Operator ----------------------- #

class EXPORT_OT_batch_export(Operator):
    """Batch export selected objects or their collection."""
    bl_idname = "export.batch_export"
    bl_label = "Export Objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        settings = context.scene.batch_export
        export_path = bpy.path.abspath(settings.export_directory)
        ensure_dir(export_path)

        exporters = {
            'FBX': self.export_fbx,
            'OBJ': self.export_obj,
            'GLTF': self.export_gltf,
            'STL': self.export_stl
        }

        export_func = exporters.get(settings.file_format)
        if not export_func:
            self.report({'ERROR'}, f"Unsupported format: {settings.file_format}")
            return {'CANCELLED'}

        objects_to_export = []

        if settings.export_mode == 'SELECTED':
            objects_to_export = context.selected_objects
            if not objects_to_export:
                self.report({'WARNING'}, "No objects selected for export.")
                return {'CANCELLED'}

        elif settings.export_mode == 'COLLECTION':
            active_obj = context.active_object
            if active_obj and active_obj.users_collection:
                collection = active_obj.users_collection[0]
                objects_to_export = [obj for obj in collection.objects if obj.type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'ARMATURE'}]
            else:
                self.report({'WARNING'}, "No active object or collection found.")
                return {'CANCELLED'}

        for obj in objects_to_export:
            export_func(obj, export_path, settings)

        self.report({'INFO'}, f"Exported {len(objects_to_export)} object(s) as {settings.file_format}.")
        return {'FINISHED'}

    def prepare_object(self, obj, settings):
        original_location = obj.location.copy()
        if settings.move_to_origin:
            obj.location = (0, 0, 0)
        return original_location

    def restore_object(self, obj, original_location):
        obj.location = original_location

    def export_fbx(self, obj, path, settings):
        self.export_generic(obj, path, settings, '.fbx', bpy.ops.export_scene.fbx)

    def export_obj(self, obj, path, settings):
        self.export_generic(obj, path, settings, '.obj', bpy.ops.export_scene.obj)

    def export_gltf(self, obj, path, settings):
        self.export_generic(obj, path, settings, '.glb', bpy.ops.export_scene.gltf, {"export_selected": True})

    def export_stl(self, obj, path, settings):
        self.export_generic(obj, path, settings, '.stl', bpy.ops.export_mesh.stl)

    def export_generic(self, obj, path, settings, extension, export_op, extra_args=None):
        original_location = self.prepare_object(obj, settings)
        filename = os.path.join(path, f"{settings.file_prefix}{obj.name}{settings.file_suffix}{extension}")
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        export_args = {
            "filepath": filename,
            "use_selection": True,
            "use_mesh_modifiers": settings.apply_modifiers,
        }
        if extra_args:
            export_args.update(extra_args)

        export_op(**export_args)
        self.restore_object(obj, original_location)

# ----------------------- UI Panels ----------------------- #

class VIEW3D_PT_batch_export(Panel):
    bl_label = "Batch Export"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Export'

    def draw(self, context):
        layout = self.layout
        settings = context.scene.batch_export

        layout.prop(settings, "export_directory")
        layout.prop(settings, "file_format")
        layout.prop(settings, "export_mode")
        layout.prop(settings, "file_prefix")
        layout.prop(settings, "file_suffix")
        layout.prop(settings, "move_to_origin")
        layout.prop(settings, "apply_modifiers")
        layout.operator("export.batch_export")

class TOPBAR_MT_batch_export_menu(bpy.types.Menu):
    bl_label = "Batch Export"
    bl_idname = "TOPBAR_MT_batch_export_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("export.batch_export", icon='EXPORT')

# ----------------------- Properties ----------------------- #

class BatchExportSettings(PropertyGroup):
    export_directory: StringProperty(
        name="Export Directory",
        description="Directory to save exported files.",
        subtype='DIR_PATH',
        default="//"
    )

    file_format: EnumProperty(
        name="File Format",
        description="Select the file format for export.",
        items=[
            ('FBX', "FBX (.fbx)", "Export as FBX format"),
            ('OBJ', "OBJ (.obj)", "Export as OBJ format"),
            ('GLTF', "glTF (.glb)", "Export as glTF format"),
            ('STL', "STL (.stl)", "Export as STL format"),
        ],
        default='FBX'
    )

    export_mode: EnumProperty(
        name="Export Mode",
        description="Choose whether to export selected objects or the entire collection of the active object.",
        items=[
            ('SELECTED', "Selected Objects", "Export only selected objects"),
            ('COLLECTION', "Collection", "Export all objects in the active object's collection"),
        ],
        default='SELECTED'
    )

    file_prefix: StringProperty(
        name="File Prefix",
        description="Prefix for exported file names.",
        default=""
    )

    file_suffix: StringProperty(
        name="File Suffix",
        description="Suffix for exported file names.",
        default=""
    )

    move_to_origin: BoolProperty(
        name="Move to Origin",
        description="Temporarily move objects to the world origin before export.",
        default=True
    )

    apply_modifiers: BoolProperty(
        name="Apply Modifiers",
        description="Apply modifiers before export.",
        default=True
    )

# ----------------------- Registration ----------------------- #

def draw_menu(self, context):
    self.layout.menu(TOPBAR_MT_batch_export_menu.bl_idname, icon='EXPORT')

def register():
    bpy.utils.register_class(BatchExportSettings)
    bpy.utils.register_class(EXPORT_OT_batch_export)
    bpy.utils.register_class(VIEW3D_PT_batch_export)
    bpy.utils.register_class(TOPBAR_MT_batch_export_menu)
    bpy.types.Scene.batch_export = PointerProperty(type=BatchExportSettings)
    bpy.types.TOPBAR_MT_file.append(draw_menu)

def unregister():
    del bpy.types.Scene.batch_export
    bpy.types.TOPBAR_MT_file.remove(draw_menu)
    bpy.utils.unregister_class(TOPBAR_MT_batch_export_menu)
    bpy.utils.unregister_class(VIEW3D_PT_batch_export)
    bpy.utils.unregister_class(EXPORT_OT_batch_export)
    bpy.utils.unregister_class(BatchExportSettings)

if __name__ == "__main__":
    register()
