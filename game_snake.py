import pygame
import functions
from random import randint

pygame.init()

#COLORS
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_green = (34, 139, 34)
color_black = (0, 0, 0)

#CONTROLERS
LEFT = 0
RIGTH = 1
UP = 3
DOWN = 4

size = width, heigth = 400, 400
x = y = 200
speed = 10
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')
background = pygame.image.load("background.jpg")
points = 0

#SNAKE
snake = [(x, y), (x+10, y), (x+20, y), (x+30 ,y)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill(color_green)
direction = None

#APPLE
apple = (randint(45, 355) // 10 * 10, randint(65, 355) // 10 * 10)
apple_skin = pygame.Surface((10, 10))
apple_skin.fill(color_red)

fps = pygame.time.Clock()



screen_open = True
while screen_open:
    fps.tick(speed)
    screen.blit(background, (0, 0))

    functions.walls(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen_open = False

    # Add text points
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(f'Points: {points}', True, color_white)
    text_rect = text.get_rect()
    text_rect.center = (200, 30)
    screen.blit(text, text_rect)

    #SHOW SNAKE
    for position in snake:
        screen.blit(snake_skin, position)

    #SHOW APPLE
    screen.blit(apple_skin, apple)

    #CONTROLERS
    comand = pygame.key.get_pressed()
    if comand[pygame.K_UP]:
        direction = UP
    if comand[pygame.K_DOWN]:
        direction = DOWN
    if comand[pygame.K_LEFT]:
        direction = LEFT
    if comand[pygame.K_RIGHT]:
        direction = RIGTH

    #MOVE
    if direction == UP:
        snake[0] = snake[0][0], snake[0][1] - 10

    elif direction == DOWN:
        snake[0] = snake[0][0], snake[0][1] + 10

    elif direction == LEFT:
        snake[0] = snake[0][0] - 10, snake[0][1]

    elif direction == RIGTH:
        snake[0] = snake[0][0] + 10, snake[0][1]

    for pos in range(len(snake)-1, 0, -1):
        snake[pos] = snake[pos-1][0], snake[pos-1][1]

    #COLISION(SNAKE-APPLE)
    if snake[0] == apple:
        snake.append((snake[-1][0] - 10, snake[-1][1]))
        speed += 0.5
        apple = (randint(45, 355) // 10 * 10, randint(65, 355) // 10 * 10)
        points += 10


    pygame.display.update()

pygame.quit()