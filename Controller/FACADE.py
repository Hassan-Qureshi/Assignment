from DB.DB_Controller import *
from Rest.CRUD_Rest import *
import threading

class FACADE(threading.Thread):

    def __init__(self, method_name):
        self.method_name = method_name
    def run(self):
        FACADE_Main(self.method_name)

def FACADE_Main(self, method_name):
    if method_name == '__main__':
        pass


#print(type(DB_Controller.get_all()))

#index(DB_Controller.get_all())

