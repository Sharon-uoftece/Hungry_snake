import pygame
pygame.init()

white = (0, 0, 0)
display_surface = pygame.display.set_mode((1500, 1500))
pygame.display.set_caption('Image')
image = pygame.image.load('gameOver.jpg')
while True :
	display_surface.fill(white)
	display_surface.blit(image, (330, 350))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		pygame.display.update()
			

