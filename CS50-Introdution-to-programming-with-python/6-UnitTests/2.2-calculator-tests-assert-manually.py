from calculator import square

def test_square(): 
    try:
        assert square(2) == 4
    except AssertionError:
        print("test_square() failed: 3 squared is not 9")
    try:
        assert square(3) == 9
    except AssertionError:
        print("test_square() failed: 3 squared is not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("test_square() failed: -2 squared is not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("test_square() failed: -3 squared is not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("test_square() failed: 0 squared is not 0")



if __name__ == '__main__':
    test_square()