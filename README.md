# Duel screen stimulant

This script is used to run a stimulant, on a duel screen. 

One screen (Screen 0) displays only a gray, the other (Screen 1) is used to display the stimulant. The script will run forever ( use control-c to break out). 

Note please adjust PRIMARY_SCREEN_SIZE and SECONDARY_SCREEN_SIZE to suite your needs and screen resolutions

**Timing**
Display stimulant for 200 seconds then reset back to gray for 100s note it is action 200s + .1 of a second for every cycle as my MAC is too fast so it looks just like noise.

**Notes**
For now I only use a visual.GratingStim with defaults you can find more details of the settings here. http://www.djmannion.net/psych_programming/vision/draw_gratings/draw_gratings.html

