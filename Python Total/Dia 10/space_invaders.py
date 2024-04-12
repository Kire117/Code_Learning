import random
import math
import pygame
from pygame import mixer
import io

# inicializar pygame
pygame.init()
# crear la pantalla
screen = pygame.display.set_mode((800, 600))

# fondo del juego
fondo = pygame.image.load("Fondo.jpg")

# agregar musica
mixer.music.load("MusicaFondo.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.3) # volumen de 0 al 1


# titulo e icono
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ovni.png")
pygame.display.set_icon(icon)

# variables del jugador
img_player = pygame.image.load("nave-espacial.png")
player_x = 368
player_y = 500
player_x_change = 0
player_died = pygame.image.load("explosion.png")

# variables del enemigo
img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
enemies = 8

for e in range(enemies):

    img_enemy.append(pygame.image.load("astronave.png"))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 200))
    enemy_x_change.append(0.4)
    enemy_y_change.append(50)


# funcion para convertir la fuente de string a bytes
def font_bytes(font):
    # abre el archivo en modo lectura binaria
    with open(font, 'rb') as f:
        # lee todos los bytes del archivo y los almacenas en una variable
        ttf_bytes = f.read()
        # crea un objeto BytesIOa partir de los bytes del archivo TTF
        return io.BytesIO(ttf_bytes)


# variables de la bala
bullets = []
img_bullet = pygame.image.load("bala.png")
bullet_x = 0
bullet_y = 500
bullet_y_change = 2
bullet = False

# variables de puntaje
puntaje = 0
font_as_byte = font_bytes("freesansbold.ttf")
fuente = pygame.font.Font(font_as_byte, 32)
txt_x = 10
txt_y = 10


# funcion para mostrar puntaje
def display_points(x, y):
    txt= fuente.render(f"Points: {puntaje}", True, (255, 255,255))
    screen.blit(txt, (x, y))

# texto final del juego
final_font = pygame.font.Font(font_as_byte, 40)

# funcion para mostrar end game
def final_text():
  myfinal_font = final_font.render("GAME OVER", True, (255, 255, 255))
  madeby_txt = final_font.render("Made by Kire", True, (255, 255, 255))
  screen.blit(myfinal_font, (280, 260))
  screen.blit(madeby_txt, (275, 300))

# funcion disparar bala
def shooting_bullet(x, y):
    global bullet
    bullet = True
    screen.blit(img_bullet, (x, y))


# funcion detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    operacion1 = math.pow(x_2 - x_1, 2)
    operacion2 = math.pow(y_2 - y_1, 2)
    distancia = math.sqrt(operacion1 + operacion2)
    if distancia < 27:
        return True
    else:
        return False


# funcion enemigo
def enemy(x, y, ene):
    screen.blit(img_enemy[ene], (x + 16, y + 10))


# funcion jugador
def player(x, y):
    screen.blit(img_player, (x, y))
    # le pasamos 3 valores, una la imagen del jugador y los otros 2 en una tupla del ancho
    # y largo donde se quiere posicionar al jugador

# funcion para mostrar que el jugador ha muerto al final
def death(x, y):
    screen.blit(player_died, (x, y))

# loop del juego
se_ejecuta = True
while se_ejecuta:
    # rgb pantalla
    screen.blit(fondo, (0, 0))
    # iterar eventos
    for event in pygame.event.get():

        # evento cerrar
        if event.type == pygame.QUIT:
            se_ejecuta = False

        # evento presionar teclas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5

            # disparar bala
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound("disparo.mp3")
                bullet_sound.set_volume(0.3)
                bullet_sound.play()
                new_bullet = {
                    "x": player_x,
                    "y": player_y,
                    "velocidad": -5
                }
                bullets.append(new_bullet)
                if not bullet:
                    bullet_x = player_x
                    shooting_bullet(bullet_x, bullet_y)
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

    # modificar ubicacion del enemigo
    for e in range(enemies):
        # fin del juego
        if enemy_y[e] > 500:
            for k in range(enemies):
                enemy_y[k] = 1000
            bullets.clear()
            final_text()
            death(player_x, player_y)
            break

        enemy_x[e] += enemy_x_change[e]
        # mantener dentro de bordes al enemigo
        if enemy_x[e] <= 0:
            enemy_x_change[e] = 0.4
            enemy_y[e] += enemy_y_change[e]
        elif enemy_x[e] >= 736:
            enemy_x_change[e] = -0.4
            enemy_y[e] += enemy_y_change[e]

        # colision
        for bullet in bullets:
            colision_enemies = hay_colision(enemy_x[e], enemy_y[e], bullet["x"], bullet["y"])
            if colision_enemies:
                sound_colision = mixer.Sound("Golpe.mp3")
                sound_colision.set_volume(0.3)
                sound_colision.play()
                bullets.remove(bullet)
                puntaje += 1
                enemy_x[e] = random.randint(0, 736)
                enemy_y[e] = random.randint(50, 200)
                break

        enemy(enemy_x[e], enemy_y[e], e) # aparecer los enemigos

    # movimiento bala
    for bullet in bullets:
        bullet["y"] += bullet["velocidad"]
        screen.blit(img_bullet, (bullet["x"] + 16, bullet['y'] + 10))
        if bullet["y"] < 0:
            bullets.remove(bullet)

    if bullet:
        shooting_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)

    display_points(txt_x, txt_y)
    # actualizar
    pygame.display.update()
#
