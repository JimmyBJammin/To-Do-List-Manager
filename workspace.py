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
#Importing os allows me to control the directory
import csv
import os

#Main_Menu will be the default function, managing the user interface
def Main_Menu():
    menu_choice = str("")

    print("\nWelcome to the To-Do List Manager!\n")

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
    list_path = str("C:\GitHub Repos\To-Do-List-Manager\Lists")
    list_list = os.listdir(list_path)

    count = 0
    menu_choice = str("")

    print("\nWhich list would you like to view?\n")

    print("0. Return to Main Menu")
    for list in list_list:
        print(str(count + 1) + ": " + list_list[count])
        count += 1

    print()

    while not(menu_choice.isdigit()):
        menu_choice = input("-> ")

        if menu_choice == "0":
            menu_choice = menu_choice
        elif menu_choice.isdigit():
            if not((int(menu_choice) >= 1) and (int(menu_choice) <= len(list_list))):
                menu_choice = ""
                print("\nThat was not a valid choice. Please enter the corresponding number of your choice.")
        elif not(menu_choice.isdigit()):
            menu_choice = ""
            print("\nThat was not a valid choice. Please enter the corresponding number of your choice.")
        
    if menu_choice == "0":
        Main_Menu()
    else:    
        Read_List(int(menu_choice) - 1)

#Read_List will print the data from the .csv file and allow editing
def Read_List(index):
    print("You chose: " + list_list[index])
    
    list_name = list_path + "\\" + list_list[index]

    with open(list_name, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            print(row)

#New_List will allow user to create lists and assign tasks to them
def New_List():
    list_path = str("C:\GitHub Repos\To-Do-List-Manager\Lists")
    list_list = os.listdir(list_path)
    menu_choice = str("")
    new_list_name = str("")

    print("\nWhat would you like to name your list?")
    new_list_name = input("-> ")
    new_list_name = new_list_name + ".csv"

    while new_list_name in list_list:
        print("\nThat list name already exists. Please choose another name.")
        new_list_name = input("-> ")
        new_list_name = new_list_name + ".csv"

    new_list_name = list_path + "\\" + new_list_name

    with open(new_list_name, mode = 'w') as csv_file:
        csv_writer = csv.writer(csv_file)

        print("\nWhat task would you like to add? (Enter '0' to exit)")

        while not(menu_choice == "0"):
            menu_choice = input("-> ")

            if not(menu_choice == "0"):
                csv_writer.writerow(menu_choice)

    Main_Menu()



Main_Menu()