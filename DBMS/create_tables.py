import sqlite3

mydb = sqlite3.connect('ipl.db')


c = mydb.cursor()

c.execute('''CREATE TABLE TEAM (
	team_id int,
	team_name text,
	PRIMARY KEY (team_id) 
)''')

c.execute('''CREATE TABLE PLAYER (
	player_id int PRIMARY KEY,
	player_name text,
	dob timestamp,
	batting_hand text,
	bowling_skill text,
	country_name text
 
)''')


c.execute('''CREATE TABLE MATCH (
	match_id int,
	season_year int,
	team1 int,
	team2 int,
	battedfirst int,
	battedsecond int,
	venue_name text,
	city_name text,
	country_name text,
	toss_winner int,
	match_winner int,
	toss_name text,
	win_type text,
	man_of_match int,
	win_margin int,
	PRIMARY KEY(match_id),
	FOREIGN KEY (team1) REFERENCES TEAM(team_id),
	FOREIGN KEY (team2) REFERENCES TEAM(team_id),
	FOREIGN KEY (battedfirst) REFERENCES TEAM(team_id),
	FOREIGN KEY (battedsecond) REFERENCES TEAM(team_id)
)''')

c.execute('''CREATE TABLE PLAYER_MATCH (
	playermatch_key int PRIMARY KEY,
	match_id int,
	player_id int,
	batting_hand text,
	bowling_skill text,
	role_desc text,
	team_id int,
	FOREIGN KEY (match_id) REFERENCES MATCH(match_id),
	FOREIGN KEY (team_id) REFERENCES TEAM(team_id),
	FOREIGN KEY (player_id) REFERENCES PLAYER(player_id)
	
)''')

c.execute('''CREATE TABLE BALL_BY_BALL (
	match_id int NOT NULL,
	innings_no int NOT NULL,
	over_id int NOT NULL,
	ball_id int NOT NULL,
	striker_batting_position int,
	runs_scored int,
	extra_runs int,
	out_type text,
	striker int,
	non_striker int,
	bowler int,
	FOREIGN KEY (match_id) REFERENCES MATCH(match_id),
	FOREIGN KEY (striker) REFERENCES PLAYER(player_id),
	FOREIGN KEY (bowler) REFERENCES PLAYER(player_id),
	FOREIGN KEY (non_striker) REFERENCES PLAYER(player_id)
)''')
mydb.commit()
mydb.close()
