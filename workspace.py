'''
Hello! This is my To-Do List Manager project!

Users will be able to:
-Create lists
    -Add/delete tasks to that list
    -Set as a daily or unique list of tasks
-View lists
-Mark tasks as complete

Enjoy!
'''
#Importing csv is required for reading and writing .csv files
import csv
import os

list_list = os.listdir("C:\GitHub Repos\To-Do-List-Manager\Lists")
list_option = str("")
menu_choice = str(0)
count = int(0)

#Main_Menu will be the default function, managing the user interface
def Main_Menu():
    print("Welcome to the To-Do List Manager!\n")

    print("What would like to do?")
    print("1. View Lists")
    print("2. Create New List")
    print("0. Exit")
    menu_choice = str(input("\n-> "))

    while not(menu_choice == "1" or menu_choice == "2" or menu_choice == "0"):
        print("\nThat was not a valid choice. Please enter the corresponding number of your choice.")
        menu_choice = str(input("-> "))

    if menu_choice == "1":
        View_List()
    elif menu_choice == "2":
        New_List()
    else:        
        quit

#View_List will display all created lists on the user's machines
def View_List():
    count = 0
    list_option = str("")

    print("\nWhich list would you like to view?\n")

    for list in list_list:
        print(str(count + 1) + ": " + list_list[count])
        count += 1

    print()

    while not(list_option.isdigit()):
        list_option = input("-> ")

        if list_option.isdigit():
            if not((int(list_option) >= 1) and (int(list_option) <= len(list_list))):
                list_option = ""
                print("\nThat was not a valid choice. Please enter the corresponding number of your choice.")
        elif not(list_option.isdigit()):
            list_option = ""
            print("\nThat was not a valid choice. Please enter the corresponding number of your choice.")

    Read_List(int(list_option) - 1)

#Read_List will print the data from the .csv file and allow editing
def Read_List(index):
    print("You chose: " + list_list[index])

#New_List will allow user to create lists and assign tasks to them
def New_List():
    print("What would you like to name your list?")

Main_Menu()