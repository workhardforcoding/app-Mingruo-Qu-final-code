from mongoengine import Document, StringField, BooleanField

class Customer(Document):
    customer_name = StringField(max_length=100, required=True)
    customer_bankaccount = StringField(max_length=100, required=True)
    customer_softdelete = BooleanField(required=True, default=False)



