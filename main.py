'''The function accepts the string n. It checks whether the number is an autobiographical number or not. If an integer returns, then it is an autobiographical number. If 0 returns, then it is not an autobiographical number.
Assumption
The input value should not be more than 10 characters.
The input string will have numeric characters.
Example
Input:
N: “1210”
Output:
3
Explanation
The 0th position has the number 1, the 1st position has the number 2, the 2nd position has the number 1, and the 3rd position has number 0. Hence, it is an autobiographical number.'''
def AutoCount(n):
    l = len(str(n))
    sum = 0
    for i in str(n):
        sum += int(i)
    if l==sum:
        return sum
    else:
        return 0
n=int(input())
print(AutoCount(n))