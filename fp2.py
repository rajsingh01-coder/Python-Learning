#Write a function count_vowels(s) that returns the number of vowels in the given string.
#Input: "Hello World"
#Output: 3
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1  
    return count    
print(count_vowels("Hellow world"))  