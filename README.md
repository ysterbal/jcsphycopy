# Example for duel screen usage of Psychopy

### Overview

This script simply runs on duel Monitors, it creates two Windows one per screen and renders a simplistic Grating on one while the other remains static. The Grating is run on the secondary screen and cycles on for 200 seconds and then off for 100 seconds. The script runs for ever and requires a ctrl-c or kill to be terminated. 

To support full screen usage the code expects to be run with the commandline parameter of -O to unset the __debug__ built-in for python, in debug we display the Windows as non decorated Windows to allow for debugging.

### Usage
This can be used in either a commandline python environment with Psychopy installed, using ''' python experiment.py ''' or using the Pshycopy Coder UI ''' python3 -m psychopy.app.psychopyApp '''

Note please adjust PRIMARY_SCREEN_SIZE and SECONDARY_SCREEN_SIZE to suite your needs and screen resolutions

I only use a visual.GratingStim with defaults you can find more details of the settings here. http://www.djmannion.net/psych_programming/vision/draw_gratings/draw_gratings.html


