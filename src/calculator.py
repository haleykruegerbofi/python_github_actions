"""
Simple Calculator Module

This module demonstrates basic arithmetic operations for the CI/CD pipeline example.
It follows SDLC naming conventions and includes comprehensive docstrings.
"""

from typing import List, Union


class Calculator:
    """A simple calculator class for basic arithmetic operations."""

    def __init__(self) -> None:
        """Initialize the calculator with a history of operations."""
        self.history: List[str] = []

    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Add two numbers together.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def get_history(self) -> List[str]:
        """Get the history of all operations."""
        return self.history.copy()


def main() -> None:
    """Example usage of the Calculator class."""
    calc = Calculator()

    print("Simple Calculator Demo")
    print("=" * 30)

    # Demonstrate a simple addition
    result = calc.add(10, 5)
    print(f"10 + 5 = {result}")


if __name__ == "__main__":
    main()
