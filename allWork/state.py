import sqlite3
import time
import sys

def main_menu():
    print("\nNACWC DAILY PARADE STATE\n")
    menu = ("""
    1 - Create New User
    2 - Login to System
    3 - Exit system\n""")

    userchoice = input(menu)

    if userchoice == "1":
        newUser()

    elif userchoice == "2":
        login()

    elif userchoice == "3":
        print("Goodbye")
        sys.exit()

    else:
        print("Command not recognised: ")

def login():
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        with sqlite3.connect("user.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursor.execute(find_user,[(username),(password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("\nWelcome " +i[2]+"\n")
            #return("exit")
            break

        else:
            print("\nUsername or password not recognised\n")
            again = input("Do you want to try again?(yes/no): ")
            if again.lower() == "no":
                print("Goodbye")
                time.sleep(1)
                #return("exit")
                break

def newUser():
    found = 0
    while found ==0:
        username = input("Please enter a username: ")
        with sqlite3.connect("user.db") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM user WHERE username = ?")
        cursor.execute(findUser,[(username)])

        if cursor.fetchall():
            print("Username Taken,Please try again")
        else:
            found = 1

    firstname = input("Enter your first name: ")
    lastname = input("Enter your lastname: ")
    password = input("Please enter your password: ")
    password = input("Please confirm password: ")
    while password !=password:
        print("Your password didn't match, please try again")
        password = input("Please enter your password: ")
        password = input("Please confirm password: ")
    insertData = '''INSERT INTO user(username,firstname,lastname,password)
    VALUES(?,?,?,?)'''
    cursor.execute(insertData,[(username),(firstname),(lastname),(password)])
    db.commit()

def menu():
    while True:
        print("This is NACWC DAILY PARADE STATE")
        menu = ("""
        1 - Add New Parade State
        2 - Show All Parade States
        3 - Search Parade State
        4 - Delete Parade State
        5 - Exit system\n""")

        userchoice = input(menu)

        if userchoice == "1":
             add_paradestate()

        elif userchoice == "2":
            list_paradestate()

        elif userchoice == "3":
            search_paradestate()

        elif userchoice == "4":
            delete_paradestate()

        elif userchoice == "5":
            print("Goodbye")
            sys.exit()

        else:
            print("Command not recognised, Please try again: ")

def  add_paradestate():
    found = 0
    while found ==0:
        date = input("Today's date: ")
        with sqlite3.connect("Project.db") as db:
            cursor = db.cursor()
        find_paradestate = ("SELECT * FROM columns WHERE date = ?")
        cursor.execute(find_paradestate,[(date)])

        if cursor.fetchall():
            print("The parade State for " + date + " has been Registered.")
        else:
            found = 1
    print("\nNACWC DAILY PARADE STATE AS AT " + date +"\n")
    date = input("Today's Date: ")
    posted_strength = input("Posted Strength: ")
    on_parade = input("On Parade: ")
    on_duty = input("On Duty: ")
    off_duty = input("Off Duty: ")
    sick = input("Sick: ")
    ops = input("Operation: ")
    course = input("Course: ")
    naicc = input("NAICC: ")
    nafc = input("NAFC: ")
    leave = input("Pass: ")
    hosp_admin = input("Hospital Admission: ")

    insertData = '''INSERT INTO columns(date, posted_strength, on_parade, on_duty, off_duty, sick, ops, course, naicc, nafc, leave, hosp_admin)
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?)'''

    cursor.execute(insertData,[(date),(posted_strength),(on_parade),(on_duty),(off_duty),(sick),(ops),(course),(naicc), (nafc),(leave),(hosp_admin)])
    db.commit()

    print("\nToday's Parade State Successfully Saved.\n")

def search_paradestate():
    while True:
        date = input("Please enter the date of the Parade State: ")
        with sqlite3.connect("Project.db") as db:
            cursor = db.cursor()
        find_state = ("SELECT * FROM columns WHERE date = ?")
        cursor.execute(find_state,[(date)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("\nDate: " +i[1] +"\nPosted Strength: " +i[2] + "\nOn Parade: " +i[3] + "\nOn Duty: " +i[4] +"\nOff Duty: " +i[5] + "\nSick: " +i[6] + "\nOperation: " +i[7] + "\nCourse: " +i[8] + "\nNAICC: " +i[9] + "\nNAFC: " +i[10] + "\nPass/Leave: " +i[11] + "\nHospital Admission: " +i[12])
            #return("exit")
            break

        else:
            print("Parade State not found")
            again = input("Do you want to try again?(yes/no): ")
            if again.lower() == "no":
                print("Goodbye")
                time.sleep(1)
                #return("exit")
                break

def list_paradestate():

    with sqlite3.connect("Project.db") as new:
        cursor = new.cursor()

    cursor.execute("SELECT * FROM columns")
    rows = cursor.fetchall()

    for row in rows:
        print("\nDAILY PARADE STATE AS AT " + str(row[0]) + "\nPosted Strength: " + str(row[1]) + "\nOn Parade: " + str(row[2]) + "\nOn duty: " + str(row[3]) + "\nOff Duty: " + str(row[4]) + "\nSick: " + str(row[5]) + "\nOperation: " + str(row[6]) + "\nCourse: " + str(row[7]) + "\nNAICC: " + str(row[8]) + "\nNAFC: " + str(row[9]) + "\nPass/Leave: " + str(row[10]) + "\nHospital Admission: " + str(row[11]))

    new.commit()

def delete_paradestate():
    while True:
        date = input("Please enter the date of the Parade State you want to delete: ")
        with sqlite3.connect("Project.db") as db:
            cursor = db.cursor()
        find_state = ("DELETE FROM columns WHERE date = ?")
        cursor.execute(find_state,[(date)])

        print("Parade state successfully deleted")

        db.commit()
        break

main_menu()
main_menu()
menu()

#db.commit