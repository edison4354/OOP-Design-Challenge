import pygame, sys, random

class Block(pygame.sprite.Sprite):
  def __init__(self, path, x_pos, y_pos):
    super().__init__()
    self.image = pygame.image.load(path)
    self.rect = self.image.get_rect(center = (x_pos, y_pos))

class Player(Block):
	def __init__(self,path,x_pos,y_pos,speed):
		super().__init__(path,x_pos,y_pos)
		self.speed = speed
		self.movement = 0

  #Keeps the player from moving out of the screen
	def screen_constrain(self):
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= screen_height:
			self.rect.bottom = screen_height

  # Moves the y cooridates of the player paddle when up and down button are used
	def update(self,ball_group):
		self.rect.y += self.movement
		self.screen_constrain()

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

# Game Objects
player = Player('Paddle.png', screen_width - 20, screen_height/2, 6)
paddle_group = pygame.sprite.Group()
paddle_group.add(player)

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
  
  # Background
  screen.fill(bg_color)
  pygame.draw.rect(screen, accent_color, middle_strip)

  # Rendering and updating the window
  pygame.display.flip()
  # Limits the loop to run 60 fps
  clock.tick(60)