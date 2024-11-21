import bpy

from ...library.shared.content_providers.content_manager import ContentManager


def serialize_mounted_content(cm: ContentManager):
    data = cm.serialize()
    resources = bpy.context.scene.mounted_resources
    for item_hash, item in data.items():
        new_resource = resources.add()
        new_resource.path = item["path"]
        new_resource.name = item["name"]
        new_resource.hash = item_hash


def deserialize_mounted_content(cm: ContentManager):
    data = {}
    resources = bpy.context.scene.mounted_resources
    for resource in resources:
        item = {"path": resource.path, "name": resource.name}
        data[resource.hash] = item
    cm.deserialize(data)
