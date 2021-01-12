### Brute-Force implementation of mine. 
def howSum(target, numbers):
    if target < 0 : return None
    if target == 0: return []

    for num in numbers:
        if (howSum(target-num, numbers)) != None:
            return howSum(target-num, numbers) + [num]
    
    return None

print(howSum(7, {2,3}))
 

### Memoized implementation of mine. 
def howSumMemo(target, numbers, memo = {} ):
    numbers.sort()
    if target == 0: return [] 
    if target < 0: return None
    if target in memo: return memo[target]

    shortest = None

    for num in numbers:
        if howSumMemo(target - num, numbers, memo) != None:
            memo[target] = howSumMemo(target-num, numbers, memo) + [num]
            if shortest == None or len(memo[target]) < len(shortest):
                shortest = memo[target]            

    return shortest

print(howSumMemo(86, [25,12,1]))


### tabulation
def howSumTab(target, numbers):
    mytable = list()

    for i in range(target + 1):
        mytable.append(None)

    mytable[0] = []

    for i in range(target):
        if mytable[i] != None:
            for num in numbers:
                if i + num < len(mytable):
                    mytable[i+num] = mytable[i] + [num] 

    return mytable[target]

print(howSumTab(300, {7,15}))    

