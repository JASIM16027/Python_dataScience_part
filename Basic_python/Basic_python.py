"""birth_year = input('Enter Birthday : ')
print(type(birth_year))
age = 2020 - int(birth_year)
print(age)
# pound to kg conversion
weight_lbs = input('Weight(lbs) : ')
weight_kg = float(weight_lbs) * 0.45
print(weight_kg)

# kg to pound conversion
weight_kg1 = input('Weight(kg) : ')
weight_lbs1 = float(weight_kg1) / 0.45
print(weight_lbs1)


name = 'Jasim Uddin'

print(name[1:-1])

fname = 'Jasim'
lname = 'Uddin'

message = fname + " [" + lname + "] is a coder"
msg = f'{fname} [{lname}] is a coder'
print(message)
print(msg)


course = "Python's Course for Beginner"
another_course = course[0:6]
# print(another_course)
print(len(course))
print(len(another_course))
f = course.find('Course')
print(course)
print(course.upper())
print(course.lower())
print(f)

r = course.replace('Beginner', 'Absolute Beginners')

print(r)

bol = 'Python' in course
bol1 = 'Course' in course
print(bol1)
print(bol)



x = 3.5
print(round(x))



day = input('Enter the type of day : ')
if day == 'hot':
    print("It's a hot day.")
    print("Drink a lot water.")

elif day == 'cold':
    print("It's a cold day")
    print("put on a warm clothes")

else:
    print("It's a good day")
    print("Enjoy your day as much as you can .")
    print("live with happiness every single moment")


price = 1000000
has_good_credit = True

if has_good_credit:
    Down_payment = price * 0.9

else:
    Down_payment = price * 0.2

print(f"Down payment : ${Down_payment}")




income = input("Enter income : ")
credit = input("Enter credit : ")

if income == "high" and credit == "good credit":
    print("Eligible for load")
else:
    print("Not Eligible for load")




has_high_income =  True
has_good_credit = False

if has_high_income and not has_good_credit:
    print("Eligible for load")
else:
    print("Not Eligible for load")

# Example weight conversion

weight = int(input("Enter weight: "))
unit = input("(L)bs or (K)g : ")
if unit.upper() == 'L':
    converted = weight*0.45
    print(f'you are  {converted} kilos')

elif unit.upper() == "K":
    converted = weight/.45
    print(f'you are  {converted} pounds')


secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess : "))
    guess_count += 1
    if guess == secret_number:
        print("you won!")
        print("Great job.")
        break

else:
    print(" sorry, you failed")

# List Example
numbers = [12, 43, 23, 4500, 100, 300, 140, 500]

max_num = numbers[0]
for x in numbers:
    if max_num < x:
        max_num = x

print("max number is : ", max_num)




matrix = [

    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [20, 30, 40, 50, 60]

]

mat = 0
print(matrix[0])
for x in matrix:

    for y in x:
        mat += y
print(mat)

matrix = [
    [1, 4, 7, 10, 14],
    [2, 3, 5, 6, 8, 9],
    [11, 12, 13, 15, 16]

]
print(matrix)

sum1 = 0
number = []
for row in matrix:
    for col in row:
        number.append(col)
        sum1 += col
        print(col, end=" ")
    print()

print('sum of matrix is ', sum1)
print(number)

number = [1, 2, 10, 20, 50, 29]

number.insert(2, 18)
number.append(20)
number.insert(1, 25)
print("Before popped up ", number)
number.pop()

print("After popped up ", number)

number.remove(25)
print("After removing  25 ", number)
number.clear()
number.append(10)
number.insert(0, 20)
print(number)

number.append(21)
number.append(21)
number.append(21)
number.append(21)

print(number)

print(number.index(21))
print(21 in number)

print(number.count(21))

number_list = number.copy()
print(number_list)
print(number.__add__(number))



numbers = [1, 2, 3, 2, 2, 8, 4, 5, 6, 5, 5]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)



# Tuple Example

num = (10, 20, 20)
# num[0] = 20 #tuple object doesn't support item assignment
print(num[1])

coordinate = (1, 2, 3)

x, y, z = coordinate
print(x, y, z)


customer = {
    'name': 'Jasim',
    'age': 25,
    'profession': 'Student',
    'is_verified': True
}

print(customer.get('name'))
print(customer.get('profession'))
print(customer.get('age'))
print(customer.get('Birthday'))
print(customer.get('is_verified'))



phone = input("Enter phone number : ")

digits_mapping = {
    '1':'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5':'five'
}

output = ''

for ch in phone:
    output += digits_mapping.get(ch, '!')+" "
    print(output)
print(output)




while True:

        message = input(">")
        if message.lower() !="exit":

                words = message.split(' ')
                emojis = {

                    ":)": "😂",
                    "(:": "😢"

                }

                output = ""
                for word in words:
                    output += emojis.get(word, word)+" "
                print(output)
        else:
            break

"""




