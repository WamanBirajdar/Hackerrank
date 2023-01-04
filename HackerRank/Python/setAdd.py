'''
Task

Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. S
he decided to count the total number of distinct country stamps in her collection. 
She asked for your help. You pick the stamps one by one from a stack of  country stamps.
Find the total number of distinct country stamps.

7
UK
China
USA
France
New Zealand
UK
France 

Sample Output

5

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
countries=set()

for i in range(n):
    s=countries.add(input())

    
print(len(countries))
