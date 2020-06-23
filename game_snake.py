import pygame
from random import randint

pygame.init()

#COLORS
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_green = (34, 139, 34)
color_brown = (200, 100, 50)

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
background = pygame.image.load("back_green.png")
points = 0

#SNAKE
snake = [(x, y), (x+10, y), (x+20, y), (x+30 ,y)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill(color_brown)
direction = None

#APPLE
apple = (randint(60, 340) // 10 * 10, randint(80, 340) // 10 * 10)
apple_skin = pygame.Surface((10, 10))
apple_skin.fill(color_red)

fps = pygame.time.Clock()

#GAME OVER
game_over = pygame.image.load('game_over.png')
over_dimens = game_over.get_rect()
over_dimens.center = (200, 200)

screen_open = True
while screen_open:
    fps.tick(speed)
    screen.blit(background, (0, 0))

    # SHOW WALL
    pygame.draw.lines(screen, (0, 0, 0), False, [[40, 60], [360, 60], [360, 360], [40, 360], [40, 60]], 10)

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

    #COLISION (SNAKE-APPLE)
    if snake[0] == apple:
        snake.append((snake[-1][0] - 10, snake[-1][1]))
        speed += 0.3
        apple = (randint(60, 340) // 10 * 10, randint(80, 340) // 10 * 10)
        points += 10

    #COLISION (SNAKE-WALL)
    if snake[0][0]  == 40 or snake[0][0] == 350 or snake [0][1] == 60 or snake[0][1] == 350:
        screen.blit(game_over, over_dimens)
        direction = None

    #COLISION (SNAKE-SNAKE)


    pygame.display.update()

pygame.quit()