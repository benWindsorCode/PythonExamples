from typing import List

# A decorator which takes a mode on if to print the function args upper or lowercase
def input_dec(mode: str):
    if mode != "UPPER" and mode != "LOWER":
        print(f"mode: {mode} must be UPPER or LOWER")
        raise RuntimeError

    def input_dec_with_mode(func):
        def inner_wrapper(*args, **kwargs):
            strToPrint = f"args: {args}, kwargs: {kwargs}"
            strToPrint = strToPrint.lower() if mode == "LOWER" else strToPrint.upper()
            print(strToPrint)
            return func(*args, **kwargs)

        return inner_wrapper

    return input_dec_with_mode

@input_dec(mode="LOWER")
def square(input: int) -> int:
    return input*input

print(square(2))



# A generator that takes a list and turns it into a squared list
def my_gen(input: List[int]):
    print("Generator starting")
    for item in input:
        yield item * item
    print("Generator done")

gen_square = my_gen([1, 2, 3, 4])
for num in gen_square:
    print(f"Square: {num}")

