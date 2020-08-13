from seed import *

def app():
    print("Welcome to your contact book!")
    user_action = input(
        "Enter 1 to display all contacts\nEnter 2 to find a contact\nEnter 3 to create new contact\nEnter 4 to delete a contact\nEnter 5 to leave contact book\nYour option:")
    if user_action == '1':
        display_all()
    elif user_action == '2':
        find()
    elif user_action == '3':
        create()
    elif user_action == '4':
        delete()
    elif user_action == '5':
        leave()
    else:
        print("please select from the options given")
        app()


def display_all():
    show_all = Contact.select()
    show_all = list(show_all)
    for i in show_all:
        print(
            f"{show_all.index(i) + 1}. Name: {i.full_name}, Phone: {i.phone_number}, Email: {i.email}")
    return_menu = input("Return to option menu (y/n) ")
    if return_menu == "y":
        app()


def find():
    find_one = input("Please Enter the contact's full name: ")
    show_one = Contact.select().where(Contact.full_name == find_one)
    show_one = list(show_one)
    for i in show_one:
        print(
            f"{show_one.index(i) + 1}. Name: {i.full_name}, Phone {i.phone_number}, Email: {i.email}")
    return_menu = input("Return to option menu (y/n) ")
    if return_menu == "y":
        app()

def create():
    print("Create contact")


def delete():
    print("Delete contact")


def leave():
    print("Leaving contact book")


app()
