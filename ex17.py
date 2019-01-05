from sys import argv  #importing sys package and argv variable
from os.path import exists #importing path package and exists variable

script, from_file, to_file = argv  #declaring command line variable

print(f"Copying from {from_file} to {to_file}") #printing the statemet

#we could these two on one line, how?

#in_file = open(from_file) #open file in read only mode . the object returned is stored in a variable
#indata = in_file.read() #file is read and stored in indata variable

indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long") #the length of a file is stored

print(f"Does the output file exist? {exists(to_file)}") #checks weather the file is present or not
print("Ready, hit RETURN to continue, CTRL-C to abort.")

input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done")

out_file.close()
#in_file.close()
