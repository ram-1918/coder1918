from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        return f"Creator Class: {product.operation()}"

class ConcreteCreatorA(Creator):
    def factory_method(self):
        print(f"Default code from factory method of Creator A !")
        productA = ConcreteProductA()
        return productA

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteProductA(Product):
    def operation(self):
        return f"Operation from Product A"    

def client_code(creator: Creator):
    print(creator.some_operation())

if __name__ == '__main__':
    obj = ConcreteCreatorA()
    client_code(obj)