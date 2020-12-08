import pygame, sys 

# Inital setup 
pygame.init()
clock = pygame.time.Clock()

# Setting up the main screen for displaying the game
screen_width = 1280 
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

while True:
  # Handling input for exiting the page 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  # Updating the window
  pygame.display.flip()
  # Limits the loop to run 60 fps
  clock.tick(60)