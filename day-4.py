# Instructions
# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
#
# Important: You are not allowed to use the choice() function.
#
# Line 1 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name
#
# NOTE: Don't worry about getting hold of the input(), we've done the work behind the scenes to import everything.
#
# HINT: Assume that names looks like this: input: x, y, z, names = ["x", "y", "z"]
#
# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.
# import random
# name_string="vaseem,sachin,suraj"
# names = [name.strip() for name in name_string.split(',')]
# random_index=random.randint(0,len(names)-1)
# selected_names=names[random_index]
# # print(f"{selected_names} is going to have sex today")
# if random_index==1:
#     print("vaseem")
# else:
#     print(f"{selected_names} is going to have sex today")
# vazu=["vaseem"]
# print(vazu[1][1])
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input("Where do you want to put the treasure?") # Where do you want to put the treasure?
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
# letter=position[0].lower()
# abc=["a","b","c"]
# letter_index=abc.index(letter)
# number_index=int(position[1])-1
# map[number_index][letter_index]="X"
#
#
# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")





# day-4 project rock paper scissor
import random
print("Hello guys lets play rock paper and scissor game")
options=["rock","paper","scissor"]
computer_choice=random.choice(options)
print("the computer choice is=",computer_choice)
player_choice=input("enter the user choice from rock paper scissor")
if computer_choice==player_choice:
    print("it's tie")
    exit()
if computer_choice=="scissor" and player_choice=="paper" or computer_choice=="rock" and player_choice=="scissor" or computer_choice=="paper" and player_choice=="rock":
    print("computer win")
else:
    print("player win")




