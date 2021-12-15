from models.ShoppingCart import ShoppingCart

default_customer_id = ['c123']
default_item_id = ['i1', 'i2', 'i3']
default_product_id = ['p1','p2', 'p3']
default_selected_quantity = ['1','10','2']

def get_shoppingCart(customer_id:str):
    if customer_id is None:
        shoppingcart_doc = ShoppingCart.objects()
    else:
        shoppingcart_doc = ShoppingCart.objects(id=customer_id)
    return shoppingcart_doc

def create_items(customer_id: str, item_id: str, product_id: str, selected_quantity:str):  # Service for the POST() method
    shoppingcart_doc = ShoppingCart(customer_id=customer_id, item_id=item_id, product_id = product_id, selected_quantity=selected_quantity)  # Create a new rider object
    shoppingcart_doc.save()  # Save the newly created rider object to the db
    return shoppingcart_doc # Return the list of one rider object that was created

def update_items(customer_id: str, item_id: str, selected_quantity: str):  # Service for the PATCH() method
    shoppingcart_doc = ShoppingCart.objects(customer_id=customer_id, item_id=item_id).first()  # extracting the first object from a list of one object
    shoppingcart_doc.update(selected_quantity=selected_quantity)
    shoppingcart_doc.reload()  # Get the latest copy from the db
    return shoppingcart_doc  # Return the list of one rider object that was updated

def delete_items(customer_id: str, item_id:str):
    shoppingcart_doc = ShoppingCart.objects(customer_id=customer_id,item_id=item_id).first()  # extracting the first object from a list of one object
    shoppingcart_doc.delete(item_id=item_id)
    shoppingcart_doc.reload()  # Get the latest copy from the db
    return shoppingcart_doc  # Return the list of one rider object that was updated

def init_shoppingcart():  # Initialize the db with default riders if there are no existing riders
    existing_shoppingcart = ShoppingCart.objects()  # List of all rider objects in the db
    if len(existing_shoppingcart) == 0:
        for i in range(3):
            create_items(default_customer_id[i], default_item_id[i], default_product_id[i], default_selected_quantity[i])


