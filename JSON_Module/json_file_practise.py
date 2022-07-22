import json

with open('new_state.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], '  ', state['abbreviation'])
    del state['area_codes']

with open('new_states_file.json', 'w') as write:
    json.dump(data, write, indent=2)


