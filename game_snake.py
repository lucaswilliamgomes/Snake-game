import pygame
import functions

pygame.init()

color_white = (255,255,255)

size = width, heigth = 400, 400
x = y = 200
speed = 1
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')
background = pygame.image.load("background.jpg")
points = 0

#Add text points
font = pygame.font.Font('freesansbold.ttf', 15)
text = font.render(f'Points: {points}', True, color_white)
text_rect = text.get_rect()
text_rect.center = (200, 30)

screen_open = True
while screen_open:
    pygame.time.delay(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen_open = False

    x, y = functions.controler(x, y, speed)

    screen.blit(background, (0, 0))
    screen.blit(text, text_rect)
    functions.walls(screen)
    pygame.draw.rect(screen, color_white, pygame.Rect(x - 10, y - 10, 10, 10))
    pygame.display.update()

pygame.quit()