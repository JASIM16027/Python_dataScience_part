prices = [20, 100, 200, 40, 600, 60, 60, 100]
total = 0

for price in prices:
    total += price

print(f'total price is ${total}')

for x in range(10):
    for y in range(5):
        print(f'({x} , {y}) ', end=" ")
    print()


num = [5, 2, 5, 2, 2]

print("Nested for loop : ")

for x in num:
    output = ''
    for y in range(x):
        output += 'x'
    print(output)


print("the below code is used single for loop : ")
for x_count in num:
    print('x'*x_count)



