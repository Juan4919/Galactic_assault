import pygame
import random

# Clase del jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self, imagen, escala, x, y, velocidad):
        # Constructor del jugador
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.image = pygame.transform.scale(self.image, escala)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = velocidad
        self.direccion = "derecha"

# Clase de los enemigos
class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, imagen):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += self.velocidad
        self.indice_imagen = (self.indice_imagen + 1) % len(self.imagenes)
        self.image = self.imagenes[self.indice_imagen]

# Clase para el proyectil
class Proyectil(pygame.sprite.Sprite):
    def __init__(self, imagen, escala, x, y):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.image = pygame.transform.scale(self.image, escala)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
