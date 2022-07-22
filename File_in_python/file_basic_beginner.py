file = open('meal_menu.txt', 'r')
data = file.read()
print(data)

file.close()
file_write = open("text.txt", 'w')
file_write.write('Hi, I am Jasim Uddin \n')
file_write.write("I'm from Bangladesh. I study at Computer Science and Engineering\n ")
file_write.write("I would like to be a AI Engineer")
file_write.close()

file2 = open('text.txt', "r")

print(file2.read())

with open('text_format.txt', 'w') as file:
    file.write('Hello, my name is Jasim Uddin.\n'
               ' I am going to go  German next year ')

with open('text_format.txt', 'r') as file:
    data = file.readlines()

for line in data:
    word = line.split()
    print(word)

