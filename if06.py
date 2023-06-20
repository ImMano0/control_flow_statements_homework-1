def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    if a>0:
        positive = positive + 1
    if b>0:
        positive = positive + 1
    if c>0:
        positive = positive + 1
    if a>0:
        negative = negative + 1
    if b>0:
        negative = negative + 1
    if c>0:
        negative = negative + 1
    if positive > negative :
    return  "there are a lot of positive numbers"

print(main(4,5,8))