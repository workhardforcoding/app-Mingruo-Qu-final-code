from models.Product import Product
default_product = ['iPhone13', 'iPhone12', 'iPhone11']
default_price = ['1129', '729', '549']
default_quantity = ['10','10','10']

def get_product(product_id:str):
    if product_id is None:
        product_doc = Product.objects()
    else:
        product_doc = Product.objects(id=product_id)
    return product_doc

def create_product(product_name: str, product_price: str, product_quantity: str):  # Service for the POST() method
    product_doc = Product(name=product_name, price= product_price, quantity = product_quantity)  # Create a new rider object
    product_doc.save()  # Save the newly created rider object to the db
    return product_doc # Return the list of one rider object that was created

def update_product(product_id: str, product_price: str, product_quantity: str):  # Service for the PATCH() method
    product_doc = Product.objects(id=product_id).first()  # extracting the first object from a list of one object
    product_doc.update(price=product_price, quantity=product_quantity)
    product_doc.reload()  # Get the latest copy from the db
    return product_doc  # Return the list of one rider object that was updated

def init_products():  # Initialize the db with default riders if there are no existing riders
    existing_products = Product.objects()  # List of all rider objects in the db
    if len(existing_products) == 0:
        for i in range(3):
            create_product(default_product[i], default_price[i], default_quantity[i])


