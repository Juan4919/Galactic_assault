import pygame
import sys
import sqlite3
import time
import random

# Función para ingresar nombre en la BBDD    
def ingresar_nombre(pantalla, reloj, FPS, ANCHO, ALTO):
    nombre = ""
    ingresando_nombre = True

    fuente_nombre = pygame.font.Font("app/fonts/fuente_pixel.ttf", 40)
    fuente_mensaje = pygame.font.Font("app/fonts/fuente_pixel.ttf", 24)
    fuente_fin = pygame.font.Font("app/fonts/fuente_pixel.ttf", 100)

    while ingresando_nombre:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nombre:
                    ingresando_nombre = False
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += evento.unicode

        pantalla.fill((0, 0, 0))

        mensaje_fin_partida = "¡Fin de la partida!"
        color_fin_partida = (255, 0, 0)  
        texto_fin_partida = fuente_fin.render(mensaje_fin_partida, True, color_fin_partida)
        pantalla.blit(texto_fin_partida, ((ANCHO - texto_fin_partida.get_width()) // 2, (ALTO - texto_fin_partida.get_height()) // 4))

        texto_nombre = fuente_nombre.render(f"Ingresa tu nombre para registrar el resultado: {nombre}", True, (255, 255, 255))
        pantalla.blit(texto_nombre, ((ANCHO - texto_nombre.get_width()) // 2, (ALTO - texto_nombre.get_height()) // 2))

        texto_mensaje = fuente_mensaje.render("Pulsa ENTER para aceptar", True, (255, 255, 255))
        pantalla.blit(texto_mensaje, ((ANCHO - texto_mensaje.get_width()) // 2, ALTO - 50))

        pygame.display.flip()
        reloj.tick(FPS)

    return nombre

# Función para mostrar mejores resultados   
def mostrar_resultados(pantalla, reloj, FPS, ANCHO, ALTO):
    conexion = sqlite3.connect("data/partidas.db")
    cursor = conexion.cursor()

    # Obtener resultados de la base de datos
    cursor.execute('''
        SELECT nombre, enemigos_eliminados, tiempo_transcurrido
        FROM resultados
        ORDER BY enemigos_eliminados DESC, tiempo_transcurrido ASC
        LIMIT 20
    ''')
    resultados = cursor.fetchall()

    fuente_titulo = pygame.font.Font("app/fonts/fuente_pixel.ttf", 50)
    fuente_resultados = pygame.font.Font("app/fonts/fuente_pixel.ttf", 26)

    pantalla.fill((0, 0, 0))

    texto_titulo = fuente_titulo.render("Mejores resultados:", True, (255, 255, 255))
    pantalla.blit(texto_titulo, ((ANCHO - texto_titulo.get_width()) // 2, 50))

    y_offset = 120
    contador = 1  
    for resultado in resultados:
        texto_resultado = fuente_resultados.render(f"{contador} - {resultado[0]} - Enemigos: {resultado[1]}, Tiempo: {resultado[2]}s", True, (255, 255, 255))
        pantalla.blit(texto_resultado, ((ANCHO - texto_resultado.get_width()) // 2, y_offset))
        y_offset += 40
        contador += 1 

    texto_instrucciones = fuente_resultados.render("Pulsa ENTER para jugar de nuevo o ESC para salir", True, (255, 255, 255))
    pantalla.blit(texto_instrucciones, ((ANCHO - texto_instrucciones.get_width()) // 2, ALTO - 50))

    pygame.display.flip()

    conexion.close()
