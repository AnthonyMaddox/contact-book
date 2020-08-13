from peewee import *

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

#create
db.drop_tables([Contact])
db.create_tables([Contact])

anthony = Contact(full_name="Anthony Maddox", phone_number="15417281280", email="anthonyjmaddox@gmail.com")
anthony.save()
rebecca = Contact(full_name="Rebecca Maddox", phone_number="13018480637", email="rekercher122@gmail.com")
rebecca.save()

#reading
# grabbing_anthony = Contact.get(Contact.full_name == 'Anthony Maddox')

# print(grabbing_anthony.full_name)