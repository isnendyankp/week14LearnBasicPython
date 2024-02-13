def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Using the decorator
@my_decorator
def say_whee():
    print("Whee!")
# say_whee = my_decorator(say_whee)

# Calling the decorated function
say_whee()


# hasoutput:
# Something is happening before the function is called.
# Whee!
# Something is happening after the function is called.