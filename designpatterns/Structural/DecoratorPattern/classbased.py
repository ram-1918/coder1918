# class BaseClass():
#     def number(self):
#         return 5

# class SquareDecorator():
#     def __init__(self, baseNumber):
#         self.baseNumber = baseNumber
    
#     def number(self):
#         return self.baseNumber.number()**2

# class CubeDecorator():
#     def __init__(self, baseNumber):
#         self.baseNumber = baseNumber
    
#     def number(self):
#         return self.baseNumber.number()**3
    
# baseobj = BaseClass()
# print(baseobj.number())
# squareobj = SquareDecorator(baseobj)
# print(squareobj.number())
# cubeobj = CubeDecorator(squareobj)
# print(cubeobj.number())

# Class-based Decorator Pattern

class OrderAPI():
    def ordersLogic(self):
        return f"Product orders logic executed!"

class PaymentsAPI():
    def paymentsLogic(self):
        return f"Payment Logic Executed!"

class LoginAPI():
    def __init__(self, componentObj, funcName):
        self._component = componentObj
        self._funcName = funcName
    
    def authenticationLogic(self):
        print(f"Authentication Logic Executed and User is Authorized!")
        print(f"output of {self._funcName.__name__} from Authentication method: {self._funcName()}\n")

print(f"\nAuthentication system with Decorator Design Patterns!\n")

ordersObj = OrderAPI()
print(f"Output of {ordersObj.ordersLogic.__name__} from OrdersAPI object: {ordersObj.ordersLogic()} \n")

paymentsObj = PaymentsAPI()
print(f"Output of {paymentsObj.paymentsLogic.__name__} from PaymentsAPI object: {paymentsObj.paymentsLogic()} \n")

loginObj = LoginAPI(ordersObj, ordersObj.ordersLogic)
loginObj.authenticationLogic()

loginObj = LoginAPI(paymentsObj, paymentsObj.paymentsLogic)
loginObj.authenticationLogic()
