def add_nums(num1, num2):
    return num1 + num2


print(add_nums)
print(add_nums(15, 30))
# print(add_nums())

# Ternary
# value_if_true else condition value_if_false
number = int(input('Enter a number between 1-20: '))

value = 'Top Half' if number > 10 else 'Bottom Half'

print(value)
