import functools
#Source https://realpython.com/primer-on-python-decorators/

def test_dec(func):
    def inner_func():
        print("Here")
        func()
        print("After Func")

    return inner_func

def test_func():
    print("Inside Func")

# You can set this up manually
test_func = test_dec(test_func)
test_func()

# Or with syntactic sugar
@test_dec
def test_func_2():
    print("Inside Test Func 2")

test_func_2()

# Now with args and return
def test_dec_2(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice

@test_dec_2
def test_func_3(input: int) -> int:
    print("In Test Func 3")
    return input + 2

print(test_func_3(3))
print(f"\n\nInfo on test_func_3 with test_dec_2:")
print(help(test_func_3))

# We can use a decorator to ensure test_func_3 remembers who it is even in a decorator
def test_dec_3(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice

@test_dec_3
def test_func_4(input):
    return input+1

print(help(test_func_4))

# You can cache values too

@functools.lru_cache(maxsize=4)
def fib(n):
    print(f"calculating fib-{n}")
    if n < 2:
        return n

    return fib(n-1)+fib(n-2)

out = fib(5)
print(out)
out = fib(4)
print(out)

# If you want your decorator to take an argument then you need to give it two inner functions
def dec_say_endpiont(endpoint_name):
    def decorator_inner(func):
        @functools.wraps(func)
        def say_endpoint_name_then_func(*args, **kwargs):
            print(f"From endpoint: {endpoint_name}")
            return func(*args, **kwargs)
        return say_endpoint_name_then_func
    return decorator_inner

@dec_say_endpiont("start/")
def some_func(input):
    print(f"In func with input: {input}")
    return input+3

print(some_func(7))

# You can also use a class for a decorator, as long as you use the __call__ function
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"Calls made: {self.calls}")
        return self.func(*args, **kwargs)

@CountCalls
def random_func():
    print("In Func")

random_func()
random_func()