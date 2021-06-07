def binary_search(alist, item):
    if not alist:  
        return False

    midpoint = len(alist) // 2
    if alist[midpoint] == item:  
        return True

    if item < alist[midpoint]:  
        return binary_search(alist[:midpoint], item)

   
    return binary_search(alist[midpoint + 1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]

print(binary_search(testlist, 13))  
print(binary_search(testlist, 3))  