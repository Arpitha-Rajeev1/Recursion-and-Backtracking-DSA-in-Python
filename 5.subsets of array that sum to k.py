import sys
sys.setrecursionlimit(10 ** 8)

def subsets(arr, si, k, v=[]):
    if k == 0:
        for value in v:
            print(value, end=' ')
        print()
        return

    if si == len(arr):
        return

    subsets(arr, si+1, k, v)
    v1 = [] + v
    v1.append(arr[si])
    subsets(arr, si+1, k-arr[si], v1)

def takeInput() :
    n = int(input().strip())

    if n == 0 :
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n


#printing the list of lists
def printListOfList(liOfLi) :
    for li in liOfLi :
        for elem in li :
            print(elem, end = " ")
        print()

#main
arr, n = takeInput()

if n != 0 :
    k = int(input().strip())
    subsetsSumK(arr, 0, k)

    # printListOfList(subsetsSumK(arr, 0, k))
