the_count = [1,2,3,4]
change = [1,'apple','2','orange']

for number in the_count:
    print(f"The number is {number}")

for changes in change:
    print(f"The mixed list is {changes}")

elememts = []

for i in range(0, 5):
    print(f"Adding {i} to the list")
    elememts.append(i)

for i1 in elememts:
    print(f"The elememts are: {i1}")

print(elememts)

elememts2 = []

for i in range(0, 6):
    elememts2.append(i)

elememts1 = []

elememts1.append(elememts)
elememts1.append(elememts2)

print(elememts1)
