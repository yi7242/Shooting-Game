import pygame
from pygame.locals import *
import sys
import math
pygame.init() # 初期化
screen = pygame.display.set_mode((640,480))
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))
screen.blit(background,(0,0))
background = background.convert()


class Player(pygame.sprite.Sprite):
	
	def __init__(self, x, y, health=500):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("./playerpic.png")
		width = self.image.get_width()
		height = self.image.get_height()
		self.rect = pygame.Rect(x, y, width, height)
		print(width,height)
	def draw(self):
		screen.blit(self.image, self.rect)
	def aim(self, confusion = False):
		mouse_pos = pygame.mouse.get_pos()
		self.image = pygame.transform.rotate(pygame.image.load("./playerpic.png"), rotation)
	def move(self, speed = 3):
		keys = pygame.key.get_pressed()
		if keys[K_UP]:
			self.rect.y-= speed
		if keys[K_DOWN]:
			self.rect.y += speed
		if keys[K_RIGHT]:
			self.rect.x += speed
		if keys[K_LEFT]:
			self.rect.x -= speed
		self.rect.clamp_ip(screen.get_rect())
		
class Enemy(pygame.sprite.Sprite):

	def __init__(self, x, y, health = 100):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("./enemypic.png")
		width = self.image.get_width()
		height = self.image.get_height()
		self.rect = pygame.Rect(x, y, width, height)

	def draw(self):
		screen.blit(self.image, self.rect)

class Bullet(pygame.sprite.Sprite):
	def  __init__(self, bullet_speed = 10):
		pygame.sprite.Sprite.__init__(self)
		
		
def main():
	pygame.display.set_caption("ShootingGame")
	loop = True
	Player1 = Player(0, 0)
	Enemy1 = Enemy(100,100,10)
	rotate = 0
	while loop:
		screen.blit(background,(0,0))
		Player1.draw()
		Enemy1.draw()
		Player1.move()
		Player1.aim(rotate)
		rotate += 1
		if rotate > 360:
			rotate = rotate - 360
		print(rotate)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				loop = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					loop = False
if __name__ == "__main__":
	main()

		
