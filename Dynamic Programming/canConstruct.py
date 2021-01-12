def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text  # or whatever

def canConstruct(target, mylist, memo = {}):
    if target == "":
        return True

    if target in memo:
        return memo[target]

    for prefix in mylist:
        if target.startswith(prefix):
            if canConstruct(remove_prefix(target, prefix), mylist):
                memo[target] = True
                return True


    memo[target] = False
    return False

print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeef", {"e","eeee", "eee", "eeeee"}))


def allConstruct(target, mylist, memo = {}):
    if target == "": return [[]]

    result = []

    for prefix in mylist:
        if target.startswith(prefix):
            the_ways = allConstruct(remove_prefix(target, prefix), mylist)

            target_ways = [[prefix ] + way for way in the_ways ]
            if target_ways:
                result.extend(target_ways )

    return result

print(allConstruct("purple" , {"purp", "p", "ur", "le", "purpl"}))


#tabulation 
def canConstructTab(target, mylist):
    mytable = list()

    for i in range(len(target) + 1):
        mytable.append(False)

    mytable[0] = True

    for i in range(len(target)):
        if mytable[i]:
            for word in mylist:
                if word.startswith(target[i: i+len(word)]):
                    if i + len(word) < len(mytable):
                        mytable[i+len(word)] = True


    return mytable[len(target)]

print(canConstructTab("eeeeeeeeeeeeeeeeeeeeeeeeeeeef", {"e","eeee", "eee", "eeeee"}))
