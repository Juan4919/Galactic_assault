import pytest, pygame
from pygame.sprite import Group
from app.game_objects import Jugador, Enemigo

# Fixture para jugador
@pytest.fixture
def jugador():
    return Jugador('app/images/jugador.png', (50, 50), 100, 100, 5)

# Fixture para enemigos
@pytest.fixture(params=['enemigo1.png', 'enemigo2.png', 'enemigo3.png', 'enemigo4.png'])
def enemigo(request):
    enemigos_rutas = {
        'enemigo1.png': 'app/images/enemigo1.png',
        'enemigo2.png': 'app/images/enemigo2.png',
        'enemigo3.png': 'app/images/enemigo3.png',
        'enemigo4.png': 'app/images/enemigo4.png'
    }
    imagen = enemigos_rutas[request.param]
    return Enemigo(100, 50, 50, 50, imagen)

def test_colision_jugador_enemigo(jugador, enemigo):
    grupo_enemigos = Group()
    grupo_enemigos.add(enemigo)
    
    # Mover enemigo a la posición del jugador para forzar una colisión
    enemigo.rect.x = jugador.rect.x
    enemigo.rect.y = jugador.rect.y
    
    assert pygame.sprite.spritecollide(jugador, grupo_enemigos, False), "Debe haber colisión entre jugador y enemigo"
