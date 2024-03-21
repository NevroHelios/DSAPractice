def powerSet(s, curr='', idx=0, lis=[]):
    #code here
    if idx == len(s):
        return
    
    lis.append(curr)
    powerSet(s, curr, idx+1, lis)
    
    lis.append(curr+s[idx])
    powerSet(s, curr+s[idx], idx+1, lis)
    
    
    return list(set(lis))
    
print(powerSet('abcd'))

