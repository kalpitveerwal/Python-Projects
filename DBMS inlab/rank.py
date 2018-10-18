import sqlite3

pokedex = sqlite3.connect('pokedex.db')
pokecursor = pokedex.cursor()

pokecursor.execute('''select identifier from POKEMON ORDER BY base_experience DESC limit 3''')

for row in pokecursor:
    print(row[0])

pokedex.commit()
pokedex.close()
