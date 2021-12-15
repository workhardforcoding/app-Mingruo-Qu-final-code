from mongoengine import Document, StringField, BooleanField

class Product(Document):
    name = StringField(max_length=100, required=True)
    price = StringField(max_length=100, required=True)
    quantity = StringField(max_length=100, required=True)



