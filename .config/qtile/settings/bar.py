from .color import *
from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy

bar_theme = {
    "size": 28,
    "margin": [8, 8, 0, 8],
    "background": background_normal,
    "border_color": decoration_focus,
    "border_width": 1,
}

group_box_theme = {
    "active": foreground_normal,
    "inactive": foreground_inactive,
    "highlight_method": "text",
    "this_current_screen_border": decoration_hover,
    "urgent_text": foreground_positive,
    "urgent_alert_method": "text",
    "fontsize": 16,
    "disable_drag": True,
}

widget_defaults = dict(
    font="FiraMono Nerd Font",
    fontsize=12,
    padding=4,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(text = "󰣇", fontsize = 20, padding = 8, foreground = foreground_normal, mouse_callbacks={'Button1': lazy.spawncmd()}),
                widget.Spacer(length = 4),
               
                widget.Sep(size_percent = 75, linewidth = 1, foreground = decoration_focus),
                widget.GroupBox(**group_box_theme),
               
                widget.Spacer(length = 2),
                widget.Sep(size_percent = 75, linewidth = 1, foreground = decoration_focus),
               
                widget.Spacer(length = 4),
                widget.Prompt(prompt = "󰣇  " , fontsize = 12, foreground = foreground_normal),
                
                widget.Spacer(length = bar.STRETCH),
                widget.TextBox(text = "󰍛", fontsize = 18, foreground = foreground_inactive),
                widget.Spacer(length = 6),
                widget.CPU(format = "{load_percent}%", foreground = foreground_normal, update_interval = 5),
                
                widget.Spacer(length = 4),
                widget.Sep(size_percent = 75, linewidth = 1, foreground = decoration_focus),
                widget.Spacer(length = 4),
                
                widget.TextBox(text = "󰘚", fontsize = 16, foreground = foreground_inactive),
                widget.Memory(foreground = foreground_normal, update_interval = 5),
                widget.Spacer(length = bar.STRETCH),

                widget.Systray(icon_size = 18),
                widget.Spacer(length = 4),

                widget.Sep(size_percent = 75, linewidth = 1, foreground = decoration_focus),
                widget.TextBox(text = " ", fontsize = 15, foreground = foreground_inactive),
                widget.Volume(foreground = foreground_normal), 
                
                widget.Sep(size_percent = 75, linewidth = 1, foreground = decoration_focus),
                widget.TextBox(text = " ", fontsize = 14, foreground = foreground_inactive),
                widget.Net(format = "{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}", foreground = foreground_normal, update_interval = 5),
                
                widget.Sep(size_percent = 75, linewidth = 1, foreground = decoration_focus),
                widget.TextBox(text = " ", fontsize = 13, foreground = foreground_inactive),
                widget.Battery(foreground = foreground_normal, format = "{percent:2.0%}", show_short_text = False),
                
                widget.Sep(size_percent = 75, linewidth = 1, foreground = decoration_focus),
                
                widget.TextBox(text = "", foreground = foreground_inactive),
                widget.Clock(format = "%d/%m/%Y", foreground = foreground_normal),
                
                widget.TextBox(text = "󰥔", fontsize = 14, foreground = foreground_inactive),
                widget.Clock(format = "%H:%M", foreground = foreground_normal),
                widget.Spacer(length = 4),
            ],
            **bar_theme
        ),
    ),
]
