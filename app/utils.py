import pygame
import sys
import time
import random

# Función para reiniciar el juego
def reiniciar_juego(ANCHO, ALTO, jugador):
    global jugador_x, jugador_y, enemigos, enemigos_eliminados, tiempo_inicio
    jugador_x = (ANCHO - jugador.get_width()) // 2
    jugador_y = ALTO - jugador.get_height() - 20
    enemigos = []
    enemigos_eliminados = 0
    tiempo_inicio = time.time()