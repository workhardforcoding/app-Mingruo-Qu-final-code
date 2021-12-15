from models.Logistics import Logistics
import uuid
# default_logistics_id = ['l1', 'l2', 'l3']
default_logistics_name = ['LogisticsManager1', 'LogisticsManager2', 'LogisticsManager3']
default_logistics_email = ['logistics1@walmart.com', 'logistics2@walmart.com', 'logistics3@walmart.com']

def get_logistics_by_id(logistics_id:str):
    if logistics_id is None:
        logistics_doc = Logistics.objects()
    else:
        logistics_doc = Logistics.objects(id=logistics_id)
    return logistics_doc

def create_logistics(name: str, email: str):  # Service for the POST() method
    while True:
        gen_logistics_id = str(uuid.uuid4())[0:7]
        if len(Logistics.objects(logistics_id=gen_logistics_id)) == 0:
            break
    logistics_doc = Logistics(logistics_id = gen_logistics_id, name=name, email=email)  # Create a new rider object
    logistics_doc.save()  # Save the newly created rider object to the db
    return logistics_doc # Return the list of one rider object that was created

def update_logistics(logistics_id: str, logistics_name: str, logistics_email: str):  # Service for the PATCH() method
    logistics_doc = Logistics.objects(id=logistics_id).first()  # extracting the first object from a list of one object
    logistics_doc.update(name=logistics_name)
    logistics_doc.reload()  # Get the latest copy from the db
    return logistics_doc  # Return the list of one rider object that was updated

def init_logistics():  # Initialize the db with default riders if there are no existing riders
    existing_logistics = Logistics.objects()  # List of all rider objects in the db
    if len(existing_logistics) == 0:
        for i in range(3):
            create_logistics(default_logistics_name[i],  default_logistics_email[i])


