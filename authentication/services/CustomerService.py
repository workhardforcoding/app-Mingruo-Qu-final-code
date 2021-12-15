from models.Customer import Customer
import uuid

default_customer = ['Karima', 'Manuja', 'Mingruo']
default_email = ['karima@cmu.edu', 'manuja@cmu.edu','mingruo@cmu.edu']

def get_customer_by_id(customer_id:str):
    if customer_id is None:
        customer_doc = Customer.objects()
    else:
        customer_doc = Customer.objects(id=customer_id)
    return customer_doc

def get_customers_by_email(email:str):
    if email is None:
        customer_doc = Customer.objects()
    else:
        customer_doc = Customer.objects(id=email)
    return customer_doc

def create_customer(name: str, email: str):  # Service for the POST() method
    while True:
        gen_customer_id = str(uuid.uuid4())[0:7]
        if len(Customer.objects(customer_id=gen_customer_id)) == 0:
            break
    customer_doc = Customer(customer_id=gen_customer_id, name = name, email=email)  # Create a new rider object
    customer_doc.save()  # Save the newly created rider object to the db
    return customer_doc # Return the list of one rider object that was created

def update_customer(customer_id: str, name: str):  # Service for the PATCH() method
    customer_doc = Customer.objects(id=customer_id).first()  # extracting the first object from a list of one object
    customer_doc.update(name=name)
    customer_doc.reload()  # Get the latest copy from the db
    return customer_doc  # Return the list of one rider object that was updated

def init_customers():  # Initialize the db with default riders if there are no existing riders
    existing_customers = Customer.objects()  # List of all rider objects in the db
    if len(existing_customers) == 0:
        for i in range(3):
            create_customer(default_customer[i], default_email[i])


