Given an integer n, using phone keypad find out and return all the possible strings that can be made using digits of input n.
Note : The order of strings are not important.
Input Format :
Integer n
Output Format :
All possible strings in different lines
Constraints :
1 <= n <= 10^6
Sample Input:
23
Sample Output:
ad
ae
af
bd
be
bf
cd
ce
cf

def getString(d):
    if d == 2:
        return "abc"
    if d == 3:
        return "def"
    if d == 4:
        return "ghi"
    if d == 5:
        return "jkl"
    if d == 6:
        return "mno"
    if d == 7:
        return "pqrs"
    if d == 8:
        return "tuv"
    if d == 9:
        return "wxyz"
    return " "

def keypad(n):
    if n == 0:
        output = []
        output.append("")
        return output

    smallerNumber = n // 10
    lastDigit = n % 10

    smallerOutput = keypad(smallerNumber)
    optionsForLastDigit=getString(lastDigit)
    output = []

    for s in smallerOutput:
        for c in optionsForLastDigit:
            option = s + c
            output.append(option)
    return output

n = int(input())
ans = keypad(n)
for s in ans:
    print(s)

#print the minimum of the array instead of returning
def minList(lst):
    if len(lst) == 1:
        return lst[0]

    minSmallArray = minList(lst[1:])
    overallMin = min(minSmallArray, lst[0])
    return overallMin

def printMin(lst, minSoFar = 100000):
    if len(lst) == 0:
        print(minSoFar)
        return

    newMin = min(minSoFar, lst[0])
    printMin(lst[1:], newMin)
        
