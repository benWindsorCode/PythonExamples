x = ["h",2,{'a':3},4]

for i, val in enumerate(x):
    print(f"{i} : {val}")

y = [(1,4,5), (2, 3, 4), (5, 2, 12)]
for a,b,c in y:
    print(f"({a}, {b}, {c})")

def enum_result(func):
    def inner(*args, **kwargs):
        out = func(*args, **kwargs)
        for i, v in enumerate(out):
            print(f"{i}: {v}")
        return out
    return inner

@enum_result
def dummy_list_return(x=0):
    return [1,5,3,x]

dummy_list_return()