def powerSet(s, curr='', idx=0, lis=[]):
    """
    Generates the power set of a given set.

    Parameters:
    s (str): The input set.
    curr (str): The current subset being generated (default is an empty string).
    idx (int): The current index in the input set (default is 0).
    lis (list): The list to store the subsets (default is an empty list).

    Returns:
    list: The power set of the input set.

    """
    if idx == len(s):
        return
    
    lis.append(curr)
    powerSet(s, curr, idx+1, lis)
    
    lis.append(curr+s[idx])
    powerSet(s, curr+s[idx], idx+1, lis)
    
    return list(set(lis))
print(powerSet('abcde'))

