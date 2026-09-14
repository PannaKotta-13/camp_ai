from src.q_08.main import A


def test_init():
    assert A.x + A.y == 3

def test_2():
    assert A.x - A.y == -1