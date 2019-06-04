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

stimulant.autoDraw = False  # Automatically draw every frame, if we do this then we do not need the .draw but we have less control
stimulant.autoLog = False  # Or we'll get many messages about phase change

# Start 
clock = core.Clock() # Get a clock that we can use for timing 
# Loop forever 
while 1: # Change this for conditional looping (not forever)
    while clock.getTime() < 200.0:  # Do stimulant for 200s
        if 0.5 <= clock.getTime() < 4.0: 
            stimulant.phase += 0.1  # Increment phase
        else: 
            stimulant.phase -= 0.1  # Decrement phase
        stimulant.draw() # Draw the stimulant into the back buffer
        window_secondary.flip() # Force the screen to update from the back back buffer
        core.wait(.1) # Added wait as on some fast machines the refresh is too fast 
    clock.reset()
    window_secondary.clearBuffer() # We must clear the back buffer to ensure we have just a plain background
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