import pygame


def controler (_x, _y ,_speed):
    comand = pygame.key.get_pressed()
    if comand[pygame.K_DOWN]:
        _y += _speed
    if comand[pygame.K_UP]:
        _y -= _speed
    if comand[pygame.K_LEFT]:
        _x -= _speed
    if comand[pygame.K_RIGHT]:
        _x += _speed
    return _x, _y


def walls (screen):
    pygame.draw.lines(screen, (0,0,0), False, [[40, 60], [360, 60], [360, 360], [40, 360], [40, 60]], 5)

