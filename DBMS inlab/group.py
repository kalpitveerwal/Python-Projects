import sqlite3

pokedex = sqlite3.connect('pokedex.db')
pokecursor = pokedex.cursor()

pokecursor.execute('''select species_id, base_experience from POKEMON GROUP BY species_id ORDER BY base_experience DESC limit 3''')

for row in pokecursor:
    print(row[1])

pokedex.commit()
pokedex.close()
