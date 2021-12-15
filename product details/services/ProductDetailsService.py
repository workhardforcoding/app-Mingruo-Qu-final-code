from models.ProductDetails import ProductDetails

default_product_id = ['p1','p2', 'p3']
default_product_desc = ['Size:64GB  |  Color:Blue  |  Service Provider:Unlocked  |  Product grade:Renewed', 'Size:64GB | Color:Green  |  Service Provider:Unlocked  |  Product grade:Renewed','Display	6.1-inch Liquid Retina HD display with True Tone']
default_product_image = ['iphone_13.jpg','iphone12.jpg','iphone11.jpg']

def get_productDetails(product_id:str):
    if product_id is None:
        product_details_doc = ProductDetails.objects()
    else:
        product_details_doc = ProductDetails.objects(id=product_id)
    return product_details_doc

def create_productDetails(product_id: str, product_desc: str, product_image: str):  # Service for the POST() method
    product_details_doc = ProductDetails(product_id=product_id, product_desc=product_desc, product_image=product_image)  # Create a new rider object
    product_details_doc.save()  # Save the newly created rider object to the db
    return product_details_doc # Return the list of one rider object that was created

def update_productDetails(product_id: str, product_desc: str, product_image: str):  # Service for the PATCH() method
    product_details_doc = ProductDetails.objects(product_id=product_id).first()  # extracting the first object from a list of one object
    product_details_doc.update(product_desc=product_desc, product_image=product_image )
    product_details_doc.reload()  # Get the latest copy from the db
    return product_details_doc  # Return the list of one rider object that was updated

def init_productDetails():  # Initialize the db with default riders if there are no existing riders
    existing_product_details = ProductDetails.objects()  # List of all rider objects in the db
    if len(existing_product_details) == 0:
        for i in range(3):
            create_productDetails(default_product_id[i], default_product_desc[i], default_product_image[i])


