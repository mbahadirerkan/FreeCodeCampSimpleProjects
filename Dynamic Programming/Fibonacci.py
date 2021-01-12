def fibonnaciEx(n):
    if n < 2:
        return 1
    
    return fibonnaciEx(n-1) + fibonnaciEx(n-2)

#cannot perform below with high speed
#print(fibonnaciEx(50))

#we have another approach:
memo = dict()
def fibonnaciNew(n):
    if n in memo:
        return memo[n]
    if n < 2:
        return 1 

    a = fibonnaciNew(n-1) + fibonnaciNew(n-2)
    memo[n] = a
    return a

print(fibonnaciNew(50))
print("Nail it")


def FibonacciTab(n):
    myarray = []
    for i in range(n+1):
        myarray.append(0)

    myarray[1] = 1

    for i in range(n-1):
        myarray[i+1] += myarray[i]
        myarray[i+2] += myarray[i]

    myarray[len(myarray) - 1] += myarray[len(myarray) - 2]

    print (myarray[n])

FibonacciTab(5)
    
