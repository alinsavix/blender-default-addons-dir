bl_info = {
    "name": "Addon Directory Default Setter",
    "author": "TDV Alinsa",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "description": "Make 'User Prefs' the default addon target path",
    "warning": "Make sure you set Preferences > File Paths > Scripts",
    "doc_url": "https://github.com/alinsavix/blender-default-addons-dir",
    "tracker_url": "https://github.com/alinsavix/blender-default-addons-dir/issues",
    "category": "System"}


import bpy
from bpy.props import EnumProperty

def monkeypatch():
    newtarget = EnumProperty(
        name="Target Path",
        items=(
            ('PREFS', "User Prefs", ""),
            ('DEFAULT', "Default", ""),
        ),
    )
    cls = bpy.types.PREFERENCES_OT_addon_install
    bpy.utils.unregister_class(cls)
    cls.__annotations__['target'] = newtarget
    bpy.utils.register_class(cls)


def register():
    monkeypatch()

def unregister():
    pass
