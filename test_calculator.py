import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    print("Add test passed")

def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(1, 1) == 0
    print("Subtract test passed")

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(0, 5) == 0
    print("Multiply test passed")

def test_divide():
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(5, 2) == 2.5
    assert calculator.divide(1, 0) == "Error: Division by zero"
    print("Divide test passed")

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("All tests passed!")