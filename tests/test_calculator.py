"""
Unit tests for the Calculator module.

This test suite demonstrates a simple test for the CI/CD pipeline.
"""

from src.calculator import Calculator, main


def test_simple_addition():
    """Test that the calculator can add two numbers."""
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5
    assert calc.get_history() == ["2 + 3 = 5"]


def test_main_function(capsys):
    """Test the main function runs without errors."""
    main()
    captured = capsys.readouterr()
    assert "Simple Calculator Demo" in captured.out
    assert "10 + 5 = 15" in captured.out
