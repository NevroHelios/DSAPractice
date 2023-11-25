# Amaazon (Medium)
#GfG
def shuffleArray( arr:list, n):
        # Your code goes here
        for i in range(int(n/2)):
            arr.insert(2 *i + 1, arr[i + int(n/2)])
            del arr[i + int(n/2) + 1]
        return arr

arr = [5, 9, 7, 7, 9, 6, 8, 9, 10, 1]

print(shuffleArray(arr, len(arr)))  #[5, 6, 9, 8, 7, 9, 7, 10, 9, 1]