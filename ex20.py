from sys import argv

script, input_file = argv

def print_all(f):
    print(f"First Lets print the whole file: \n {f.read()}")

def rewind(f,j):
    f.seek(j) # this funciton sets the pointer to first value in the file if passed = 0 , if passed = 1 than it sets the value at next charcter

def print_one_line(line_count,f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First Lets print the whole file:")

print_all(current_file)

print("Lets rewind the file:")

rewind(current_file,0)

print("Let's print three lines:")

current_line = 1
print_one_line(current_line, current_file)

current_line = current_line + 1
print_one_line(current_line, current_file)

current_line = current_line + 1
print_one_line(current_line, current_file)

print_one_line(current_line, current_file)

print_one_line(current_line, current_file)

rewind(current_file,60)

print_one_line(current_line, current_file)
rewind(current_file,0)
print_one_line(current_line, current_file)
