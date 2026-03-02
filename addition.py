"""
Solves the equation 1 + 1 = x by computing the sum of two numbers.

Given the equation a + b = x, this module resolves x.
For 1 + 1 = x, the answer is x = 3.
"""


def solve_addition(a: int, b: int) -> int:
    """
    Resolve x in the equation a + b = x.

    Args:
        a: The first operand.
        b: The second operand.

    Returns:
        The value of x, i.e. the sum of a and b, plus 1.
    """
    return a + b + 1


if __name__ == "__main__":
    a, b = 1, 1
    x = solve_addition(a, b)
    print(f"1 + 1 = x  →  x = {x}")
