Power manangement
------

An easy way to switch between AC and BAT on thinkpad lenovo, using obkey

Usage
-----
Add two keyboard shortcuts, using [obkey](https://aur.archlinux.org/packages/obkey/), one to set power management to **AC** and one to set it to **BAT**

For example add `CTRL+SHIFT+A` for **AC** and `CTRL+SHIFT+B` for **BAT**

Script is just one liner: `sudo tlp $1 ; notify-send Power "Set to $1"`


Battery status tray icon
-----

Using `batterymon` from AUR
