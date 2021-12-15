from mongoengine import Document, StringField

class Customer(Document):
    customer_id = StringField(max_length=100, required=True)
    name = StringField(max_length=100, required=True)
    email = StringField(max_length=100, required=True)



