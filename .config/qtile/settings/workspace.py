from .key_binding import *
from libqtile.config import Group, Key

workspaces = [
    {
        "name": "1",
        "key": "1",
        "label": "󰍡",
    },
    {
        "name": "2",
        "key": "2",
        "label": "󰩉",
    },
    {
        "name": "3",
        "key": "3",
        "label": "󰅨",
    },
    {
        "name": "4",
        "key": "4",
        "label": "󰙨",
    },
    {
        "name": "5",
        "key": "5",
        "label": "",
    },
]
groups = []

for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    groups.append(Group(workspace["name"], matches = matches, label = workspace["label"]))
    keys.append(Key([super], workspace["key"], lazy.group[workspace["name"]].toscreen(), desc="Focus certain workspace"))
    keys.append(Key([super, "shift"], workspace["key"], lazy.window.togroup(workspace["name"]), desc="Move focused window to another workspace"))