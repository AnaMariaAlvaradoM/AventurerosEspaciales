import pygame
import random
import pygame.mixer
from sprites import *
#Cambios
# Inicializar Pygame
pygame.init()

# Configurar la ventana
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Aventureros Espaciales")

# Cargar imágenes
fondo = pygame.image.load("fondo1.jpg")
nave = NaveEspacial()
reloj = pygame.time.Clock()
musica_fondo = pygame.mixer.Sound("musica_fondo.ogg")
musica_fondo.play(loops=-1)
musica_explosion = pygame.mixer.Sound("explosion.wav")

# Crear grupos de sprites
todos_los_sprites = pygame.sprite.Group()
balas = pygame.sprite.Group()
enemigos = pygame.sprite.Group()

nave = NaveEspacial()
todos_los_sprites.add(nave)

# Crear enemigos iniciales
def crear_enemigos():
    for _ in range(10):
        enemigo = Enemigo()
        enemigos.add(enemigo)
        todos_los_sprites.add(enemigo)  # Añadir al grupo de todos los sprites para que se dibuje

crear_enemigos()

# Variables del juego
puntuacion = 0
vidas = 3

# Fuentes para el texto
fuente_grande = pygame.font.Font(None, 36)
fuente_pequena = pygame.font.Font(None, 24)

# Funciones del juego
def mostrar_texto(mensaje, x, y, color):
    texto = fuente_grande.render(mensaje, True, color)
    texto_rect = texto.get_rect(center=(x, y))
    screen.blit(texto, texto_rect)

# Crear balas
def disparar_bala():
    bala = Bala(nave.rect.centerx, nave.rect.top)
    balas.add(bala)
    todos_los_sprites.add(bala)

# Bucle principal del juego
bucle_principal = True
movimiento_izquierda = False
movimiento_derecha = False

while bucle_principal:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bucle_principal = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movimiento_izquierda = True
            if event.key == pygame.K_RIGHT:
                movimiento_derecha = True
            if event.key == pygame.K_SPACE:
                nave.disparar(balas, todos_los_sprites)  # Pasar los grupos balas y todos_los_sprites

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                movimiento_izquierda = False
            if event.key == pygame.K_RIGHT:
                movimiento_derecha = False

    # Mover la nave
    if movimiento_izquierda:
        nave.mover_izquierda()
    if movimiento_derecha:
        nave.mover_derecha()

    # Actualizar sprites
    todos_los_sprites.update()

    # Detectar colisiones jugador-enemigo
    colisiones_jugador_enemigo = pygame.sprite.spritecollide(nave, enemigos, False)
    if colisiones_jugador_enemigo:
        vidas -= 1
        if vidas == 0:
            bucle_principal = False
            mostrar_texto("¡Game Over!", 400, 300, (255, 0, 0))
        else:
            for enemigo in colisiones_jugador_enemigo:
                enemigo.kill()  # Eliminar el enemigo que colisionó con la nave

    # Detectar colisiones enemigo-bala
    colisiones_enemigo_bala = pygame.sprite.groupcollide(enemigos, balas, True, True)
    if colisiones_enemigo_bala:
        for enemigo in colisiones_enemigo_bala:
            musica_explosion.play()
            puntuacion += 100
            crear_enemigos()

    # Dibujar elementos en la pantalla
    screen.blit(fondo, (0, 0))
    todos_los_sprites.draw(screen)

    # Mostrar puntuación y vidas
    mostrar_texto(f"Puntuación: {puntuacion}", 100, 10, (255, 255, 255))
    mostrar_texto(f"Vidas: {vidas}", 740, 10, (255, 255, 255))

    # Actualizar la pantalla y controlar FPS
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()