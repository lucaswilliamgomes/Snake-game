import pygame
import functions

pygame.init()

size = width, heigth = 400, 400
x = y = 200
speed = 10
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Gaminho')
backgraound = pygame.image.load("background.jpg")
screen_open = True

while screen_open:
    pygame.time.delay(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen_open = False

    x, y = functions.controler(x, y, speed)



    screen.blit(backgraound, (0,0))
    pygame.draw.line(screen, (0,0,0), (40,40), (360,40), 5)
    pygame.draw.line(screen, (0, 0, 0), (360, 40), (360, 360), 5)
    pygame.draw.line(screen, (0, 0, 0), (360, 360), (40, 360), 5)
    pygame.draw.line(screen, (0, 0, 0), (40, 360), (40, 40), 5)
    pygame.draw.circle(screen, (0,255,255), (x,y), 15)
    pygame.display.update()

pygame.quit()