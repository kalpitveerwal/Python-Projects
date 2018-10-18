import csv, sqlite3

pokedex = sqlite3.connect('pokedex.db')
pokecursor = pokedex.cursor()

with open('pokemon.csv') as file1:
    dr1 = csv.DictReader(file1)
    poke_table = [(i['id'],i['identifier'],i['species_id'],i['height'],i['weight'],i['base_experience'],i['order'],i['is_default']) for i in dr1]

pokecursor.executemany('''INSERT INTO POKEMON VALUES(?,?,?,?,?,?,?,?)''',poke_table)

with open('abilities.csv') as file2:
    dr2 = csv.DictReader(file2)
    abilities_table = [(i['id'],i['identifier'],i['generation_id'],i['is_main_series']) for i in dr2]

pokecursor.executemany('''INSERT INTO ABILITIES VALUES(?,?,?,?)''',abilities_table)

with open('pokemon_abilities.csv') as file3:
    dr3 = csv.DictReader(file3)
    poke_abilities = [(i['pokemon_id'],i['ability_id'],i['is_hidden'],i['slot']) for i in dr3]

pokecursor.executemany('''INSERT INTO POKEMON_ABILITIES VALUES(?,?,?,?)''',poke_abilities)

pokedex.commit()
pokedex.close()
