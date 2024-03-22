# Brute Force
def subsetSums(arr, N):
    """
    Function to find all possible subset sums of a given array.
    
    Parameters:
    arr (list): The input array.
    N (int): The size of the array.

    Returns:
    list: A list of all possible subset sums.
    """
    def psum(arr, lis=[], idx=0):
        """
        Helper function to recursively find all subset sums.
        
        Parameters:
        arr (list): The input array.
        lis (list): The current subset.
        idx (int): The current index in the array.

        Returns:
        None
        """
        if lis:
            res.add(sum(lis[:]))
        if idx >= N:
            return
        lis.append(arr[idx])
        psum(arr, lis, idx+1)
        lis.pop()
        psum(arr, lis, idx+1)

    res = set({0})
    psum(arr)
    return list(res)



# Optimal

def subSum(arr, tot=0, idx=0):
    """
    This function calculates the sum of all possible subsets of the given array.
    
    Parameters:
    arr (list): The input list of numbers.
    tot (int): The total sum of the subset, initially set to 0.
    idx (int): The index of the current element in the array, initially set to 0.
    
    Returns:
    None: The function does not return any value. It appends the sum of each subset to the global list 'res'.
    """
    
    # Base case: if the current index is equal to the length of the array,
    # append the total sum to the global list 'res' and return
    if idx == len(arr): 
        res.append(tot)
        return
    
    # Recursive case 1: Include the current element in the total sum and move to the next element
    subSum(arr, tot+arr[idx], idx+1)

    # Recursive case 2: Exclude the current element from the total sum and move to the next element
    subSum(arr, tot, idx+1)

    
res = []
subSum([2, 5, 8, 11, 13] , )

print(sorted(res))