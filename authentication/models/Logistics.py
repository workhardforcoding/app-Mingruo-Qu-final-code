from mongoengine import Document, StringField

class Logistics(Document):
    logistics_id = StringField(max_length=100, required=True)
    name = StringField(max_length=100, required=True)
    email = StringField(max_length=100, required=True)



