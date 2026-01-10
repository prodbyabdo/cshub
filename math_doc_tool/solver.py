try:
    from sympy import sympify, diff, integrate, solve, simplify, Symbol
    from sympy.parsing.latex import parse_latex # Optional, might require antlr4
    SYMPY_AVAILABLE = True
except ImportError:
    SYMPY_AVAILABLE = False

import re
from typing import Optional
from .core import ExtractedItem

class MathSolver:
    """
    Attempts to solve math exercises extracted from text.
    Uses heuristic pattern matching to determine the operation (derivative, integral, solve).
    """
    
    def __init__(self):
        if not SYMPY_AVAILABLE:
            print("Warning: SymPy not installed. Solver will not work.")

    def solve(self, item: ExtractedItem) -> Optional[str]:
        """
        Main entry point. Returns a string description of the solution or None if failed.
        """
        if not SYMPY_AVAILABLE:
            return None
            
        # We process the 'Statement' content usually
        text = item.content.lower().replace('\n', ' ')
        
        # 1. Check for Derivatives
        # Patterns like "find the derivative of x^2" or "differentiate sin(x)"
        diff_match = re.search(r'(derivative of|differentiate|find y\'|find f\'\(x\))\s+(.*)', text)
        if diff_match:
            expr_str = self._clean_expression(diff_match.group(2))
            return self._solve_derivative(expr_str)

        # 2. Check for Integrals
        # Patterns like "find the integral of..." or "evaluate \int ..."
        int_match = re.search(r'(integral of|integrate|evaluate)\s+(.*)', text)
        if int_match:
            expr_str = self._clean_expression(int_match.group(2))
            return self._solve_integral(expr_str)

        return None

    def _clean_expression(self, text: str) -> str:
        """
        Heuristic cleanup to isolate the math expression from trailing punctuation/words.
        Stop at common end-of-sentence markers or connection words.
        """
        # Stop at: . , with where using
        text = re.split(r'[\.,]| with | where | using ', text)[0]
        return text.strip()

    def _solve_derivative(self, expr_str: str) -> str:
        try:
            x = Symbol('x')
            # Handle some basic latex replacements if raw sympify fails
            # e.g. \sin(x) -> sin(x)
            clean_expr = expr_str.replace('\\', '') 
            
            expr = sympify(clean_expr)
            result = diff(expr, x)
            return f"**Computed Derivative**: d/dx ({clean_expr}) = {result}"
        except Exception as e:
            return f"Error computing derivative for '{expr_str}': {e}"

    def _solve_integral(self, expr_str: str) -> str:
        try:
            x = Symbol('x')
            clean_expr = expr_str.replace('\\', '')
            
            expr = sympify(clean_expr)
            result = integrate(expr, x)
            return f"**Computed Integral**: ∫ ({clean_expr}) dx = {result} + C"
        except Exception as e:
            return f"Error computing integral for '{expr_str}': {e}"
