import calculator
import pytest

def test_add():
    assert calculator.calculate(2, 3, "add") == 5
def test_subtract():
    assert calculator.calculate(10, 3, "subtract") == 7
def test_multiply():
    assert calculator.calculate(3, 2, "multiply") == 6
def test_divide():
    assert calculator.calculate(6, 2, "divide") == 3
def test_divide_zero():
    with pytest.raises(ValueError):
        calculator.calculate(3, 0, "divide")
    # assert calculator.calculate(3, 0, "divide") == "Cannot divide by zero"

# Add more functional tests for subtract, multiply, and divide

def test_terminal_output(capsys):
    value = calculator.calculate(10, 2, "multiply")
    print('Result:', value)
    captured = capsys.readouterr()
    assert captured.out == "Result: 20\n"

def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3.0

# Add more tests to cover edge cases and negative scenarios



