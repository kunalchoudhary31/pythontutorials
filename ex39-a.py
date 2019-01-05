state = {
        'Madhya Pradesh' : 'MP',
        'Rajasthan' : 'RJ',
        'Kerala' : 'KR',
        'Punjab' : 'PB'
        }

print("\"" * 10)
print("The state dict is :",state)
cities = {
        'MP' : 'Indore',
        'RJ' : 'Jaipur'
        }

print("\"" * 10)
print("The cities orginal :", cities)

print("\"" * 10)
#Addition of new cities and new state

state['Haryana'] = 'HR'
cities['HR'] = 'Rohtak'
cities['KR'] = 'Kochi'
cities['PB'] = 'Chandigarh'

print("The cities now are :", cities)

print("state Kerala has abbrev :",state['Kerala'])
print("state Rajasthan has abbrev :",state['Rajasthan'])

print("Dict state in the sorted way is :", sorted(state))
list_state = list(state.items())
print("The string values of Dict are :",list(state.items()))
print("The the item at 0 position is :", list_state[0])
print("Lenght is:", len(state))
print("Lenght is:", str(state))
print("Type is", type(state))

for states,abbrev in list(state.items()):
    print("The state {} and it's abbrev is {}".format(states,abbrev))
    print("The states is: {} , the abbrev is : {} , The cities is {}".format(states,abbrev,cities[abbrev]))

for keyss in state.keys():
    print(f"The keys are: {keyss}")

for gh in state.values():
    print(f"The {gh}")
