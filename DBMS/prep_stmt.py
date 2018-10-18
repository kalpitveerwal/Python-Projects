import sqlite3
import sys

mydb = sqlite3.connect('ipl.db')

x = input()
if(x== '1'):
	l = []
	a= input()
	b = input()
	l.append(tuple([a,b])) 
	mydb.executemany("INSERT INTO TEAM (team_id, team_name) VALUES (?, ?);", l)
	mydb.commit()


elif(x=='2'):	
	l = []
	a = input()
	b = input()
	c = input()
	d = input()
	e = input()
	f = input()
	l.append(tuple([a,b,c,d,e,f]))
	mydb.executemany("INSERT INTO PLAYER (player_id, player_name, dob, batting_hand, bowling_skill, country_name) VALUES (?, ?, ?, ?, ?, ?);", l)
	mydb.commit()


elif(x=='3'):
	l = []
	a = input()
	b = input()
	c = input()
	d = input()
	e = input()
	f = input()
	g = input()
	h = input()
	i = input()
	j = input()
	k = input()
	l1 = input()
	m = input()
	n = input()
	o = input()
	l.append(tuple([a,b,c,d,e,f,g,h,i,j,k,l1,m,n,o]))
	mydb.executemany("INSERT INTO MATCH (match_id, season_year, team1, team2, battedfirst, battedsecond, venue_name, city_name, country_name, toss_winner, match_winner, toss_name, win_type, man_of_match, win_margin) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", l)
	mydb.commit()

elif(x=='4'):	
	l = []
	a = input()
	b = input()
	c = input()
	d = input()
	e = input()
	f = input()
	g = input()

	l.append(tuple([a,b,c,d,e,f,g]))
	mydb.executemany("INSERT INTO PLAYER_MATCH (playermatch_key, match_id, player_id, batting_hand, bowling_skill, role_desc, team_id) VALUES (?, ?, ?, ?, ?, ?, ?);", l)
	mydb.commit()

elif(x=='5'):	
	l = []
	a = input()
	b = input()
	c = input()
	d = input()
	e = input()
	f = input()
	g = input()
	h = input()
	i = input()
	j = input()
	k = input()
	l.append(tuple([a,b,c,d,e,f,g,h,i,j,k]))
	mydb.executemany("INSERT INTO BALL_BY_BALL (match_id, innings_no, over_id, ball_id, striker_batting_position, runs_scored, extra_runs, out_type, striker, non_striker, bowler) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", l)
	mydb.commit()
