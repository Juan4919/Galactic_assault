import pytest
from app.game_objects import Proyectil

@pytest.fixture
def proyectil():
    return Proyectil('app/images/bala.png', (10, 10), 100, 100)

def test_movimiento_proyectil(proyectil):
    pos_original_y = proyectil.rect.y
    proyectil.rect.y -= 5 
    assert proyectil.rect.y < pos_original_y
