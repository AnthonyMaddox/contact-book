# **Python CLI Contact Book**

## About:

###### This application is a representation of a contact book that runs in the command line interface. It has full CRUD operations allowing the user to display all contacts, find one contact, create a new contact and delete a contact.

## Technologies:

#### Peewee, PostgreSQL, Python

## Instructions:

* ###### Make sure you have Python 3, postgreSQL and pipenv installed on your computer

* ###### Open two command line interfaces and in one of them run:

```
psql
```

* ###### In your psql command line run:

```
CREATE DATABASE 'contacts';
```

* ###### Clone down this repo

* ###### In your other CLI, CD into the cloned repo's directory

* ###### CD into the lib directory

* ###### To install dependencies run:

```
pipenv install
```

* ###### To enter your virtual environment run:

```
pipenv shell
```

* ###### To seed initial data to contacts database, in your virtual environment run:

```
python3 seed.py
```

* ###### To start the app run:

```
python3 app.py
```

### Option Menu:

> ###### Upon running python3 app.py you will be given an option menu that appears like this:

```
Welcome to your contact book!
Enter 1 to display all contacts
Enter 2 to find a contact
Enter 3 to create new contact
Enter 4 to update a contact
Enter 5 to delete a contact
Enter 6 to leave contact book
```

* ###### Enter a number option to begin using the your contact book

* ###### You may delete initial contacts

### CRUD

###### *CREATE* a contact by entering their full name, phone number, email and birthday

###### *READ* by finding and displaying either all or one contact by name

###### *UPDATE* a contact by using the contact's Id and reentering all of the information for that contact

###### *DELETE* a contact by using contact's Id

### Author:

##### Anthony Maddox
