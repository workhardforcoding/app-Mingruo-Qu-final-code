from models.Customer import Customer
default_customer = ['Iris', 'Sam', 'Bill']
default_bankAccount = ['1111111111', '2222222222', '3333333333']

def get_customer(customer_id:str):
    if customer_id is None:
        customer_doc = Customer.objects()
    else:
        customer_doc = Customer.objects(id=customer_id)
    return customer_doc

def create_customer(customer_name: str, customer_bankaccount: str):  # Service for the POST() method
    customer_doc = Customer(customer_name=customer_name, customer_bankaccount=customer_bankaccount)  # Create a new rider object
    customer_doc.save()  # Save the newly created rider object to the db
    return customer_doc # Return the list of one rider object that was created

def update_customer(customer_id: str, customer_name: str, customer_bankaccount: str, customer_softdelete:bool):  # Service for the PATCH() method
    customer_doc = Customer.objects(id=customer_id).first()  # extracting the first object from a list of one object
    customer_doc.update(customer_name=customer_name, customer_bankaccount=customer_bankaccount, customer_softdelete=customer_softdelete)
    customer_doc.reload()  # Get the latest copy from the db
    return customer_doc  # Return the list of one rider object that was updated

def init_customers():  # Initialize the db with default riders if there are no existing riders
    existing_customers = Customer.objects()  # List of all rider objects in the db
    if len(existing_customers) == 0:
        for i in range(3):
            create_customer(default_customer[i], default_bankAccount[i])


