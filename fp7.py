#Write a Python code to print the factorial 
#Formula : n! = n*(n-1)*....*1(base : 0! = 1)
#Take the input from the user as n , 
#Example : 
#Input : 5
#Output : 120

num = int(input("Enter a number to find its factorial: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
print(factorial(num))