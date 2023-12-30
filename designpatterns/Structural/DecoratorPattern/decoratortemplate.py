class Component():
    def operations(self):
        pass

class Concretecomponent(Component):
    def operations(self):
        return (f'ConcreteComponent')

class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component):
        self._component = component
        # print(f'Decorator init func {self._component}')

    @property
    def component(self) -> Component:
        return self._component
    
    # def operations(self):
    #     print(f'Operations method inside decorators')
    #     return self._component.operations()

class DecoratorA(Decorator):
    def operations(self):
        return (f'DecoratorA({self.component.operations()})')

class DecoratorB(Decorator):
    def operations(self):
        return (f'DecoratorB({self.component.operations()})')

def client_code(component: Component) -> None:
    print(f'Client function: {component.operations()}')

    

if __name__ == '__main__':
    print('Decorator Implementation!')
    obj = Concretecomponent()
    client_code(obj)
    print(f'Object with decorators')
    decorator1 = DecoratorA(obj)
    decorator2 = DecoratorB(decorator1)
    client_code(decorator2)