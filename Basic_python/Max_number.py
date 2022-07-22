def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:

        if max_number < number:
            max_number = number
    return max_number



#print(find_max(number_list))