def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    sum=0
    for i in range(A,B+1):
       sum+=i
    return sum
print(main(1,10))