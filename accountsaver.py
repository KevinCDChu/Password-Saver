import os
import tkinter
import pickle
import time
import datetime
import pyperclip


accounts = {}
now = datetime.datetime.now()


def save_dict():
    with open("b.txt", "wb") as b:
        pickle.dump(accounts, b)


def load_dict():
    if os.path.isfile(os.getcwd() + "\\b.txt"):
        with open("b.txt", "rb") as b:
            return pickle.load(b)
    else:
        return {}


def input_account():
    nam = input("Enter the name of the account: ")
    use = input("Please enter the username: ")
    pas = input("Please enter the password: ")
    if nam not in accounts:
        print("Processing... ")
        time.sleep(2)
        accounts[nam] = [use, pas]
        return nam
    else:
        print("That account already exists")


def addinfo():
    with open("accountsaver.txt", "w") as account:
        for key in sorted(accounts.keys()):
            account.write("Name: " + key + "\n")
            account.write("Username: " + accounts[key][0] + "\n")
            account.write("Password: " + accounts[key][1] + "\n")
            account.write("\n")


def log(key, condition, changel):
    with open("log.txt", "a") as record:
        if condition == "add":
            record.write(
                "Added %s, with %s as username and %s as password on %s" % (
                    key, accounts[key][0], accounts[key][1], now.strftime(
                        "%Y-%m-%d")))
        elif condition == "del":
            record.write(
                "Deleted %s, with %s as username and %s as password on %s" % (
                    key, accounts[key][0], accounts[key][1], now.strftime(
                        "%Y-%m-%d")))
        elif condition == "change":
            record.write(
                "Changed %s, with %s as username and %s as password to" % (
                    changel[0], changel[1], changel[2]))
            record.write(
                "%s with %s as username and %s as password on %s" % (
                    key, accounts[key][0], accounts[key][1], now.strftime(
                        "%Y-%m-%d")))


def changelog(key):
    return [key, accounts[key][0], accounts[key][1]]


def amend(name):
    while True:
        user = input("What piece of information would you like to change "
                     + "(n for name, u for username and p for password): ")
        if user.upper() == "N":
            namechange = input("What would you like the new name to be: ")
            accounts[namechange] = accounts[name]
            del accounts[name]
            break
        elif user.upper() == "U":
            userchange = input("What would you like the new username to be: ")
            accounts[name] = [userchange, accounts[name][1]]
            break
        elif user.upper() == "P":
            passchange = input("What would you like the new password to be: ")
            accounts[name] = [accounts[name][0], passchange]
            break
        else:
            print("Invalid choice, please try again")


def delete():
    while True:
        delet = input("Enter the account you would like to delete: ")
        if delet in accounts:
            del accounts[delet]
            break
        else:
            print("Invalid choice, please try again")


def view():
    copy = input("Enter the account you would like to view: ")
    while True:
        if copy in accounts:
            print("The account name is %s, its username is %s and its password is %s" % (
                copy, accounts[copy][0], accounts[copy][1]))
            user_input = input("Enter N to copy name, U to copy username, P to copy password and E to exit: ")
            if user_input.upper() == "N":
                pyperclip.copy(copy)
                break
            elif user_input.upper() == "U":
                pyperclip.copy(accounts[copy][0])
                break
            elif user_input.upper() == "P":
                pyperclip.copy(accounts[copy][1])
                break
            elif user_input.upper() == "E":
                break
            else:
                print("Invalid input, please try again")
        else:
            print("Invalid input, please try again")


def startaccount():
    start = True
    while start:
        user_choice = input(
            "Input A to add account, C to change account, D to delete account, V to view account and E to exit: ")
        global accounts
        accounts = load_dict()
        if user_choice.upper() == "E":
            start = False
        elif user_choice.upper() == "A":
            input_account()
            save_dict()
            addinfo()
        elif user_choice.upper() == "C":
            name = input("Enter the account you would like to change: ")
            if name in accounts:
                amend(name)
                save_dict()
                addinfo()
            else:
                print("Invalid command, please try again")
        elif user_choice.upper() == "D":
            delete()
            save_dict()
            addinfo()
        elif user_choice.upper() == "L":
            print(accounts)
        elif user_choice.upper() == "V":
            view()
        else:
            print("Invalid command, please try again")


startaccount()


# TODO implement the log function
# TODO implement the website function
# TODO implement the difflib(similarity detector) function
# TODO implement windows using tkinker
