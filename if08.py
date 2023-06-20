def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a>9 and a<100:
        if a>9 and a<100 and a % 2 == 0:
            "two-digit odd number"
        if a>9 and a<100 and a % 2 != 1:
            "two-digit ever number"
        if a>9 and a<1000 and a % 2 == 0:
            "three-digit odd number"
        if a>9 and a<1000 and a % 2 != 1:
            "three-digit odd number"
    return   "two-digit ever number"

print(main(132))
                    