import pygame
import sys
import os
pygame.init() # 初期化

game_dir = os.path.dirname(__file__)
img_dir = os.path.join(game_dir, "img")

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
		self.rect = (x, y, width, height)

	def draw(self):
		screen.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):

	def __init__(self, x, y, health = 100):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("./enemypic.png")
		width = self.image.get_width()
		height = self.image.get_height()
		self.rect = (x, y, width, height)
	
	def draw(self):
		screen.blit(self.image, self.rect)
		
def main():
	mainloop = True
	while mainloop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				mainloop = False # pygame window closed by user
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					mainloop = False # user pressed ESC
		Player1 = Player(0, 0)
		Enemy1 = Enemy(100,100,10)
		Player1.draw()
		Enemy1.draw()
		pygame.display.flip()

if __name__ == "__main__":
    main()

		
