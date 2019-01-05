name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_in_centimeters = height * 2.54 # height in centimeters
weight_in_pounds = round(weight * 0.453592)

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall")
print(f"He's {weight} pounds heavy")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes")
print(f"His teeth are usually {teeth} depending upon the coffee.")
print(f"My height {height_in_centimeters} in centimeters")
print(f"My weight is {weight_in_pounds} kg")
#this line is tricky , try to get it exactly right

total = age + height + weight

print(f"If I add {age}, {height}, and {weight} I get {total}.")
