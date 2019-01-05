from sys import argv #importing module argv

script, file_name = argv #declare variables for command line input

txt = open(file_name) #declare a variable and initalize it's value to an stream

print(f"Here is your file {file_name}:")
print(txt.read())

#print("Type the filename again:")
#likes = input("> ")

#txt_again = open(likes)

#print(txt_again.read())
