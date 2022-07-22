import random

for x in range(10):
    # random.seed(0)
    print(random.randint(1, 20), end=" ")

print()
for x in range(10):
    print(random.random(), end=" ")
print()

members = ['Jasim', 'Shanto', "Jewel", 'Fahim', 'Rasel']
leader = random.choice(members)
print(leader)
