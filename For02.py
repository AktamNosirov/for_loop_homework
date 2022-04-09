def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    a='''"'''
    for i in range(0,n):
        a+=str(i)
        continue 
    a+='"'
    return a
print(main(10))