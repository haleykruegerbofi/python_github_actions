"""
Unit tests for the Calculator module.

This test suite covers all methods and edge cases for the Calculator class.
"""

import pytest
from src.calculator import Calculator


class TestCalculator:
    """Test suite for the Calculator class."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(10, 20) == 30
        assert self.calc.add(0.5, 0.5) == 1.0
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert self.calc.add(-5, 3) == -2
        assert self.calc.add(-10, -20) == -30
        assert self.calc.add(-0.5, 0.5) == 0
    
    def test_add_type_error(self):
        """Test that add raises TypeError for non-numeric inputs."""
        with pytest.raises(TypeError):
            self.calc.add("2", 3)
        with pytest.raises(TypeError):
            self.calc.add(2, "3")
        with pytest.raises(TypeError):
            self.calc.add(None, 5)
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert self.calc.subtract(10, 5) == 5
        assert self.calc.subtract(20, 20) == 0
        assert self.calc.subtract(1.5, 0.5) == 1.0
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        assert self.calc.subtract(-5, -3) == -2
        assert self.calc.subtract(5, -3) == 8
        assert self.calc.subtract(-5, 3) == -8
    
    def test_subtract_type_error(self):
        """Test that subtract raises TypeError for non-numeric inputs."""
        with pytest.raises(TypeError):
            self.calc.subtract("10", 5)
        with pytest.raises(TypeError):
            self.calc.subtract(10, "5")
    
    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(5, 0) == 0
        assert self.calc.multiply(2.5, 2) == 5.0
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        assert self.calc.multiply(-3, 4) == -12
        assert self.calc.multiply(-3, -4) == 12
        assert self.calc.multiply(0, -5) == 0
    
    def test_multiply_type_error(self):
        """Test that multiply raises TypeError for non-numeric inputs."""
        with pytest.raises(TypeError):
            self.calc.multiply("3", 4)
        with pytest.raises(TypeError):
            self.calc.multiply(3, "4")
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(15, 3) == 5
        assert self.calc.divide(7, 2) == 3.5
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        assert self.calc.divide(-10, 2) == -5
        assert self.calc.divide(10, -2) == -5
        assert self.calc.divide(-10, -2) == 5
    
    def test_divide_by_zero(self):
        """Test that divide raises ValueError when dividing by zero."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
    
    def test_divide_type_error(self):
        """Test that divide raises TypeError for non-numeric inputs."""
        with pytest.raises(TypeError):
            self.calc.divide("10", 2)
        with pytest.raises(TypeError):
            self.calc.divide(10, "2")
    
    def test_history_recording(self):
        """Test that operations are recorded in history."""
        self.calc.add(2, 3)
        self.calc.subtract(10, 5)
        self.calc.multiply(3, 4)
        self.calc.divide(20, 4)
        
        history = self.calc.get_history()
        assert len(history) == 4
        assert "2 + 3 = 5" in history
        assert "10 - 5 = 5" in history
        assert "3 * 4 = 12" in history
        assert "20 / 4 = 5.0" in history
    
    def test_history_immutability(self):
        """Test that get_history returns a copy, not the original list."""
        self.calc.add(1, 1)
        history = self.calc.get_history()
        history.append("fake operation")
        
        assert len(self.calc.get_history()) == 1
        assert "fake operation" not in self.calc.get_history()
    
    def test_clear_history(self):
        """Test that clear_history removes all history."""
        self.calc.add(1, 1)
        self.calc.subtract(2, 1)
        assert len(self.calc.get_history()) == 2
        
        self.calc.clear_history()
        assert len(self.calc.get_history()) == 0
    
    def test_float_precision(self):
        """Test calculations with floating point numbers."""
        result = self.calc.add(0.1, 0.2)
        assert abs(result - 0.3) < 0.0001
        
        result = self.calc.multiply(0.1, 0.1)
        assert abs(result - 0.01) < 0.0001


def test_calculator_instantiation():
    """Test that Calculator can be instantiated."""
    calc = Calculator()
    assert isinstance(calc, Calculator)
    assert calc.history == [] 