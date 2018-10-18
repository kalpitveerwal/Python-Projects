import sqlite3

mydb = sqlite3.connect('ipl.db')

c = mydb.cursor()
 
c.execute('''	SELECT
				ID,
				NAME,
				COUNT(BALLS)/COUNT(DISTINCT MATCHES) AS abd

				

				FROM
				(SELECT PLAYER.player_id as ID, PLAYER.player_name as NAME, 
				BALL_BY_BALL.striker as BALLS, BALL_BY_BALL.match_id as MATCHES

				FROM PLAYER
				INNER JOIN BALL_BY_BALL ON PLAYER.player_id = BALL_BY_BALL.striker)
				GROUP BY 
				name
				ORDER BY 
				abd DESC
				


				''')

for row in c:
	print(str(row[0])+','+row[1]+','+str(row[2]))

mydb.commit()	