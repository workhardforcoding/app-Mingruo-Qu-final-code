from models.Logistics import Logistics
# default_logistics_id = ['l1', 'l2', 'l3']
default_logistics_manager_name = ['LogisticsManager1', 'LogisticsManager2', 'LogisticsManager3']
default_logistics_manager_title = ['Package Tracker', 'Selling Tracker', 'Order Tracker']

def get_logistics(logistics_id:str):
    if logistics_id is None:
        logistics_doc = Logistics.objects()
    else:
        logistics_doc = Logistics.objects(id=logistics_id)
    return logistics_doc

def create_logistics(logistics_manager_name: str, logistics_manager_title: str):  # Service for the POST() method
    logistics_doc = Logistics(logistics_manager_name=logistics_manager_name, logistics_manager_title=logistics_manager_title)  # Create a new rider object
    logistics_doc.save()  # Save the newly created rider object to the db
    return logistics_doc # Return the list of one rider object that was created

def update_logistics(logistics_id: str, logistics_manager_name: str, logistics_manager_title: str, logistics_manager_softdelete: bool):  # Service for the PATCH() method
    logistics_doc = Logistics.objects(id=logistics_id).first()  # extracting the first object from a list of one object
    logistics_doc.update(logistics_manager_name=logistics_manager_name, logistics_manager_title=logistics_manager_title, logistics_softdelete=logistics_manager_softdelete)
    logistics_doc.reload()  # Get the latest copy from the db
    return logistics_doc  # Return the list of one rider object that was updated

def init_logistics():  # Initialize the db with default riders if there are no existing riders
    existing_logistics = Logistics.objects()  # List of all rider objects in the db
    if len(existing_logistics) == 0:
        for i in range(3):
            create_logistics(default_logistics_manager_name[i],  default_logistics_manager_title[i])


