def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    list=[]
    for i in range(0,len(list1)):
       list+= [list1[i].capitalize()]
    return list
print(main(["Anvar","bobur", "rustam"]))