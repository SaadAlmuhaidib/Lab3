# Decorator function
def repeat_call(num_repetitions):
    def decorator_func(func):
        def wrapper():
            for _ in range(num_repetitions):
                func()
        return wrapper
    return decorator_func

x = int(input("Enter the number of repetitions: "))

@repeat_call(x)
def hello():
    print("Hello")

hello()