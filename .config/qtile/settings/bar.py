from .color import *
from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from .default import application_launcher

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
}

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
                widget.TextBox(text = "󰷐", fontsize = 20, padding = 8, foreground = foreground_normal, mouse_callbacks={'Button1': lazy.spawn(application_launcher)}),
                widget.Spacer(length = 4),
                widget.Sep(size_percent = 75, linewidth = 1, foreground = decoration_focus),
                widget.GroupBox(**group_box_theme),
                widget.Spacer(length = 2),
                widget.Sep(size_percent = 75, linewidth = 1, foreground = decoration_focus),
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
