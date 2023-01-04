'''
Output the symmetric difference integers in ascending order, one per line.
STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}

Sample Output

5
9
11
12

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

m=input()
i=set(map(int,input().split()))
n=input()
j=set(map(int,input().split()))

o=i.difference(j)
on=j.difference(i)

for a in sorted(o.union(on)):
    print(a)
