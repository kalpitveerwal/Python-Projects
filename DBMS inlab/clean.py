import sqlite3

pokedex = sqlite3.connect('pokedex.db')
pokecursor = pokedex.cursor()

pokecursor.execute('''DELETE FROM POKEMON WHERE identifier = "roguebeautifly"''')
pokecursor.execute('''DELETE FROM POKEMON WHERE identifier = "rogueraticate"''')
pokecursor.execute('''DELETE FROM POKEMON WHERE identifier = "roguespearow"''')
pokecursor.execute('''DELETE FROM POKEMON WHERE identifier = "roguedragalge"''')
pokecursor.execute('''DELETE FROM POKEMON WHERE identifier = "rogueclauncher"''')
pokecursor.execute('''DELETE FROM POKEMON WHERE identifier = "rogueclawitzer"''')
pokecursor.execute('''DELETE FROM POKEMON WHERE identifier = "roguemiltank"''')
pokecursor.execute('''DELETE FROM POKEMON WHERE identifier = "rogueblissey"''')
pokecursor.execute('''DELETE FROM POKEMON WHERE identifier = "roguefearow"''')
pokecursor.execute('''DELETE FROM POKEMON WHERE identifier = "roguerattata"''')
pokecursor.execute('''DELETE FROM POKEMON WHERE identifier = "roguebulbasaur"''')
pokecursor.execute('''DELETE FROM POKEMON WHERE identifier = "rogueraikou"''')

pokedex.commit()
pokedex.close()
