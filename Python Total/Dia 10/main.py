import random

import pygame

# inicializar pygame
pygame.init()
# crear la pantalla
screen = pygame.display.set_mode((800, 600))

# titulo e icono
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ovni.png")
pygame.display.set_icon(icon)

# variables del jugador
img_player = pygame.image.load("nave-espacial.png")
player_x = 368
player_y = 536
player_x_change = 0

# variables del enemigo
img_enemy = pygame.image.load("astronave.png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 200)
enemy_x_change = 0.3
enemy_y_change = 50


#funcion enemigo
def enemy(x, y):
    screen.blit(img_enemy, (x, y))


# funcion jugador
def player(x, y):
    screen.blit(img_player, (x, y))
    # le pasamos 3 valores, una la imagen del jugador y los otros 2 en una tupla del ancho
    # y largo donde se quiere posicionar al jugador


# loop del juego
se_ejecuta = True
while se_ejecuta:
    # rgb pantalla
    screen.fill((205, 144, 228))
    # iterar eventos
    for event in pygame.event.get():

        # evento cerrar
        if event.type == pygame.QUIT:
            se_ejecuta = False

        #evento presionar flecha
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3

        # evento soltar flecha
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # modificar ubicacion del jugador
    player_x += player_x_change

    # mantener dentro de bordes al jugador
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # modificar ubicacion del jugador
    enemy_x += enemy_x_change
    #enemy_y += enemy_y_change

    # mantener dentro de bordes al jugador
    if enemy_x <= 0:
        enemy_x_change = 0.3
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -0.3
        enemy_y += enemy_y_change

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    # actualizar
    pygame.display.update()
#
