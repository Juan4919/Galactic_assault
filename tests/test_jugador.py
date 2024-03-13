import pytest
from app.game_objects import Jugador

@pytest.fixture
def jugador():
    return Jugador('app/images/jugador.png', (50, 50), 100, 100, 5)

def test_movimiento_jugador(jugador):
    pos_original_x = jugador.rect.x
    jugador.rect.x += jugador.velocidad
    assert jugador.rect.x > pos_original_x
