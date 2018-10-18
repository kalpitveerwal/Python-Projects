import sqlite3

pokedex = sqlite3.connect('pokedex.db')
pokecursor = pokedex.cursor()

pokecursor.execute('''UPDATE ABILITIES set generation_id=8 WHERE is_main_series=0''')

pokedex.commit()
pokedex.close()
