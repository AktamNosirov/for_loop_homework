def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    a='''"'''
    for i in range(0,n-1):
        a+=str(i)
        a=a+','
        continue
    a+=str(n-1) 
    a+='"'
    return a
print(main(12))