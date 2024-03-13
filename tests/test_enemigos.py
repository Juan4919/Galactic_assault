import pytest
from app.game_objects import Enemigo

# Crear fixture para cada enemigo
@pytest.fixture
def enemigo1():
    return Enemigo(100, 100, 50, 50, 'app/images/enemigo1.png')

@pytest.fixture
def enemigo2():
    return Enemigo(150, 100, 50, 50, 'app/images/enemigo2.png')

@pytest.fixture
def enemigo3():
    return Enemigo(200, 100, 50, 50, 'app/images/enemigo3.png')

@pytest.fixture
def enemigo4():
    return Enemigo(250, 100, 50, 50, 'app/images/enemigo4.png')

# Test movimiento de cada enemigo
def test_movimiento_enemigo1(enemigo1):
    pos_original = enemigo1.rect.y
    enemigo1.update()
    assert enemigo1.rect.y > pos_original

def test_movimiento_enemigo2(enemigo2):
    pos_original = enemigo2.rect.y
    enemigo2.update()
    assert enemigo2.rect.y > pos_original

def test_movimiento_enemigo3(enemigo3):
    pos_original = enemigo3.rect.y
    enemigo3.update()
    assert enemigo3.rect.y > pos_original

def test_movimiento_enemigo4(enemigo4):
    pos_original = enemigo4.rect.y
    enemigo4.update()
    assert enemigo4.rect.y > pos_original
