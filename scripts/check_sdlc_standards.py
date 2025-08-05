#!/usr/bin/env python3
"""
SDLC Standards Checker

This script validates code against organizational SDLC standards including:
- Naming conventions
- File structure
- Documentation requirements
- Code complexity limits
"""

import os
import sys
import re
import ast
from pathlib import Path
from typing import List, Tuple, Dict


class SDLCChecker:
    """Check code compliance with SDLC standards."""
    
    def __init__(self, root_path: str = "."):
        """Initialize the checker with the project root path."""
        self.root_path = Path(root_path)
        self.errors: List[str] = []
        self.warnings: List[str] = []
        
    def check_all(self) -> Tuple[List[str], List[str]]:
        """Run all SDLC checks and return errors and warnings."""
        self.check_file_naming()
        self.check_module_structure()
        self.check_function_naming()
        self.check_docstrings()
        self.check_complexity()
        self.check_imports()
        
        return self.errors, self.warnings
    
    def check_file_naming(self) -> None:
        """Check that Python files follow naming conventions."""
        for py_file in self.root_path.rglob("*.py"):
            # Skip virtual environment and other common directories
            if any(part in py_file.parts for part in ['venv', '.venv', 'env', '__pycache__', '.git']):
                continue
            if py_file.is_file():
                filename = py_file.stem
                
                # Skip __init__ files
                if filename == "__init__":
                    continue
                
                # Check for snake_case
                if not re.match(r'^[a-z][a-z0-9_]*$', filename):
                    self.errors.append(
                        f"File '{py_file}' does not follow snake_case naming convention"
                    )
                
                # Check for no leading underscores (except for private modules)
                if filename.startswith('_') and not filename.startswith('__'):
                    self.warnings.append(
                        f"File '{py_file}' starts with underscore (consider making it public)"
                    )
    
    def check_module_structure(self) -> None:
        """Check that modules have proper structure."""
        src_path = self.root_path / "src"
        if not src_path.exists():
            self.errors.append("Missing 'src' directory for source code")
            return
        
        # Check for __init__.py files
        for dir_path in src_path.rglob("**/"):
            if dir_path.is_dir() and dir_path != src_path:
                init_file = dir_path / "__init__.py"
                if not init_file.exists():
                    self.warnings.append(
                        f"Directory '{dir_path}' missing __init__.py file"
                    )
    
    def check_function_naming(self) -> None:
        """Check that functions and classes follow naming conventions."""
        for py_file in self.root_path.rglob("*.py"):
            # Skip virtual environment and other common directories
            if any(part in py_file.parts for part in ['venv', '.venv', 'env', '__pycache__', '.git']):
                continue
            if not py_file.is_file():
                continue
                
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    tree = ast.parse(f.read())
                
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        # Check function names are snake_case
                        if not re.match(r'^[a-z_][a-z0-9_]*$', node.name):
                            self.errors.append(
                                f"Function '{node.name}' in '{py_file}' "
                                f"does not follow snake_case convention"
                            )
                    
                    elif isinstance(node, ast.ClassDef):
                        # Check class names are PascalCase
                        if not re.match(r'^[A-Z][a-zA-Z0-9]*$', node.name):
                            self.errors.append(
                                f"Class '{node.name}' in '{py_file}' "
                                f"does not follow PascalCase convention"
                            )
            
            except Exception as e:
                self.warnings.append(f"Could not parse '{py_file}': {e}")
    
    def check_docstrings(self) -> None:
        """Check that all public functions and classes have docstrings."""
        for py_file in self.root_path.rglob("*.py"):
            # Skip virtual environment and other common directories
            if any(part in py_file.parts for part in ['venv', '.venv', 'env', '__pycache__', '.git']):
                continue
            if not py_file.is_file():
                continue
                
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    tree = ast.parse(f.read())
                
                # Check module docstring
                if not ast.get_docstring(tree):
                    self.warnings.append(f"Module '{py_file}' missing docstring")
                
                for node in ast.walk(tree):
                    if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                        # Skip private methods
                        if node.name.startswith('_') and not node.name.startswith('__'):
                            continue
                        
                        if not ast.get_docstring(node):
                            node_type = "Function" if isinstance(node, ast.FunctionDef) else "Class"
                            self.errors.append(
                                f"{node_type} '{node.name}' in '{py_file}' missing docstring"
                            )
            
            except Exception as e:
                self.warnings.append(f"Could not parse '{py_file}': {e}")
    
    def check_complexity(self) -> None:
        """Check code complexity metrics."""
        max_function_lines = 50
        max_file_lines = 500
        
        for py_file in self.root_path.rglob("*.py"):
            # Skip virtual environment and other common directories
            if any(part in py_file.parts for part in ['venv', '.venv', 'env', '__pycache__', '.git']):
                continue
            if not py_file.is_file():
                continue
            
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.split('\n')
                
                # Check file length
                if len(lines) > max_file_lines:
                    self.warnings.append(
                        f"File '{py_file}' has {len(lines)} lines "
                        f"(exceeds recommended {max_file_lines})"
                    )
                
                # Check function length
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        func_lines = node.end_lineno - node.lineno + 1
                        if func_lines > max_function_lines:
                            self.warnings.append(
                                f"Function '{node.name}' in '{py_file}' "
                                f"has {func_lines} lines (exceeds recommended {max_function_lines})"
                            )
            
            except Exception as e:
                self.warnings.append(f"Could not analyze '{py_file}': {e}")
    
    def check_imports(self) -> None:
        """Check import organization and style."""
        for py_file in self.root_path.rglob("*.py"):
            # Skip virtual environment and other common directories
            if any(part in py_file.parts for part in ['venv', '.venv', 'env', '__pycache__', '.git']):
                continue
            if not py_file.is_file():
                continue
            
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    tree = ast.parse(f.read())
                
                imports = []
                for node in ast.walk(tree):
                    if isinstance(node, (ast.Import, ast.ImportFrom)):
                        imports.append(node)
                
                # Check for wildcard imports
                for imp in imports:
                    if isinstance(imp, ast.ImportFrom):
                        for alias in imp.names:
                            if alias.name == '*':
                                self.errors.append(
                                    f"Wildcard import found in '{py_file}': "
                                    f"from {imp.module} import *"
                                )
            
            except Exception as e:
                self.warnings.append(f"Could not check imports in '{py_file}': {e}")


def main():
    """Run SDLC standards check."""
    print("Running SDLC Standards Check...")
    print("=" * 60)
    
    checker = SDLCChecker()
    errors, warnings = checker.check_all()
    
    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"  ⚠️  {warning}")
    
    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"  ❌ {error}")
        print(f"\nFound {len(errors)} errors and {len(warnings)} warnings")
        sys.exit(1)
    else:
        print("✅ All SDLC standards checks passed!")
        if warnings:
            print(f"   (with {len(warnings)} warnings)")
        sys.exit(0)


if __name__ == "__main__":
    main() 