ten_things = "Apple Oranges Crows Telephone Light Sugar"

print("Wait not 10 things. Let's fix that.")

stuff = ten_things.split(" ")
#print(type(stuff))
more_stuff = ['Day','Night','Moon','Sun','Corn','Banana','Girl','Boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print(f"Adding {next_one} to list")
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go:",stuff)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
