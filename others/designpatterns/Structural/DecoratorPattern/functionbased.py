# Function based Decorator Pattern
def login_required(apiFunc):
    print("Outside wrapper!")
    def loginWrapper():
        print(f"Login Logic Executed and user is authorized!")
        print(apiFunc())
    print(f"Address of loginWrapper function: {id(loginWrapper)}")
    return loginWrapper

# With decorators
@login_required
def OrdersAPI():
    return f"Orders API Logic executed!"

OrdersAPI()
print(f"Address of OrdersAPI function: {id(OrdersAPI)}")

# Without decorators
def OrdersAPI():
    return f"Orders API Logic executed without decorator!"

decorated_OrdersAPI = login_required(OrdersAPI) # assiging inner function reference to a variable
decorated_OrdersAPI()

# in the line where @login_required exists - 
# login_required() executes without being called and returns its inner function(loginWrapper)
# when we explicitly call the function(ordersAPI) which is decorated, only then inner function(loginWrapper) executes
# loginWrapper acts as OrdersAPI and viceversa (LoginWrapper references OrdersAPI)



    
