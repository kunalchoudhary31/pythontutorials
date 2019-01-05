# create a mapping of state is abbrevation

states = {
        'Oregon' : 'OR',
        'Michigan' : 'MI',
        'Florida' : 'FL',
        'Newyork' : "NY"
}

# create a mapping of cities is abbrevation

cities = {
        'OR' : 'California',
        'MI' : 'Detroit',
        'FL' : 'Jacksonvile'
}


# add some more cities

cities['NY'] = 'Rachel'
cities['KU'] = 'Boston'

print(states)
print('*' * 10)
print(cities)

print(f"Newyork has state abbrevation : {states['Newyork']}")
print(f"NY state has : {cities['NY']}")

#do it by state than city dicitin

print(f"The city in 'Newyork' is :{cities[states['Newyork']]}")

#print every state abbrevation

print('*' * 10)

for stat,abbrev in  list(states.items()):
    print(f"{stat} is abbrevated as {abbrev}") #loop has started for items in the dict, for each items,state is a variable now

#get a variable by state that is not There

state = states.get('Texas')
# print('*' * 10)
# print(states)
if state:
    print("The value is : {}".format(state))
else:
    print("The state : {} is not there".format(state))
