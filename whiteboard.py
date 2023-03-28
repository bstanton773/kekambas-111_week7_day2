# Write a function that doubles every second integer in a list starting from the left.

# solution([1, 2, 3, 4]) -> [1, 4, 3, 8]

def solution(nums_list):
    # write your code here
    for i in range(len(nums_list)):
        if i % 2 == 1:
            nums_list[i] = nums_list[i] * 2
    return nums_list

print(solution([1, 2, 3, 4]))


def solution(nums_list):
    # write your code here
    new_list = []
    for i in range(len(nums_list)):
        if i % 2:
            new_list.append(nums_list[i] * 2)
        else:
            new_list.append(nums_list[i])
    return new_list


print(solution([1, 2, 3, 4]))
