#Recursive can sum program to check if we reach the target by summing up the numbers in the list.

memo = dict()
def canSumInner(target, nlist):
    if target in memo:
        return memo[target]

    if 0 == target:
        return True

    if 0 > target:
        return False
    
    for index in range(len(nlist)):
        if canSumInner(target - nlist[index] , nlist):
            memo[target] = True
            return True

    memo[target] = False
    return False

print(canSumInner(350, [7,14]))

def CanSumTab(target, nlist):
    mylist = list()
    for i in range(target+1):
        mylist.append(False)

    mylist[0] = True

    for i in range(len(mylist)):
        if mylist[i]:
            for num in nlist:
                if i + num < len(mylist):
                    mylist[i + num] = True

    return mylist[target]

print(CanSumTab(7, [2,3]))

 