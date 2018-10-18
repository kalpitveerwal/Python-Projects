import sqlite3

pokedex = sqlite3.connect('pokedex.db')
pokecursor = pokedex.cursor()

pokecursor.execute('''CREATE TABLE POKEMON(id int, identifier text, species_id int, height int, weight int, base_experience int, order1 int, is_default int)''')

pokecursor.execute('''CREATE TABLE ABILITIES(id int, identifier text, generation_id int, is_main_series int)''')

pokecursor.execute('''CREATE TABLE POKEMON_ABILITIES(pokemon_id int, ability_id int, is_hidden int, slot int)''')

pokedex.commit()

pokedex.close()
