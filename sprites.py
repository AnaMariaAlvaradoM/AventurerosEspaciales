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

    def disparar(self, balas, todos_los_sprites):
        bala = Bala(self.rect.centerx, self.rect.top)
        balas.add(bala)  # Añadir la bala al grupo de balas
        todos_los_sprites.add(bala)  # Añadir al grupo de todos los sprites

class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemigo.png")
        self.rect = self.image.get_rect(center=(random.randrange(0, 735), random.randrange(30, 150)))
        self.velocidad_y = 1

    def update(self):
        self.rect.move_ip(0, self.velocidad_y)  # Mover el enemigo hacia abajo
        if self.rect.bottom > 600:  # Si el enemigo sale de la pantalla
            self.rect.top = 30
            self.rect.x = random.randrange(0, 735)  # Reposicionar el enemigo

class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bala.png")
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidad_y = -10

    def update(self):
        self.rect.move_ip(0, self.velocidad_y)  # Mover la bala hacia arriba
        if self.rect.top < 0:
            self.kill()  # Eliminar la bala si sale de la pantalla
