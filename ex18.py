# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1} arg2: {arg2}")

# we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1} arg2: {arg2}")

# we can do this also
def print_one(arg1):
    print(f"arg1: {arg1} ")

# this one takes no argument
def print_none():
    print("Hello")


print_two("Zed","Shaw")
print_one("Zed")
print_two_again("Zed","Shaw")
print_none()
