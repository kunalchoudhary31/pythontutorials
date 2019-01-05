from sys import argv

script, from_file, to_file = argv

#indata = open(from_file).read()
open(to_file,'w').write(open(from_file).read())
