#The Author is Cody Brown, CPSC207, 07 Nov
#Test on 10 Nov 2022: includes strings, substrings, random module, and dctionary

#HISTOGRAM FUNCTION!!!!!!
def histogram(word):
    d = dict()
    for char in word:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d

hist = histogram('parrot')
hist
#this returns {'p': 1, 'a': 1, 'r': 2, 'o': 1, 't': 1}
#this will be in our test

#Inverting a dictionary
def invert_dict(d):
    inverse = dict()
    #when you want to have access to each item in sequential dataset, use for loop
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
            #append the key to the value that has the list of the values
    return inverse

inverse = invert_dict(hist)
inverse
#this returns {1: ['p', 'a', 'o', 't'], 2: ['r']}
#there is now only 2 key's in our dictionary, our values are lists, and
#insides those lists, we have strings!

#Try:
t = [1, 2, 3]
d = dict()
d[t] = "oops"
#this returns: TypeError: unhashable type: 'list'
#cannot have lists in a dictionary like this

#TEST REVIEW

#Strings and complex strings
# - single quotes ' vs double quotes "
# - new line character \n (goes to new line)
# - escape character \ (avoid code from seeing somehting in a code)
# - triple quotes """ (each time you press enter, you will go to the next line)

len() #function

#Looping over a letter of strings, can gain access to each items in a lists
#FOR Looping
for thing in "Hello":
    print(thing)

#Looping over characters and searching if we have a specifc characters
for ch in "Hello!":
    print(ch)
    if ch == "!":
        print("i am excited too!")

#Indexing! look at class activty for session 14

#Range function
for i in range(3):
    print(i)

    #is equal to

for i in range(len("yay")):
    print(i)

#both return:
#0
#1
#2

#len(word) gives access to indices and characters

#Slicing
#being able to tell (w/out computer) what these will give:
"python"[0:2]
... #(more in slides)

#Indices and For-Looping
for thing in ["some", 'list', 'of', 'things']:
    print(things)

my_list = ['a','b','c',1,2,3,False,True,2.5,3.1415]
my_list[:4]
my_list
... #(more in slides)

#List Methods

#Append: add one item to the END of a lists
#Extend: add possibly several items to the end of a list
#Sort: change a list so it is in alphabetical and numercal order
    #must be in the same datatype, no integers and strings - must be one type
#Reverse: change a list so it is i the opposite order from how it was before

#where does the . and command go?
my_list._____("")
    #END of the name

#Mutable vs Immutable
    #lists are mutable - meaning we CAN modify them
    #strings are immutable - meaning we CANNOT modify the substrings or letters

#Locating a substring
word = "fascinating"
location = 4
size = 2
word[location : location + size]
    #to find substring we are looking for

#Counting substrings, THIS WILL BE ASKED!
def count_substring(string, target):
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
            total += len(target) #improtant line
        else:
            index += 1
    return total

#Locating All function, retunrs a list
def locate_all(string, sub):
    matches = []
    index = 0
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            matches.append(index)
            index += len(sub)
        else:
            index += 1
    return matches
#try to be able to explain which each line does

#Random module
import random
color = random.choice(['red','green','blue'])
    #can be used over lists and can have ANYTHING inside
die_roll = random.randint(1,6)
    #only does integers
#might be given list of names, give two random names - must use random.choice command
#make sure not to repeat things(?)

#Go over:
# - slides
# - class activites
# - quizzes

#two coding questions, matching, fill in the blanks, simple short answers
