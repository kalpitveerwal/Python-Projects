import sqlite3

mydb = sqlite3.connect('ipl.db')

c = mydb.cursor()
 
c.execute('''	SELECT
				CAST(SUM(RUNS) AS float) /CAST(COUNT(DISTINCT ID) AS float) AS abd,
				
				VENUE

				FROM
				(SELECT MATCH.match_id as ID, MATCH.venue_name as VENUE, BALL_BY_BALL.runs_scored as RUNS
				FROM MATCH
				INNER JOIN BALL_BY_BALL ON MATCH.match_id = BALL_BY_BALL.match_id)
				GROUP BY
					VENUE
				ORDER BY
						abd DESC
				


				''')

for row in c:
	print(row[1]+','+str(row[0]))

mydb.commit()	

				