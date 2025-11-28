'''
Hello! This is my To-Do List Manager project!

Users will be able to:
-Create lists
    -Add tasks to that list
-View lists
    -Mark tasks as complete
    -Delete tasks

Enjoy!
'''
#Importing csv is required for reading and writing .csv files
#Importing os allows me to control the directory
import csv
import os

#Main_Menu will be the default function, managing the user interface
def Main_Menu():
    os.system('cls')
    menu_choice = str("")

    print("\nHello " + os.getlogin() + "! Welcome to the To-Do List Manager!\n")

    print("What would like to do?")
    print("1. Create New List")
    print("2. View Lists")
    print("0. Exit")
    menu_choice = str(input("\n-> "))

    while not(menu_choice == "1" or menu_choice == "2" or menu_choice == "0"):
        os.system('cls')
        print("\nHello " + os.getlogin() + "! Welcome to the To-Do List Manager!\n")

        print("What would like to do?")
        print("1. Create New List")
        print("2. View Lists")
        print("0. Exit")

        print("\nThat was not a valid choice. Please enter the corresponding number of your choice.")
        menu_choice = str(input("-> "))

    if menu_choice == "1":
        New_List()
    elif menu_choice == "2":
        View_List()
    else:        
        quit

#Will create the csv file given the name and list of tasks
def Write_CSV(csv_name, task_list):
    with open(csv_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        csv_writer.writerows(task_list)

#Will return the list of tasks given the csv file name
def Get_CSV(csv_name):
    task_list = []

    with open(csv_name, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            task_list.append(row)

    return task_list

#New_List will allow user to create lists and assign task_list to them
def New_List():
    os.system('cls')
    list_path = str(os.getcwd() + "\Lists")
    list_list = os.listdir(list_path)
    menu_choice = str("")
    new_list_name = str("")
    task_list = [["Task", "Complete"]]

    print("\nWhat would you like to name your list? (Enter '0' to cancel)")
    menu_choice = input("-> ")
    new_list_name = menu_choice + ".csv"

    while new_list_name in list_list:
        os.system('cls')
        new_list_name = str("")

        print("\nThat list name already exists. Please choose another name. (Enter '0' to cancel)")
        menu_choice = input("-> ")
        new_list_name = menu_choice + ".csv"

    
    new_list_name = list_path + "\\" + new_list_name

    if not(menu_choice == '0'):
        print("\nWhat task would you like to add? (Enter '0' finish)")

        while not(menu_choice == "0"):
            menu_choice = input("-> ")

            if not(menu_choice == "0"):
                task_list.append([menu_choice, ""])

        Write_CSV(new_list_name, task_list)

    Main_Menu()

#View_List will display all created lists on the user's machines
def View_List():
    os.system('cls')
    list_path = str(os.getcwd() + "\Lists")
    list_list = os.listdir(list_path)

    count = 0
    menu_choice = str("")

    print("\nWhich list would you like to view?\n")

    for list in list_list:
        print(str(count + 1) + ": " + list_list[count])
        count += 1

    print("0. Return to Main Menu\n")

    while not(menu_choice.isdigit()):
        menu_choice = input("-> ")

        if menu_choice == "0":
            menu_choice = menu_choice
        elif menu_choice.isdigit():
            if not((int(menu_choice) >= 1) and (int(menu_choice) <= len(list_list))):
                os.system('cls')
                count = 0
                menu_choice = str("")

                print("\nWhich list would you like to view?\n")

                for list in list_list:
                    print(str(count + 1) + ": " + list_list[count])
                    count += 1

                print("0. Return to Main Menu")
                
                print("\nThat was not a valid choice. Please enter the corresponding number of your choice.")
        elif not(menu_choice.isdigit()):
            os.system('cls')
            count = 0
            menu_choice = str("")

            print("\nWhich list would you like to view?\n")

            for list in list_list:
                print(str(count + 1) + ": " + list_list[count])
                count += 1

            print("0. Return to Main Menu")
            print("\nThat was not a valid choice. Please enter the corresponding number of your choice.")
        
    if menu_choice == "0":
        Main_Menu()
    else:    
        Read_List(int(menu_choice) - 1)

#Read_List will print the data from the .csv file and allow editing
def Read_List(list_index):
    os.system('cls')
    list_path = str(os.getcwd() + "\Lists")
    list_list = os.listdir(list_path)
    list_name = list_path + "\\" + list_list[list_index]
    task_list = Get_CSV(list_name)

    count = 0

    print("You chose: " + list_list[list_index] + "\n")

    for row in task_list:
        if count == 0:
            print("   " + row[0] + "\t\t" + row[1])
        else:
            print(str(count) + ". " + row[0] + "\t\t" + row[1])
        count += 1


    print("\nWould you like to edit?")
    print("1. Mark a task as complete")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Delete list")
    print("0. Return")
    menu_choice = str(input("\n-> "))

    while not(menu_choice == "1" or menu_choice == "2" or menu_choice == "3" or menu_choice == "4" or menu_choice == "0"):
        os.system('cls')
        count = 0

        print("You chose: " + list_list[list_index] + "\n")

        for row in task_list:
            if count == 0:
                print("   " + row[0] + "\t\t" + row[1])
            else:
                print(str(count) + ". " + row[0] + "\t\t" + row[1])
            count += 1


        print("\nWould you like to edit?")
        print("1. Mark a task as complete")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Delete list")
        print("0. Return")

        print("\nThat was not a valid choice. Please enter the corresponding number of your choice.")
        menu_choice = str(input("-> "))

    if menu_choice == "1":
        Complete_Task(list_index)
    elif menu_choice == "2":
        Add_Task(list_index)
    elif menu_choice == "3":
        Delete_Task(list_index)
    elif menu_choice == "4":
        Delete_List(list_index)
    else:        
        View_List()

#Mark the designated task as complete with an 'x'
def Complete_Task(list_index):
    os.system('cls')
    list_path = str(os.getcwd() + "\Lists")
    list_list = os.listdir(list_path)
    list_name = list_path + "\\" + list_list[list_index]
    task_list = Get_CSV(list_name)

    menu_choice = ""
    count = 0

    print(list_list[list_index]+ "\n")
    for row in task_list:
        if count == 0:
            print("   " + row[0] + "\t\t" + row[1])
        else:
            print(str(count) + ".\t" + row[0] + "\t\t" + row[1])
        count += 1
    
    print("\nWhich task have you completed? (Press '0' to cancel)")
    
    while not(menu_choice.isdigit()):
        menu_choice = input("-> ")

        if menu_choice == "0":
            menu_choice = menu_choice
        elif menu_choice.isdigit():
            if not((int(menu_choice) >= 1) and (int(menu_choice) <= (len(task_list) - 1))):
                os.system('cls')
                menu_choice = str("")
                count = 0

                print(list_list[list_index]+ "\n")
                for row in task_list:
                    if count == 0:
                        print("\t" + row[0] + "\t\t" + row[1])
                    else:
                        print(str(count) + ".\t" + row[0] + "\t\t" + row[1])
                    count += 1
                
                print("\nWhich task have you completed? (Press '0' to cancel)")
                
                print("\nThat was not a valid choice. Please enter the corresponding number of your choice.")
        elif not(menu_choice.isdigit()):
            os.system('cls')
            count = 0
            menu_choice = str("")

            print(list_list[list_index]+ "\n")
            for row in task_list:
                if count == 0:
                    print("\t" + row[0] + "\t\t" + row[1])
                else:
                    print(str(count) + ".\t" + row[0] + "\t\t" + row[1])
                count += 1
            
            print("\nWhich task have you completed? (Press '0' to cancel)")

            print("\nThat was not a valid choice. Please enter the corresponding number of your choice.")

    if not(menu_choice == "0"):
        task_list[int(menu_choice)][1] = "x"

        Write_CSV(list_name, task_list)

    Read_List(list_index)

#Add a task to the end of the list of tasks
def Add_Task(list_index):
    os.system('cls')
    list_path = str(os.getcwd() + "\Lists")
    list_list = os.listdir(list_path)
    list_name = list_path + "\\" + list_list[list_index]
    task_list = Get_CSV(list_name)

    menu_choice = ""
    count = 0

    print(list_list[list_index]+ "\n")
    for row in task_list:
        if count == 0:
            print("\t" + row[0] + "\t\t" + row[1])
        else:
            print(str(count) + ".\t" + row[0] + "\t\t" + row[1])
        count += 1
    
    print("\nWhich task would you like to add? (Press '0' to cancel)")
    menu_choice = input("-> ")
    
    if not(menu_choice == "0"):
        task_list.append([menu_choice, ""])

        Write_CSV(list_name, task_list)

    Read_List(list_index)

#Delete the designated task
def Delete_Task(list_index):
    os.system('cls')
    list_path = str(os.getcwd() + "\Lists")
    list_list = os.listdir(list_path)
    list_name = list_path + "\\" + list_list[list_index]
    task_list = Get_CSV(list_name)

    menu_choice = ""
    count = 0

    print(list_list[list_index]+ "\n")
    for row in task_list:
        if count == 0:
            print("\t" + row[0] + "\t\t" + row[1])
        else:
            print(str(count) + ".\t" + row[0] + "\t\t" + row[1])
        count += 1
    
    print("\nWhich task would you like to delete? (Press '0' to cancel)")
    
    while not(menu_choice.isdigit()):
        menu_choice = input("-> ")

        if menu_choice == "0":
            menu_choice = menu_choice
        elif menu_choice.isdigit():
            if not((int(menu_choice) >= 1) and (int(menu_choice) <= (len(task_list) - 1))):
                os.system('cls')
                menu_choice = str("")
                count = 0

                print(list_list[list_index]+ "\n")
                for row in task_list:
                    if count == 0:
                        print("\t" + row[0] + "\t\t" + row[1])
                    else:
                        print(str(count) + ".\t" + row[0] + "\t\t" + row[1])
                    count += 1
                
                print("\nWhich task would you like to delete? (Press '0' to cancel)")
                
                print("\nThat was not a valid choice. Please enter the corresponding number of your choice.")
        elif not(menu_choice.isdigit()):
            os.system('cls')
            count = 0
            menu_choice = str("")

            print(list_list[list_index]+ "\n")
            for row in task_list:
                if count == 0:
                    print("\t" + row[0] + "\t\t" + row[1])
                else:
                    print(str(count) + ".\t" + row[0] + "\t\t" + row[1])
                count += 1
            
            print("\nWhich task would you like to delete? (Press '0' to cancel)")

            print("\nThat was not a valid choice. Please enter the corresponding number of your choice.")

    if not(menu_choice == "0"):
        task_list.pop(int(menu_choice))

        Write_CSV(list_name, task_list)

    Read_List(list_index)

#Delete the entire list, with confirmation
def Delete_List(list_index):
    os.system('cls')
    list_path = str(os.getcwd() + "\Lists")
    list_list = os.listdir(list_path)
    list_name = list_path + "\\" + list_list[list_index]

    menu_choice = str("")

    print("Are you sure you want to delete the entire list? (Enter '0' to cancel)")
    print("\nEnter 'DELETE' to confirm.")

    while menu_choice == "":
        menu_choice = input("-> ")

        if menu_choice == "0":
            menu_choice = "0"
        elif menu_choice == "DELETE":
            os.remove(list_name)   
        else:
            os.system('cls')

            menu_choice = str("")

            print("Are you sure you want to delete the entire list? (Enter '0' to cancel)")
            print("\nEnter 'DELETE' to confirm.") 

    if menu_choice == "0":
        Read_List(list_index)
    if menu_choice == "DELETE":
        View_List()   

#Will create the Lists folder wherever the program is saved.
list_path = str(os.getcwd() + "\Lists")

if not(os.path.isdir(list_path)):
    os.makedirs(list_path)


Main_Menu()