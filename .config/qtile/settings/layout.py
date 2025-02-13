from libqtile import layout
from .color import decoration_hover, decoration_focus


layout_base_theme = {
    "border_focus": decoration_hover,
    "border_normal": decoration_focus,
    "border_width": 2,
    "margin": 8,
}


layouts = [
    layout.MonadTall(**layout_base_theme),
]