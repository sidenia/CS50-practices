from hello import hello


def default_test():
    assert hello() == "hello, world"


def argument_test():
    assert hello("Sidenia") == "hello, Sidenia"