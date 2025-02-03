import pygame

# Initialize stuff
pygame.mixer.init()

# Load the sound
pygame.mixer.music.load("sounds\\ringtone1.mp3")

# Start playing the sound in a loop (-1 means infinite loop)
pygame.mixer.music.play(loops=-1)  # Use loops=N for N loops, or -1 for infinite

input("Press Enter to stop the sound")
pygame.mixer.music.stop()
