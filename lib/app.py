from model import *


def app():
    print("Welcome to your contact book!")
    user_action = input(
        "Enter 1 to display all contacts\nEnter 2 to find a contact by first name\nEnter 3 to create new contact\nEnter 4 to update a contact\nEnter 5 to delete a contact\nEnter 6 to leave contact book\nYour option: ")
    if user_action == '1':
        display_all()
    elif user_action == '2':
        find()
    elif user_action == '3':
        create()
    elif user_action == '4':
        update()
    elif user_action == '5':
        delete()
    elif user_action == '6':
        leave()
    else:
        print("Please select from the options given...")
        app()


def display_all():
    show_all = Contact.select()
    show_all = list(show_all)
    for i in show_all:
        print(
            f"{show_all.index(i) + 1}. Name: {i.first_name} {i.last_name} Phone: {i.phone_number}, Email: {i.email} Birthday: {i.birthday}")
    return_menu = input("Return to option menu (y/n): ")
    if return_menu == "y":
        app()
    else:
        leave()


def find():
    find_one = input("Please Enter the contact's first name: ")
    show_one = Contact.select().where(Contact.first_name == find_one)
    show_one = list(show_one)
    for i in show_one:
        print(
            f"{show_one.index(i) + 1}. Name: {i.first_name} {i.last_name} Phone {i.phone_number}, Email: {i.email}, Birthday: {i.birthday}")
    return_menu = input("Return to option menu (y/n): ")
    if return_menu == "y":
        app()
    else:
        leave()


def create():
    new_first_name = input("Enter contact's first name: ")
    new_last_name = input("Enter contact's last name: ")
    new_phone_number = input("Enter contact's phone number: ")
    new_email = input("Enter contact's email address: ")
    new_birthday = input("Enter contacts birthday(year-month-day): ")

    new_contact = Contact(
        first_name=new_first_name,
        last_name=new_last_name,
        phone_number=new_phone_number,
        email=new_email,
        birthday=new_birthday
    )
    new_contact.save()
    print("Created contact")

    return_menu = input("Return to option menu (y/n): ")
    if return_menu == "y":
        app()
    else:
        leave()


def delete():
    find_one = input("Please Enter the contact's first name: ")
    show_one = Contact.select().where(Contact.first_name == find_one)
    show_one = list(show_one)
    for i in show_one:
        print(
            f"Id: {i.id}, Name: {i.first_name} {i.last_name}, Phone {i.phone_number}, Email: {i.email}, Birthday: {i.birthday}")
    check_sure = input(
        "If you're sure you want to delete this contact, enter contact Id or enter n: ")
    if check_sure == 'n':
        app()
    else:
        found_contact = Contact.get(Contact.id == check_sure)
        found_contact.delete_instance()
        print("Deleted contact")
    return_menu = input("Return to option menu (y/n): ")
    if return_menu == "y":
        app()
    else:
        leave()


def update():
    find_one = input("Please Enter the contact's first name: ")
    show_one = Contact.select().where(Contact.first_name == find_one)
    show_one = list(show_one)
    for i in show_one:
        print(
            f"Id: {i.id}, Name: {i.first_name} {i.last_name}, Phone {i.phone_number}, Email: {i.email}, Birthday: {i.birthday}")
    check_sure = input(
        "If you're sure you want to update this contact, enter contact Id or enter n: ")
    if check_sure == 'n':
        app()
    else:
        found_contact = Contact.get(Contact.id == check_sure)
        new_first_name = input("Update contact's first name to: ")
        new_last_name = input("Update contact's last name to: ")
        new_phone_number = input("Update contact's phone number to: ")
        new_email = input("Update contact's email address to: ")
        new_birthday = input("Update contact's birthday(year-month-day) to: ")
        found_contact.first_name = new_first_name
        found_contact.last_name = new_last_name
        found_contact.phone_number = new_phone_number
        found_contact.email = new_email
        found_contact.birthday = new_birthday
        found_contact.save()
        print("Updated contact")
    return_menu = input("Return to option menu (y/n): ")
    if return_menu == "y":
        app()
    else:
        leave()


def leave():
    print("Leaving contact book")


app()
