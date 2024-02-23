# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from settings.color import Color

super = "mod4"
alt = "mod1"
file_manager = "thunar"
terminal = guess_terminal()
color = Color()

layout_theme = {
    "border_focus": color.decoration_hover,
    "border_normal": color.decoration_focus,
    "border_width": 2,
    "margin": 8,
}
bar_theme = {
    "size": 28,
    "margin": [8, 8, 0, 8],
    "background": color.background_normal,
    "border_color": color.decoration_focus,
    "border_width": 1,
}
group_box_theme = {
    "active": color.foreground_normal,
    "inactive": color.foreground_inactive,
    "highlight_method": "text",
    "this_current_screen_border": color.decoration_hover,
    "urgent_text": color.foreground_positive,
    "urgent_alert_method": "text",
    "fontsize": 16,
}
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
    Key([super], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([super], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([super, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([super, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([super], "space", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([super, "control"], "right", lazy.screen.next_group(), desc="Move to the group on the right"),
    Key([super, "control"], "left", lazy.screen.prev_group(), desc="Move to the group on the left"),
    Key([super], "e", lazy.spawn(file_manager), desc="File manager"), 
]

for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    groups.append(Group(workspace["name"], matches = matches, label = workspace["label"]))
    keys.append(Key([super], workspace["key"], lazy.group[workspace["name"]].toscreen(), desc="Focus certain workspace"))
    keys.append(Key([super, "shift"], workspace["key"], lazy.window.togroup(workspace["name"]), desc="Move focused window to another workspace"))

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=4,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(text = "", fontsize = 16, padding = 8, foreground = color.foreground_link, mouse_callbacks={'Button1': lazy.spawncmd()}),
                widget.Spacer(length = 4),
                widget.Sep(size_percent = 75, linewidth = 1, foreground = color.foreground_separator),
                widget.GroupBox(**group_box_theme),
                widget.Spacer(length = 2),
                widget.Sep(size_percent = 75, linewidth = 1, foreground = color.foreground_separator),
                widget.Spacer(length = 4),
                widget.Prompt(),
                widget.Spacer(length = bar.STRETCH),
                widget.WindowName(format='{name}', scroll = True, width = 512),
                widget.Spacer(length = bar.STRETCH),
                widget.Systray(),
                widget.Clock(format="%d/%m/%Y - %H:%M "),
            ],
            **bar_theme
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([super], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([super], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([super], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "RaidZero"
