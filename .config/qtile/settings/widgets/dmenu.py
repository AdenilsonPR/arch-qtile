from libqtile import extension
from libqtile.lazy import lazy
from ..color import background_normal, decoration_hover, foreground_normal

dmenu = lazy.run_extension(extension.DmenuRun(
    dmenu_prompt = "󰣇  ",
    background = background_normal,
    foreground = foreground_normal,
    selected_background = decoration_hover,
    selected_foreground = foreground_normal,
    dmenu_command = "dmenu_run",
    fontsize = 10,
    dmenu_lines = 10,
))