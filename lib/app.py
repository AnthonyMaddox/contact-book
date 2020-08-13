from model import *


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
            f"{show_all.index(i) + 1}. Name: {i.full_name}, Phone: {i.phone_number}, Email: {i.email} Birthday: {i.birthday}")
    return_menu = input("Return to option menu (y/n): ")
    if return_menu == "y":
        app()
    else:
        leave()


def find():
    find_one = input("Please Enter the contact's full name: ")
    show_one = Contact.select().where(Contact.full_name == find_one)
    show_one = list(show_one)
    for i in show_one:
        print(
            f"{show_one.index(i) + 1}. Name: {i.full_name}, Phone {i.phone_number}, Email: {i.email}, Birthday: {i.birthday}")
    return_menu = input("Return to option menu (y/n) ")
    if return_menu == "y":
        app()
    else:
        leave()


def create():
    new_full_name = input("Enter contact's full name: ")
    new_phone_number = input("Enter contact's phone number: ")
    new_email = input("Enter contact's email address: ")
    new_birthday = input("Enter contacts birthday(year-month-day): ")
    print("Created contact")

    new_contact = Contact(
        full_name=new_full_name,
        phone_number=new_phone_number,
        email=new_email,
        birthday=new_birthday
    )
    new_contact.save()


    return_menu = input("Return to option menu (y/n) ")
    if return_menu == "y":
        app()
    else:
        leave()


def delete():
    find_one = input("Please Enter the contact's full name: ")
    show_one = Contact.select().where(Contact.full_name == find_one)
    show_one = list(show_one)
    for i in show_one:
        print(
            f"Id: {i.id}, Name: {i.full_name}, Phone {i.phone_number}, Email: {i.email}, Birthday: {i.birthday}")
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
    #  contact_name = input(
    #      "Please enter the full name of the contact you want to delete(case sensitive): ")
    #  contact_to_delete = Contact.select().where(
    #      Contact.full_name == contact_name)
    #  contact_to_delete = list(contact_to_delete)
        # print(contact_to_delete)
  #   for i in contact_to_delete:
  #       print(
  #           f"Id: {i.id}, Name: {i.full_name}, Phone {i.phone_number}, Email: {i.email}, Birthday: {i.birthday}")
  #       check_sure = input(
  #           "If you're sure you want to delete this contact, enter contact Id or enter n: ")
  #       found_contact = Contact.get(Contact.id == check_sure)
  #       found_contact.delete_instance()


def leave():
    print("Leaving contact book")


app()
