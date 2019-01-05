print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')


poem = """
\t Time is money .\n Money is time.
\n\t one day no time and no money will be there.
"""

print("----------------")
print(poem)
print("----------------")

five = 10-2+6-9
print (f"The value should be five: {five}")

def secret_formula(started):
    jelly_beans = started/100
    jars = jelly_beans * 10
    return jelly_beans,jars

start_point = 10000

jelly_beans, jars =secret_formula(start_point)
#remember this is another way to format string
print("with starting_point of: {}".format(start_point))
#it's just like with an f"" string
print(f"The jelly_beans are {jelly_beans} and jars are {jars}")

start_point = start_point / 10

print("another way to store returned value is:")
formula = secret_formula(start_point)
print("We'd have {} beans and {} jars .".format(*formula))
