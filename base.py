from math import *
from Student import Student  #from module (python file) Student import class Student
from Chef import Chef
from ChineseChef import ChineseChef

print("\n--simple hello world print, print is a function--")
print("hello world, this is the first program!")


print("\n--variable assignment--")
name = "Shobhit"
age = 32
healthy = True   # type boolean


print("\n--how to replace variables with their values--")
print("my name is %s and my age is %d" %(name, age))
print("Am I healthy: ", healthy)

print("\n--strings--")
phrase = "This One Is.."
print(phrase + "cool")

print("\n--example fo using a function on a string--")
print("Case changed: ",phrase.swapcase())
print("Length of phrase is: ", len(phrase))
print(phrase[0])

print("\n--index from the right end start with -1, decreases by 1 everytime you move left--")
print(phrase[-3])
print(phrase.index("."))

print("\n--Numbers--")

print(max(4,6))
print(pow(2,4))
print("\n--needed the from math import * statement. math is the module--")
print(floor(3.6))
print(sqrt(6))

#user input

"""
name = input("Please enter your name: ")
print("hello %s" %name) """

print("\n--lists")

friends = ["abhishek","joy","harsh","tanuj","vaibhav"]
print(friends[0])
print(friends[1:])
print(friends[1:2])
friends[2] = "nitin"
print(friends)
new_friends = ["priyanka","mora","akshay"]

print("\n--extend the existing list with the passed on list to make one long list--")
friends.extend(new_friends)
print("the extended list of friends is", friends)

print("\n--adds an item at the end of the list--")
friends.append("latest friend")
print("After adding one more", friends)
friends.insert(1, "new friend")
print(friends)
friends.remove("new friend")
print(friends)
friends.pop()
print(friends)
friends2 = friends.copy()
print(friends2)
friends.sort()
print(friends)


print("\n--Tuples: they are immutable--")
coordinates = (4,5)
print(coordinates)
print(coordinates[0])
list_coordinates = [(1,2), (3,4), (4,5)]
print(list_coordinates)

print("\n--functions--")

def say_hi(name):
    print("hi", name)

say_hi("Shobhit")

def cube(num):
    return num*num*num

print(cube(3))

print("\n--if_statements--")

is_male = False
is_tall = False
if is_male and is_tall:
    print("Tall Male")
elif is_male and not(is_tall):
    print("Short male")
else:
    print("Not male")

print("\n--Dictionaries   .. key in the dictionary should be unique--")

month_conversions = {
    "jan": "january",
    "feb": "february",
}

print(month_conversions)
print(month_conversions["jan"])
print(month_conversions.get("feb"))
print(month_conversions.get("mar", "Not a valid key"))

print("\n--while loop--")
i = 1
while i<=10:
    print(i)
    i+=1

print("done with while loop")

print("\n--for loop--")

for letter in "The Movie Name":
    print(letter)

friends = ["Abhi","Pali", "Joy", "Mora", "Niga"]
for friend in friends:
    print(friend)

for index in range(4,7):
    print(index)

for index in range(5):
    if index==0:
        print("DO this the first time")
    else:
        print(index)

print("\n--sample function--")

def exp_func(base, power):
    result = 1
    for num in range(power):
        result = result * base
    return result

print("the result is:",exp_func(2,3))

print("\n--2d lists and nested for loop--")

number_grid = [
    [1,2],
    [2,3],
    [3,4],
]
print("2nd element of item 1 in number_grid list is:", (number_grid[0][1]))

print("This wil print all the individual elements of the 2d array")
for i in number_grid:
    for j in i:
        print(j)

"""
print("\n--Try and Catch: error handling--")

try:
    #value = 20/0
    number = int(input("Enter a number:"))
    print(number)
except ValueError as err:
    print("you entered in invalid input and the error is -", err)
except ZeroDivisionError:
    print("you outta your mind?? cannot divide by 0")
"""

print("\n--Reading from files--")  #the file text_file should be in the same directory as this python file. create anything with some text

full_file = open("text_file.txt","r")  #open a file in read mode
isReadable = full_file.readable()
if isReadable:
    print("The file is readable")
    print(full_file.read())
full_file.close()

print("\n--writing to files--")

full_file = open("text_file.txt","a")
full_file.write("This is the added stuff")
full_file.close()


print("\n--classes and objects--") #used to create a custom data type

student1 = Student("Shobhit","IT",4,False)  #instantiate your Student Class.. create an object of the class
print("Student name is " + student1.name1)

is_on_honor_roll = student1.is_on_honor_roll()
if is_on_honor_roll:
    print(student1.name1 + " is on HonorRoll")

generic_chef = Chef()
chinese_chef = ChineseChef()

print("Generic Chef ki special dish: " + generic_chef.special_dish())
print("Chinese chef ki special dish" + chinese_chef.special_dish())


















