## Wallpaper changer

Script that changes wallpaper every X minutes

Dependencies:

- python2.7
- feh


### Script config 

Edit the top part of the script to reflect your system/taste

```
PICTURES_FOLDER = '/home/icebox/Pictures/wallpapers'
ROTATE_EVERY = 60   # minutes
```

### Auto-start

As usual, add something like this into `~/.config/openbox/autostart` file:

```
(sleep 2 && /home/icebox/Documents/scripts/change_wallpaper.py) &
```
