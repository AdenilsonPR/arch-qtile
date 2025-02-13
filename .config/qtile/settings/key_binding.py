from libqtile.config import Key
from libqtile.lazy import lazy
from .default import *


keys = [
    Key([super], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([super], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([super], "down", lazy.layout.down(), desc="Move focus down"),
    Key([super], "up", lazy.layout.up(), desc="Move focus up"),
    Key([super, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([super, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([super, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([super, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([super, alt], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([super, alt], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([super, alt], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([super, alt], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([super, alt], "r", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(["control", alt], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key([super], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([alt], "f4", lazy.window.kill(), desc="Kill focused window"),
    Key([super], "t", lazy.hide_show_bar("top"), desc="Toggle fullscreen on the focused window"),
    Key([super], "f11", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([super, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([super, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([super], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([super, "control"], "right", lazy.screen.next_group(), desc="Move to the group on the right"),
    Key([super, "control"], "left", lazy.screen.prev_group(), desc="Move to the group on the left"),
    Key([super], "e", lazy.spawn([terminal, "-e", file_manager]), desc="File manager"), 
    Key([super], "space", lazy.spawn("rofi -show drun"), desc="Open Rofi applications"), 
    Key([super], "tab", lazy.spawn("rofi -show window"), desc="Open Rofi windows"),
    Key([super], "b", lazy.spawn("rofi -show filebrowser"), desc="Open Rofi file browser"),
    Key([super], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle"), desc="Mute volume"), 
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute"), desc="Volume -"), 
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute"), desc="Volume +"), 
]
