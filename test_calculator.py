from calculator import Calculator

class TestCalculator:
    def test_sum(self):
        calc = Calculator(1, 2)
        assert calc.sum() == 3