nums = [1, 2, 4, 5, 6, 7, 8, 9]
for num in nums:
    if num == 4:
        print('Found!')
        continue
    print(num, end=" ")


#  Example 01

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print()
for num in nums:
    print("[", end=" ")
    for letter in 'abc':
        print(num, letter, end=" ")
    print(']')


for i in range(10):
    print(i, end="-->")

