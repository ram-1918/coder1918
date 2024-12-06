from abc import ABC, abstractmethod

class Logistics(ABC):
    # declares a method, that enforces subclasses to implement their own method
    @abstractmethod
    def factory_method(self):
        pass
    # app the parents methods like the one below can be accessed by its child classes
    def createProduct(self):
        product = self.factory_method()
        return f"Request made to Logistics Class to create a product --> {product.designProduct()}"

class TruckLogistics(Logistics):
    def factory_method(self):
        print(f"Truck factory method produces trucks!")
        truckObj = Trucks()
        return truckObj

class ShipLogistics(Logistics):
    def factory_method(self):
        print(f"Ship factory method produces ships!")
        shipObj = Ships()
        return shipObj

class TransportCompany(ABC):
    @abstractmethod
    def designProduct(self):
        pass

class Trucks(TransportCompany):
    def designProduct(self):
        return f"Request recieved to design Trucks!"

class Ships(TransportCompany):
    def designProduct(self):
        return f"Request recieved to design Ships!"

def client_code(obj):
    print(obj.createProduct())

if __name__ == '__main__':
    truckObj = TruckLogistics()
    client_code(truckObj)

    client_code(ShipLogistics())
