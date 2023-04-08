from hello import hello

def test_hello():
    assert hello("Bob") == "hello, Bob"


def test_default():
    assert hello() == "hello, world"
