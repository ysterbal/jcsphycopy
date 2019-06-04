from psychopy import visual, core, hardware, event
# Configure the screen
# This is my setup on my MAC
# Change it to suite your needs
PRIMARY_SCREEN_SIZE = [1920,1200]   
SECONDARY_SCREEN_SIZE = [1920,1200]   
# If this is a MAC set this to True
# Define the fullscreen only for release run this with -O for release
if __debug__: 
    FULL_SCREEN = False
else:
    FULL_SCREEN = True

# Setup the windows, we will use framed for debugging but full screen for release
window_primary = visual.Window(size=PRIMARY_SCREEN_SIZE,units="pix", screen=0,allowGUI=False,fullscr=FULL_SCREEN)
window_secondary = visual.Window(size=SECONDARY_SCREEN_SIZE,units="pix", screen=1,allowGUI=False,fullscr=FULL_SCREEN)

# Setup the visuals to be displayed
# Setup stimulus
stimulant = visual.GratingStim(window_secondary,units="pix",size=SECONDARY_SCREEN_SIZE)

stimulant.autoDraw = False  # Automatically draw every frame
stimulant.autoLog = False  # Or we'll get many messages about phase change

# Start 
clock = core.Clock()
# Loop forever 
while 1: # Change this for conditional looping (not forever)
    while clock.getTime() < 200.0:  # Do stimulant for 200s
        if 0.5 <= clock.getTime() < 4.0: 
            stimulant.phase += 0.1  # Increment by 10th of cycle
        else: 
            stimulant.phase -= 0.1  # Increment by 10th of cycle
        stimulant.draw()
        window_secondary.flip()
        core.wait(.1)
    clock.reset()
    window_secondary.clearBuffer()
    while clock.getTime() < 100.0:  # Do nothing for 100s
        window_secondary.flip()

# Reset 
stimulant.reset()
clock.reset()

# Clean up windows
window_primary.release()
window_primary.close()
window_secondary.release()
window_secondary.close()

# Exit application
exit