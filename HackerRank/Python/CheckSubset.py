'''
You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False.

Input Format

The first line will contain the number of test cases, T.
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set A .
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of set B .
'''


# STD INPUT
testcases=int(input())

for i in range(testcases):
    n,set_a=input(),set(input().split())
    m,set_b=input(),set(input().split())
    
    
    if len(set_a)==len(set_a.intersection(set_b)):
        print(True)
    else:
        print(False)
