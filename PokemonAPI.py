import requests as r
pokemon = ['ditto', 'charizard', 'pikachu', 'blastoise', 'scyther', 'hitmonchan', 'zapdos', 'gyarados', 'lugia', 'machamp', 'raichu', 'venusaur', 'magikarp', 'alakazam', 'mewtwo', 'mew', 'geodude', 'haunter', 'weedle', 'moltres', 'snorlax', 'articuno']

# I want to replace each pokemon name with my pokemon dict
# Key word there: replace - I need access to my list indexes in order to be able to change their values

for index in range(len(pokemon)):
    
    data = r.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon[index]}')
    print(data)

    if data.status_code == 200:
        print('Pokemon Info:')
        data = data.json()
        pokemon_dict = {}
        names = pokemon_dict['Name'] = data['forms'][0]['name']
        ability1 = pokemon_dict['Ability_1'] = data['abilities'][0]['ability']['name']
        ability2 =pokemon_dict['ability_2'] = data['abilities'][1]['ability']['name']
        #pokemon_dict['ability_2'] = data['abilities'][2]['ability']['name']
        weight = pokemon_dict['Weight'] = data['weight']
        poketype = pokemon_dict['Type'] = data['types'][0]['type']['name']
    print(pokemon_dict)
    pokemon[index] = pokemon_dict
    
# ok for loop is done, we're outside of it
pokemon