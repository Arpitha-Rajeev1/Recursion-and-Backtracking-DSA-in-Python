import sys
sys.setrecursionlimit(10 ** 8)


def subsets(s, o):
    if len(s) == 0:
        for value in o:
            print(value, end=' ')
        print()
        return

    subsets(s[1:], o)
    newOutput = o + [s[0]]
    subsets(s[1:], newOutput)


def takeInput():
    n = int(input().strip())

    if n == 0:
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n


def printListOfList(liOfLi):
    for li in liOfLi:
        for elem in li:
            print(elem, end=" ")
        print()


arr, n = takeInput()

if n != 0:
    subsets(arr, [])
