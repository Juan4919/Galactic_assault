import random
import pygame
import sys
import time
from app.game_objects import Jugador, Enemigo, Proyectil
from app.utils import reiniciar_juego

# Iniciar Pygame
pygame.init()

# Configuración del tamaño y velocidad del juego
ANCHO, ALTO = 1920, 1080
FPS = 60

# Configuración de la ventana de juego
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Naves Espaciales")

# Cargar fondo de pantalla
fondo = pygame.image.load("app/images/fondo.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Configuración inicial de la pantalla
mostrar_pantalla_inicial = True
temporizador_parpadear = 0
parpadear = False

# Configuración tipo de letra para el título
fuente_titulo = pygame.font.Font("app/fonts/fuente_pixel.ttf", 180)  
texto_titulo = fuente_titulo.render("Galactic Assault", True, (248, 0, 0))
rect_titulo = texto_titulo.get_rect(center=(ANCHO // 2, ALTO // 2 - 50))

# Configuración tipo de letra para el mensaje parpadeante
fuente_mensaje = pygame.font.Font("app/fonts/fuente_pixel.ttf", 36)  
texto_mensaje = fuente_mensaje.render("Pulsa ENTER para iniciar el juego", True, (248, 0, 0))
rect_mensaje = texto_mensaje.get_rect(center=(ANCHO // 2, ALTO // 1.2 + 50))

# Posición vertical del fondo
fondo_y1 = 0
fondo_y2 = -ALTO 

# Factor para ajustar velocidad del fondo en relación con la velocidad de los enemigos
factor_velocidad_fondo = 1.0 

# Cargar imágenes
jugador = pygame.image.load("app/images/jugador.png")
jugador = pygame.transform.scale(jugador, (50, 50))

nave_enemiga1 = pygame.image.load("app/images/enemigo1.png")
nave_enemiga1 = pygame.transform.scale(nave_enemiga1, (40, 40))

nave_enemiga2 = pygame.image.load("app/images/enemigo2.png")
nave_enemiga2 = pygame.transform.scale(nave_enemiga2, (25, 25))

nave_enemiga3 = pygame.image.load("app/images/enemigo3.png")
nave_enemiga3 = pygame.transform.scale(nave_enemiga3, (30, 30))

nave_enemiga4 = pygame.image.load("app/images/enemigo4.png")
nave_enemiga4 = pygame.transform.scale(nave_enemiga4, (35, 35))

# Lista de enemigos 
tipos_enemigos = [nave_enemiga1, nave_enemiga2, nave_enemiga3, nave_enemiga4]

# Configuración de la bala
bala_img = pygame.image.load("app/images/bala.png")
bala_img = pygame.transform.scale(bala_img, (10, 20))

# Inicialización de variables y objetos del juego
jugador_x = (ANCHO - jugador.get_width()) // 2
jugador_y = ALTO - jugador.get_height() - 10
velocidad_jugador = 8
direccion_jugador = "derecha"
velocidad_jugador_y = 3  
velocidad_jugador_y = 3

enemigos = []
velocidad_enemigo = 2
retraso_aparicion = 10
contador_aparicion = 0

balas = []
velocidad_bala = 10

tiempo_inicio = time.time()
duracion_juego = 60
enemigos_eliminados = 0

reloj = pygame.time.Clock()

# Función para reiniciar el juego
def reiniciar_juego():
    global jugador_x, jugador_y, enemigos, enemigos_eliminados, tiempo_inicio
    jugador_x = (ANCHO - jugador.get_width()) // 2
    jugador_y = ALTO - jugador.get_height() - 20
    enemigos = []
    enemigos_eliminados = 0
    tiempo_inicio = time.time()

# Variables de control del juego
juego_terminado = False
temporizador_fin_juego = 0

# Temporizador para controlar los cambios cada X segundos
temporizador_cambios = 0
cada_cuanto_cambios = 0.5

retraso_aparicion_minimo = 10

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Verificar si se debe mostrar la pantalla inicial
    if mostrar_pantalla_inicial:
        pantalla.blit(fondo, (0, 0))

        # Cambiar el estado de parpadeo cada 30 frames
        temporizador_parpadear += 1
        if temporizador_parpadear % 30 == 0:
            parpadear = not parpadear

        pantalla.blit(texto_titulo, rect_titulo)
        if parpadear:
            pantalla.blit(texto_mensaje, rect_mensaje)

        pygame.display.flip()

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RETURN]:
            mostrar_pantalla_inicial = False

    else:
        fondo_y1 += velocidad_jugador_y * factor_velocidad_fondo
        fondo_y2 += velocidad_jugador_y * factor_velocidad_fondo

        if fondo_y1 > ALTO:
            fondo_y1 = -ALTO

        if fondo_y2 > ALTO:
            fondo_y2 = -ALTO

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jugador_x > 0:
            jugador_x -= velocidad_jugador
            direccion_jugador = "izquierda"
        if teclas[pygame.K_RIGHT] and jugador_x < ANCHO - jugador.get_width():
            jugador_x += velocidad_jugador
            direccion_jugador = "derecha"

        if teclas[pygame.K_SPACE]:
            if time.time() - balas[-1][2] >= 0.2 if balas else True:
                balas.append([jugador_x + jugador.get_width() // 2 - bala_img.get_width() // 2, jugador_y, time.time()])

        for bala in balas[:]:
            for enemigo in enemigos:
                if (
                    bala[0] < enemigo[0] + enemigo[2]
                    and bala[0] + bala_img.get_width() > enemigo[0]
                    and bala[1] < enemigo[1] + enemigo[3]
                    and bala[1] + bala_img.get_height() > enemigo[1]
                ):
                    enemigos.remove(enemigo)
                    balas.remove(bala)
                    enemigos_eliminados += 1
                    break

        for enemigo in enemigos:
            enemigo[1] += velocidad_enemigo * (1 + enemigo[4] / 100)

        contador_aparicion += 2
        if contador_aparicion == retraso_aparicion:
            tipo_enemigo = random.choice(tipos_enemigos)
            enemigos.append([random.randint(0, ANCHO - tipo_enemigo.get_width()), 0, tipo_enemigo.get_width(), tipo_enemigo.get_height(), random.randint(0, 20)])
            contador_aparicion = 0

        retraso_aparicion = max(retraso_aparicion, retraso_aparicion_minimo)

        balas = [[bx, by - velocidad_bala, bt] for bx, by, bt in balas if by > 0]
        balas = [[bx, by, bt] for bx, by, bt in balas if by > 0 and by < ALTO]

        temporizador_cambios += 1
        if temporizador_cambios % FPS == 0:
            if temporizador_cambios // FPS % cada_cuanto_cambios == 0:
                velocidad_enemigo *= 1.03
                retraso_aparicion = int(retraso_aparicion * 1)
                factor_velocidad_fondo *= 1.01

        pantalla.blit(fondo, (0, fondo_y1))
        pantalla.blit(fondo, (0, fondo_y2))

        if direccion_jugador == "izquierda":
            pantalla.blit(jugador, (jugador_x, jugador_y))
        elif direccion_jugador == "derecha":
            pantalla.blit(jugador, (jugador_x, jugador_y))

        for enemigo in enemigos:
            pantalla.blit(tipos_enemigos[enemigo[4] % len(tipos_enemigos)], (enemigo[0], enemigo[1]))

        for bala in balas:
            pantalla.blit(bala_img, (bala[0], bala[1]))

        tiempo_transcurrido = int(duracion_juego - (time.time() - tiempo_inicio))
        fuente = pygame.font.Font(None, 36)
        texto_tiempo = fuente.render(f"Tiempo: {tiempo_transcurrido}s", True, (248, 0, 0))
        pantalla.blit(texto_tiempo, (10, 10))

        texto_enemigos_eliminados = fuente.render(f"Enemigos eliminados: {enemigos_eliminados}", True, (248, 0, 0))
        pantalla.blit(texto_enemigos_eliminados, (ANCHO - 305, 10))

        for enemigo in enemigos:
            if (
                jugador_x < enemigo[0] + enemigo[2]
                and jugador_x + jugador.get_width() > enemigo[0]
                and jugador_y < enemigo[1] + enemigo[3]
                and jugador_y + jugador.get_height() > enemigo[1]
            ):
                juego_terminado = True

        if tiempo_transcurrido <= 0 or juego_terminado:
            if tiempo_transcurrido <= 0:
                texto_victoria = fuente.render(f"¡Victoria! Has completado el tiempo y eliminado {enemigos_eliminados} enemigos", True, (0, 255, 0))
            else:
                texto_victoria = fuente.render(f"Game Over, has eliminado {enemigos_eliminados} enemigos", True, (255, 0, 0))

            pantalla.blit(texto_victoria, ((ANCHO - texto_victoria.get_width()) // 2, (ALTO - texto_victoria.get_height()) // 2))

            fuente_instrucciones = pygame.font.Font(None, 24)
            texto_instrucciones = fuente_instrucciones.render("Para reiniciar el juego, pulsa ENTER", True, (255, 255, 255))
            pantalla.blit(texto_instrucciones, ((ANCHO - texto_instrucciones.get_width()) // 2, ALTO - 30))

            pygame.display.flip()

            esperando_enter = True
            while esperando_enter:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                        reiniciar_juego()

                        juego_terminado = False
                        esperando_enter = False

        pygame.display.flip()

    reloj.tick(FPS)
