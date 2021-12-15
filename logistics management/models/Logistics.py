from mongoengine import Document, StringField, BooleanField

class Logistics(Document):
    logistics_id = StringField(max_length=100, required=True)
    logistics_manager_name = StringField(max_length=100, required=True)
    logistics_manager_title = StringField(max_length=100, required=True)
    logistics_manager_softdelete = BooleanField(default=False, required=True)



