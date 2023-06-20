def main(a,b,c):
    """
    Find number of negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    n=0
    if a<0:
        n=n+ 1
    if b<0:
        n=n+ 1
    if c<0:
        n=n+ 1
    return n 

print(main(-13,-17,-14))