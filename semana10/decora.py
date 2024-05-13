from functools import wraps


def my_decorator(func):
    @wraps(func)
    def warpped(*args,**kwargs):
        print("antes")
        print(**kwargs)
        result=func(*args,**kwargs)
        print("despues")
        return result
    return warpped


@my_decorator
def greet(name):
    """saludo"""
    print(f"hola, {name}!")
    
greet("juan")
print(greet.__name__)
print(greet.__doc__)


