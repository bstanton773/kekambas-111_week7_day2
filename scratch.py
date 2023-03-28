def add_nums(num1, num2):
    return num1 + num2


print(add_nums)
print(add_nums(15, 30))
# print(add_nums())

# Ternary
# value_if_true else condition value_if_false
# number = int(input('Enter a number between 1-20: '))

# value = 'Top Half' if number > 10 else 'Bottom Half'

# print(value)


list_a = [1, 2, 3]
list_b = [4, 5, 6]

list_c = list_a + list_b
print(list_c)

print(30 in list_c)


my_name_list = ['B', 'r', 'i', 'a', 'n']
print(my_name_list)
print(''.join(my_name_list))
print('-'.join(my_name_list))

name_list = [letter for letter in 'Brian Stanton']

print(name_list[3::2])
