# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2020,Created started script
# HyojinK,11.13.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #
# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
objFile = open("ToDoList.txt", "r")
for row in objFile:
    a, b = row.split(",")
    dicRow = {"Task": a, "Priority": b}
    lstTable.append(dicRow)
objFile.close()
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == "1"):
        print("Your current data is : ")
        for i in lstTable:
            print(i["Task"] + ", " + i["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == "2"):
        print("Please type in a 'Task' and 'Priority' again")
        strtask = input("Enter a Task: ")
        strpriority = input("Enter a Priority: ")
        dicRow = {"Task": strtask, "Priority": strpriority}
        lstTable.append(dicRow)
        objFile = open("ToDoList.txt", "a")
        objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()
        objFile = open("ToDoList.txt", "r")
        for row in objFile:
            a, b = row.split(",")
            print("Your data now is:" + "{Task:" + a + "}, {Priority:" + b.strip() + "}")
        objFile.close()
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == "3"):
        lstTable.pop(len(lstTable)-1)
        print(lstTable)
        print("The lastly added data has been deleted")
        objFile = open("ToDoList.txt", "w")
        for i in lstTable:
            objFile.write(i["Task"]+","+i["Priority"])
        objFile.close()
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == "4"):
        print("Your data has been saved onto 'ToDoList.txt' file.")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == "5"):
        finish = input("Please press enter key to exit")
        print("Done!")
        break
