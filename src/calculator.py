"""
Simple Calculator Module

This module demonstrates basic arithmetic operations for the CI/CD pipeline example.
It follows SDLC naming conventions and includes comprehensive docstrings.
"""

from typing import Union


class Calculator:
    """A simple calculator class for basic arithmetic operations."""
    
    def __init__(self):
        """Initialize the calculator with a history of operations."""
        self.history = []
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Add two numbers together.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
            
        Raises:
            TypeError: If inputs are not numeric
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numeric")
        
        result = a + b
        self._record_operation(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Subtract b from a.
        
        Args:
            a: Number to subtract from
            b: Number to subtract
            
        Returns:
            Difference of a and b
            
        Raises:
            TypeError: If inputs are not numeric
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numeric")
        
        result = a - b
        self._record_operation(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
            
        Raises:
            TypeError: If inputs are not numeric
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numeric")
        
        result = a * b
        self._record_operation(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Divide a by b.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            Quotient of a and b
            
        Raises:
            TypeError: If inputs are not numeric
            ValueError: If b is zero
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numeric")
        
        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        result = a / b
        self._record_operation(f"{a} / {b} = {result}")
        return result
    
    def _record_operation(self, operation: str) -> None:
        """Record an operation in the history."""
        self.history.append(operation)
    
    def get_history(self) -> list:
        """Get the history of all operations."""
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear the operation history."""
        self.history.clear()


def main():
    """Example usage of the Calculator class."""
    calc = Calculator()
    
    print("Simple Calculator Demo")
    print("=" * 30)
    
    # Demonstrate operations
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"20 - 8 = {calc.subtract(20, 8)}")
    print(f"7 * 6 = {calc.multiply(7, 6)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    
    print("\nOperation History:")
    for operation in calc.get_history():
        print(f"  - {operation}")


if __name__ == "__main__":
    main() 