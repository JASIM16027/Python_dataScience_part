import Max_number
from Max_number import find_max

number_1st_list = [1, 200, 100, 4, 6, 7, 30, 60]
number_2nd_list = [1, 4, 5, 6, 7]
number_3rd_list = [12, 14, 15, 16, 17]
max_number = find_max(number_1st_list)

print(max_number)
print(find_max(number_2nd_list))

print(find_max(number_3rd_list))
