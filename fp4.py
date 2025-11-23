#Write a function get_min_max(lst) that returns the minimum and maximum of the list .
#Input: [3, 5, 1, 9, 7]
#Output: (1, 9)
def get_min_max(list):
    if not list:
        return None, None
    min_val = list[0]
    max_val = list[0]
    for num in list:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val
print(get_min_max([3, 5, 1, 9, 7]))
    