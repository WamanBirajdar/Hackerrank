fruits = ['Apples', 'Oranges', 'Bananas']
quantities = [5, 3, 4]
prices = [1.50, 2.25, 0.89]


i=0
ouput=[]

for fruit in fruits:
    temp_qt=quantities[i]
    temp_price=prices[i]
    ouput.append((fruit,temp_qt,temp_price))

print(ouput)
