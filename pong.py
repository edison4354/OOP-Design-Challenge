import pygame, sys, random

class Block():
  def __init__(self, x_pos, y_pos, width, height):
    self.rect = pygame.Rect(x_pos, y_pos, width, height)

class Player(Block):
	def __init__(self,x_pos,y_pos,speed):
		super().__init__(x_pos,y_pos, 10, 140)
		self.speed = speed

	def screen_constrain(self):
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= screen_height:
			self.rect.bottom = screen_height

  def update():
    self.rect.y += self.speed

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')



# Game objects
player = Player(screen_width - 20,screen_height/2, 0)
print(player)
# opponent = Opponent(screen_width - 20, screen_height/2 - 70, 7)
# ball = Ball(10, screen_height/2 - 70,)

while True:
  # Handling input
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        player.speed += 7
      if event.key == pygame.K_UP:
        player.speed -= 7 
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_DOWN:
        player.speed -= 7
      if event.key == pygame.K_UP:
        player.speed += 7

  # Rendering and updating the window
  pygame.display.flip()
  # Limits the loop to run 60 fps
  clock.tick(60)