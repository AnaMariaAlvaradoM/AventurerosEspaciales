import pygame
import random

class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("nave.png")
        self.rect = self.image.get_rect(center=(400, 550))
        self.velocidad = 5

    def mover_izquierda(self):
        if self.rect.left > 0:
            self.rect.move_ip(-self.velocidad, 0)

    def mover_derecha(self):
        if self.rect.right < 800:
            self.rect.move_ip(self.velocidad, 0)

    def disparar(self):
        bala = Bala(self.rect.centerx, self.rect.top)
        balas.add((bala,))

class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemigo.png")
        self.rect = self.image.get_rect(center=(random.randrange(0, 735), random.randrange(30, 150)))
        self.velocidad_y = 1

    def mover(self):
        self.rect.move_ip(0, self.velocidad_y)
        if self.rect.bottom > 600:
            self.rect.top = 30
            self.rect.x = random.randrange(0, 735)

class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bala.png")
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidad_y = -10
    def actualizar(self):
        self.rect.move_ip(0, self.velocidad_y)
        if self.rect.top < 0:
            self.kill()

todos_los_sprites = pygame.sprite.Group()            
balas = pygame.sprite.Group()           
enemigos = pygame.sprite.Group()
def crear_enemigo():
    nuevo_enemigo = Enemigo()
    enemigos.add(nuevo_enemigo)

def crear_enemigos():
    for _ in range(10):
        crear_enemigo()