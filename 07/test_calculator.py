import pytest
from calculator import addTwoNumbers, subtractTwoNumbers, multiplyTwoNumbers, divideTwoNumbers

def main():
    test_add()
    test_subtract()
    test_multiply()
    test_divide()

def test_add():
    assert addTwoNumbers(1, 2) == 3
    assert addTwoNumbers(0, 0) == 0
    assert addTwoNumbers(-1, -1) == -2

def test_subtract():
    assert subtractTwoNumbers(1, 2) == -1
    assert subtractTwoNumbers(0, 0) == 0
    assert subtractTwoNumbers(-1, -1) == 0

def test_multiply():
    assert multiplyTwoNumbers(1, 2) == 2
    assert multiplyTwoNumbers(0, 0) == 0
    assert multiplyTwoNumbers(-1, -1) == 1

def test_divide():
    assert divideTwoNumbers(1, 2) == 0.5
    # assert divideTwoNumbers(0, 0) == "undefined"
    assert divideTwoNumbers(-1, -1) == 1

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divideTwoNumbers(1, 0)

if __name__ == "__main__":
    main()
