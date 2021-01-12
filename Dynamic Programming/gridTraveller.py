"""
This program tries to find how many ways to reach bottom right end 
from top left begin.
"""

#this approach is the naive one 
def gridTravellerEx(n,m):
    if n == 1 or m == 1:
        return 1

    return gridTravellerEx(n-1, m) + gridTravellerEx(n, m-1)

#print (gridTravellerEx(3,2)) 

#memo again
memo = dict()
def gridTravellerNew(n,m):
    if m > n:
        m ,n = n ,m  
    
    if m == 1 or n == 1:
        return 1
    
    if (n,m) in memo:
        return memo[(n,m)]
    
    a = gridTravellerNew(n-1, m) + gridTravellerNew(n, m-1)
    memo[(n,m)] = a
    return a 

print(gridTravellerNew(18,18))

#tabulation 
def gridTravellerTab(n,m):
    myarray = list()
    for i in range(n+1):
        myline = []
        for k in range(m+1):
            myline.append(0)
        myarray.append(myline)

    if n > 1 and m > 1: 
        myarray[1][1] = 1

    for i in range(n+1):
        for k in range(m+1):
            if i-1 >= 0:
                myarray[i][k] += myarray[i-1][k]
            if k-1 >= 0:
                myarray[i][k] += myarray[i][k-1]

    return myarray[n][m]

print(gridTravellerTab(3,3))