

# First: Function Decorators
"""

"""
import logging
def validation(func):
    def wrapper(*args, **kwargs):
        # here will be validation steps
        logging.info("validation pased successfully")
        result = func(*args, **kwargs)
        return result
    return wrapper

@validation
def get_order(order_id):
    if not order_id:
        raise Exception("There is no order id provided")
    
    # handle getting order
    order = {
        "title": "bag",
        "size": 2,
        "order_id": order_id,
    }
    return order

print(get_order(1))



# Second: Class Decorators
class AccessControlDecorator:
    def __init__(self, allowed_roles):
        self.allowed_roles = allowed_roles

    def __call__(self, cls):
        original_methods = {}

        # Wrap each method in the class
        for name, method in cls.__dict__.items():
            if callable(method):
                original_methods[name] = method
                setattr(cls, name, self._create_wrapper(name, method))

        # Create a new constructor for the class
        def new_init(self, *args, **kwargs):
            self._check_access()
            original_methods['__init__'](self, *args, **kwargs)

        original_methods['__init__'] = cls.__init__
        setattr(cls, '__init__', new_init)

        # Include the _check_access method in the class
        cls._check_access = self._check_access

        return cls

    def _create_wrapper(self, name, method):
        def wrapper(*args, **kwargs):
            self._check_access()
            return method(*args, **kwargs)

        return wrapper

    def _check_access(self):
        # Check the access control logic here (e.g., user roles, permissions)
        # For simplicity, let's assume a role-based access control check
        if not self._is_allowed_role():
            raise PermissionError("Access denied")

    def _is_allowed_role(self):
        # Check if the user's role is allowed based on self.allowed_roles
        # Implement your access control logic here
        # For demonstration purposes, let's assume the allowed roles are 'admin' and 'manager'
        allowed_roles = {'admin', 'manager'}
        user_role = 'admin'  # Assume the user role is 'admin'
        return user_role in allowed_roles


@AccessControlDecorator(allowed_roles={'admin'})
class SecureClass:
    def __init__(self):
        print("SecureClass initialized")

    def public_method(self):
        print("Public method called")

    def sensitive_method(self):
        print("Sensitive method called")


secure_obj = SecureClass()
secure_obj.public_method()  # Output: Public method called
secure_obj.sensitive_method()  # Output: Sensitive method called


