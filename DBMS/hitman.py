import sqlite3

mydb = sqlite3.connect('ipl.db')

c = mydb.cursor()
 
c.execute('''	SELECT
				ID,
				NAME,
				COUNT(case RUNS WHEN '6' then 1 else null end),
				COUNT(BALLS),
				CAST(COUNT(case RUNS WHEN '6' then 1 else null end) AS float)/CAST(COUNT(BALLS) AS float) as rg

				FROM
				(SELECT PLAYER.player_id as ID, PLAYER.player_name as NAME, 
				BALL_BY_BALL.runs_scored as RUNS, BALL_BY_BALL.striker as BALLS

				FROM PLAYER
				INNER JOIN BALL_BY_BALL ON PLAYER.player_id = BALL_BY_BALL.striker)
				GROUP BY 
				name
				ORDER BY
				rg DESC
				''')

for row in c:
	print(str(row[0])+','+row[1]+','+str(row[2])+','+str(row[3])+','+str(row[4]))

mydb.commit()	