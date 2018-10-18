import sqlite3

pokedex = sqlite3.connect('pokedex.db')
pokecursor = pokedex.cursor()

pokecursor.execute('''select POKEMON_ABILITIES.pokemon_id, POKEMON_ABILITIES.ability_id, POKEMON.identifier, ABILITIES.identifier FROM POKEMON INNER JOIN ABILITIES ON ABILITIES.id = POKEMON_ABILITIES.ability_id INNER JOIN POKEMON_ABILITIES ON POKEMON_ABILITIES.pokemon_id = POKEMON.id''')

for row in pokecursor:
    print(row[2] + " " + row[3])

pokedex.commit()
pokedex.close()
