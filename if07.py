def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a>0 and a%2 == 1: 
        "positive odd number"
    if a>0 and a%2 ==  1:
        "positive ever number"
    if a>0 and a%2 ==  0:
        "negative odd number"
    if a>0 and a%2 ==  0:
        "negative ever number"
    if a==0:
        "the number is zero" 
    return "the number is zero"

print(main(2))