from mongoengine import Document, StringField

class ProductDetails(Document):
    product_id = StringField(max_length=100, required=True)
    product_desc = StringField(max_length=100, required=True)
    product_image = StringField(max_length=100, required=True)



