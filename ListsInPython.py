# Lists in Python

# https://www.youtube.com/watch?v=9OeznAkyQz4

# create a list of any type with brackets []

letters = ["a", "b", "c", "d"]

# list of lists - two dimensional list, or matrix

matrix = [[0,1], [2,3]]

# creating a list of repeated items - the asterisk makes the item of the list to be repeated

zeros = [0] * 100

# a plus sign concatenates multiple lists

zeros = [0] * 5
combined = zeros + letters
print(combined)

# create a sequence automatically - a list of numbers from 0 to < 20
numbers = list(range(20))

# each character in the string would be an item in the list
chars = list("Hello World")

# get the number of items of a list
print(len(chars))

## acessing items in a list
print(letters[0])

# last item
print(letters[-1])

# changing one item
letters[0]="A"
print(letters)

# slicing without changing the content
print(letters[0:3])
# or: (with the exact same result)
print(letters[:3])

# if you dont put the last index, the length of the list will be used
print(letters[0:])

# when slicing a list, I can also pass a step
print(letters[::2])
print(numbers[::2])

# this will print all items in the original list, but in reverse order
print(numbers[::-1])


## Unpacking lists
numbers = [1,2,3]
first = numbers[0]
second = numbers[1]
third = numbers[2]

# there's a cleaner way to do the same with list unpacking:
first, second, third = numbers
# the numbers of variables on the left side of the equal sign should be equal to the numbers of elements in the list
# otherwise, we will see an error
# ex.: first, second = numbers
# if we don't want anything, we have to use this sintax:
numbers = [1,2,3,4,5,6]
first, second, *other = numbers
# where other will be another list
print(other)
# so, the asterisk makes python pack the values into another variable. This is used also when we have a function with
# a variable number of arguments

# if we care only with the first and the last:
first, *other, last = numbers

## Looping over lists

letters = ["a", "b", "c"]
for letter in letters: print(letter)

# what if we want also the letter index:
for tupple in enumerate(letters): print(tupple)

# we can unpack each letter with:
for index, letter in enumerate(letters): print(index, letter)

## Adding / removing items in a list

# add at the end:
letters.append("d")

# add something at an specific index:
letters.insert(0, "a")

# remove at the end
letters.pop()

# remove at some specific index - in this case, at the beginning
letters.pop(0)

print(letters)

# remove the first occurence 
letters.remove("b")

# remove a range of items
del letters[0:3]

# remove all objects in a list
letters.clear()

## Finding items
letters = ["a", "b", "c"]

# how to find the index of letter "a" in the list
letters.index("a")

# you will get an error if you try to find an object that is NOT in the list
# letters.index("d")
# for that, you want to use the operator "in":
print("d" in letters)


# you can count the number of occurences of an item in a list:
print(letters.count("d"))
print(letters.count("a"))
