import pygame, sys, random

# class Block(pygame.sprite.Sprite):
#   def __init__():

# class Player(Block):
#   def __init__():

# class Ball(Block):
#   def __init__():

# class Opponent(Block):
#   def __init__():

# class GameManager:

# Inital setup for pygame
pygame.init()
clock = pygame.time.Clock()

# Setting up the main screen for displaying window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Global Variables
bg_color = pygame.Color("black")
accent_color = pygame.Color("white")
middle_strip = pygame.Rect(screen_width/2 - 2, 0, 4, screen_height)

while True:
  # Handling input
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        player.movement += player.speed
      if event.key == pygame.K_UP:
        player.movement -= player.speed
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_DOWN:
        player.movement -= player.speed
      if event.key == pygame.K_UP:
        player.movement += player.speed

  # Rendering and updating the window
  pygame.display.flip()
  # Limits the loop to run 60 fps
  clock.tick(60)