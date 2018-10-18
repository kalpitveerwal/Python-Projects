import sqlite3
import sys

mydb = sqlite3.connect('ipl.db')
cur = mydb.cursor();
x = input()
y = input()
if(y=='1'):
	if(x== '1'):
		a= input()
	
		cur.execute("DELETE FROM TEAM WHERE team_name = (?);", [a])
		mydb.commit()
  

	elif(x== '2'):
		a= input()
	
		cur.execute("DELETE FROM PLAYER WHERE player_name = (?);", [a])
		mydb.commit()


	elif(x== '3'):
		a= input()
	
		cur.execute("DELETE FROM MATCH WHERE match_id = (?);", [a])
		mydb.commit()

else:
	if(x== '1'):
		a= input()

		
		cur.execute("DELETE FROM TEAM WHERE team_name ="+"'"+a+"'"+";")
		mydb.commit()
  

	elif(x== '2'):
		a= input()
	
		cur.execute("DELETE FROM PLAYER WHERE player_name = " +"'"+a+"'"+";")
		mydb.commit()


	elif(x== '3'):
		a= input()
	
		cur.execute("DELETE FROM MATCH WHERE match_id = "+"'"+a+"'"+";")
		mydb.commit()		