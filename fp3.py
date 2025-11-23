#Write a function sum_numbers(lst) that returns the sum of all numbers in a list.
#Input : [1,2,3,4,5]
#Output : 15
def sum_numbers(list):
    total = 0
    for num in list:
        total += num
    return total            
print(sum_numbers([1,2,3,4,5]))