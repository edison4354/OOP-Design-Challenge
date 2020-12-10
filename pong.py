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

class Ball(Block):
	def __init__(self,path,x_pos,y_pos,speed_x,speed_y,paddles):
		super().__init__(path,x_pos,y_pos)
		self.speed_x = speed_x * random.choice((-1,1))
		self.speed_y = speed_y * random.choice((-1,1))
		self.paddles = paddles
		self.active = False

  # Moves the x and y position of the ball and detectis
	def update(self):
		if self.active:
			self.rect.x += self.speed_x
			self.rect.y += self.speed_y
			self.collisions()
		else:
			self.restart_counter()
		
	def collisions(self):
    # Checks if the ball collides with either the top or bottom of the screen
		if self.rect.top <= 0 or self.rect.bottom >= screen_height:
			self.speed_y *= -1

    # Checks if the ball collides with the paddle
		if pygame.sprite.spritecollide(self,self.paddles,False):
			collision_paddle = pygame.sprite.spritecollide(self,self.paddles,False)[0].rect
			if abs(self.rect.right - collision_paddle.left) < 10 and self.speed_x > 0:
				self.speed_x *= -1
			if abs(self.rect.left - collision_paddle.right) < 10 and self.speed_x < 0:
				self.speed_x *= -1
			if abs(self.rect.top - collision_paddle.bottom) < 10 and self.speed_y < 0:
				self.rect.top = collision_paddle.bottom
				self.speed_y *= -1
			if abs(self.rect.bottom - collision_paddle.top) < 10 and self.speed_y > 0:
				self.rect.bottom = collision_paddle.top
				self.speed_y *= -1

	def reset_ball(self):
    # Sets the ball back to the center and moves the ball to a random directions 
		self.active = True
		self.speed_x *= random.choice((-1,1)) 
		self.speed_y *= random.choice((-1,1))
		self.rect.center = (screen_width/2,screen_height/2)

class Opponent(Block):
	def __init__(self,path,x_pos,y_pos,speed):
		super().__init__(path,x_pos,y_pos)
		self.speed = speed

  # This function is made for the paddle to follow the ball y
	def update(self,ball_group):
		if self.rect.top < ball_group.sprite.rect.y:
			self.rect.y += self.speed
		if self.rect.bottom > ball_group.sprite.rect.y:
			self.rect.y -= self.speed
		self.constrain()

  # Keeps the paddle from going out of the screen
	def constrain(self):
		if self.rect.top <= 0: self.rect.top = 0
		if self.rect.bottom >= screen_height: self.rect.bottom = screen_height

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
opponent = Opponent('Paddle.png', 20, screen_width/2, 6)
paddle_group = pygame.sprite.Group()
paddle_group.add(player)
paddle_group.add(opponent)

ball = Ball('Ball.png', screen_width/2, screen_height/2, 4, 4, paddle_group)
ball_sprite = pygame.sprite.GroupSingle()
ball_sprite.add(ball)

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