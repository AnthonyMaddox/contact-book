from peewee import *
from datetime import date

db = PostgresqlDatabase('contacts', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Contact(BaseModel):
    full_name = CharField()
    phone_number = CharField()
    email = CharField()
    birthday = DateField()


#db.drop_tables([Contact])
db.create_tables([Contact])

# create


# reading
# grabbing_anthony = Contact.get(Contact.full_name == 'Anthony Maddox')

# print(grabbing_anthony.full_name)
