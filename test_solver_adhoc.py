from math_doc_tool.core import ExtractedItem
from math_doc_tool.solver import MathSolver

def test_solver():
    print("Testing MathSolver...")
    solver = MathSolver()
    
    # Test case 1: Derivative
    item1 = ExtractedItem(
        item_type="Example",
        category="Solution",
        content="Example 1: Find the derivative of x**2"
    )
    result1 = solver.solve(item1)
    print(f"Input: {item1.content}")
    print(f"Result: {result1}")
    
    # Test case 2: Integral
    item2 = ExtractedItem(
        item_type="Exercise",
        category="Solution",
        content="Exercise: Calculate the integral of 2*x"
    )
    result2 = solver.solve(item2)
    print(f"Input: {item2.content}")
    print(f"Result: {result2}")

    # Test case 3: Failure case
    item3 = ExtractedItem(
        item_type="Text",
        category="Law",
        content="This is just some text."
    )
    result3 = solver.solve(item3)
    print(f"Input: {item3.content}")
    print(f"Result: {result3}")

if __name__ == "__main__":
    test_solver()
