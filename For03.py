def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    list=[]
    for i in range(0,n) :
        list=[k]*n 
    return list

print(main(2,10))