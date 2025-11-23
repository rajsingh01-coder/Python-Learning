#Write a function word_frequency(sentence) that returns a dictionary with word frequency.
#Input: "this is a test this is not fun"
#Output: {'this': 2, 'is': 2, 'a': 1, 'test': 1, 'not': 1, 'fun': 1}
def word_frequency(sentence):
    words = sentence.split()        #->split words ko ek ek kr ke thodata hai
    frequency = {}                  #->empty dictionary hai ek ek kr ke words ko count krnta hai
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1 
    return frequency
print(word_frequency("this is a test this is not fun"))