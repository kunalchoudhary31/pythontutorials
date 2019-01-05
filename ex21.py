def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b
def sub(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b
def mul(a, b):
    print(f"Multiplying {a} * {b} ")
    return a * b
def div(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some maths with just functions")

age = add(30,5)
weight = sub(70,4)
height = mul(90,2)
iq = div(190,2)

print(f"Your age is {age}, height is {height}, weight is {weight}, iq is {iq}")
print("Here is a puzzle:")

what =  div(iq,add(age,sub(weight,mul(height,5))))

print(f"That becomes {int(what)} can you do it by hand")
