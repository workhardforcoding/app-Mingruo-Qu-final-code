from mongoengine import Document, StringField, BooleanField

class ShoppingCart(Document):
    customer_id = StringField(max_length=100, required=True)
    item_id = StringField(max_length=100, required=True)
    product_id = StringField(max_length=100, required=True)
    selected_quantity = StringField(max_length=100, required=True)



