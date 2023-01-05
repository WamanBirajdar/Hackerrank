""""
You are given a string .
Your task is to print all possible size  replacement combinations of the string in lexicographic sorted order.
A single line containing the string  and integer value  separated by a space.


Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *

s,k=input().split()
S=sorted(s)
for i in combinations_with_replacement(S,int(k)):
    print("".join(i))
