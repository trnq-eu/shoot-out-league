import sqlite3
import csv
import random
import pandas as pd
import sqlalchemy

conn = sqlite3.connect('penalty_db.sqlite')
c = conn.cursor()

engine = sqlalchemy.create_engine('sqlite:///penalty_db.sqlite')

def insert_team(name, city):
    #takes name, city and insert a new team on db
    name = name
    city = city
    with conn:
        c.execute(
        "INSERT INTO teams (name, city) VALUES (?, ?)", (name, city)
        )


def list_teams():
    with conn:
        c.execute("SELECT name, city FROM teams")
        return c.fetchall()

#Converting csv rows to lists
first_names_list = []
family_names_list = []

file = open('db/italian_names.csv', encoding="utf8")
file_reader_it = csv.reader(file, delimiter=';')
file_list_it = list(file_reader_it)

for row in file_list_it:
    if not row[0]:
        continue
    else:
         first_names_list.append(row[0])

for row in file_list_it:
    if not row[1]:
        continue
    else:
         family_names_list.append(row[1])

file = open('db/american_names.csv', encoding="utf8")
file_reader_am = csv.reader(file, delimiter=';')
file_list_am = list(file_reader_am)

for row in file_list_am:
    if not row[0]:
        continue
    else:
         first_names_list.append(row[0])

for row in file_list_it:
    if not row[1]:
        continue
    else:
         family_names_list.append(row[1])

file = open('db/spanish_names.csv')
file_reader_sp = csv.reader(file, delimiter=';')
file_list_sp = list(file_reader_sp)

for row in file_list_sp:
    if not row[0]:
        continue
    else:
         first_names_list.append(row[0])

for row in file_list_it:
    if not row[1]:
        continue
    else:
         family_names_list.append(row[1])


file = open('db/swedish_names.csv', encoding="utf8")
file_reader_sw = csv.reader(file, delimiter=';')
file_list_sw = list(file_reader_sw)

for row in file_list_sw:
    if not row[0]:
        continue
    else:
         first_names_list.append(row[0])

for row in file_list_it:
    if not row[1]:
        continue
    else:
         family_names_list.append(row[1])


###

def insert_gk():
    first = str(random.choice(first_names_list).title())
    last = str(random.choice(family_names_list).title())
    age = str(random.randint(18, 34))
    diving = random.randint(70, 99)
    positioning = random.randint(70, 99)
    instinct = random.randint(70, 99)
    concentration = random.randint(70, 99)
    power = random.randint(10, 99)
    precision = random.randint(10, 99)
    coolness = random.randint(10, 99)
    improvement = random.randint(5, 30)
    improvement_pace = random.randint(1, 5)

    with conn:
        c.execute("""
        INSERT INTO players (first, last, age, player_type, diving, positioning, instinct, concentration, power, precision, coolness, improvement, improvement_pace)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (first, last, age, 0, diving, positioning, instinct, concentration, power, precision, coolness, improvement, improvement_pace))

def insert_shooter():
    first = str(random.choice(first_names_list).title())
    last = str(random.choice(family_names_list).title())
    age = str(random.randint(18, 34))
    diving = random.randint(1, 60)
    positioning = random.randint(1, 99)
    instinct = random.randint(1, 99)
    concentration = random.randint(60, 99)
    power = random.randint(70, 99)
    precision = random.randint(70, 99)
    coolness = random.randint(70, 99)
    improvement = random.randint(5, 30)
    improvement_pace = random.randint(1, 5)

    with conn:
        c.execute("""
        INSERT INTO players (first, last, age, player_type, diving, positioning, instinct, concentration, power, precision, coolness, improvement, improvement_pace)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (first, last, age, 1, diving, positioning, instinct, concentration, power, precision, coolness, improvement, improvement_pace))

def select_gk():
    with conn:
        c.execute('SELECT first, last, age, id, player_type, diving, positioning, instinct, concentration, power, precision, coolness FROM players WHERE player_type = 0')
        return c.fetchone()

def list_gk():
    with conn:
        c.execute('SELECT id, first, last, age, player_type, diving, positioning, instinct, concentration, power, precision, coolness FROM players WHERE player_type = 0')
        goalkeepers = c.fetchall()
        for gk in goalkeepers:
            print('ID: ' + str(gk[0]) + " Name: " + str(gk[1]) + ' ' + str(gk[2]) + '\tAge: ' + str(gk[3]) + "\tDVNG: " + str(gk[5]) + "\tPOS: " + str(gk[6]) + "\tINST: " + str(gk[7]) + "\tCONC: " + str(gk[8]))


def update_gks():
    #updates goalkeepers overall value
    with conn:
        c.execute('SELECT id, diving, positioning, instinct, overall FROM players WHERE player_type=0')
        records = c.fetchall()
        for record in records:
            player_id = record[0]
            new_overall = record[1] + record[2] + record[3]
            c.execute('UPDATE players SET overall=? WHERE id=?', (new_overall, player_id,))

def update_shooter():
    #updates shooters overall value
    with conn:
        c.execute('SELECT id, power, precision, coolness, overall FROM players WHERE player_type=1')
        records = c.fetchall()
        for record in records:
            player_id = record[0]
            new_overall = record[1] + record[2] + record[3]
            c.execute('UPDATE players SET overall=? WHERE id=?', (new_overall, player_id,))

def get_team_name(team_id):
    with conn:
        c.execute('SELECT name FROM teams WHERE id=?',(team_id,))
        return c.fetchone()

def get_player_name(player_id):
    with conn:
        c.execute('SELECT first, last FROM players WHERE id=?',(player_id,))
        return c.fetchone()

def assign_player(team_id, player_id):
    with conn:
        c.execute('UPDATE players SET team_id=? WHERE id=?',(team_id, player_id,))
        team_name = get_team_name(team_id)
        player_name = get_player_name(player_id)
        print(f'{team_name} selects {player_name}')


def list_roster(team_id):
    team_roster = '''SELECT players.id, first, last, age, power, precision, coolness, concentration, diving, instinct, positioning, overall, teams.name
        FROM players INNER JOIN teams ON players.team_id = teams.id WHERE team_id='%s' ORDER BY overall DESC''' % team_id
    df = pd.read_sql(team_roster, engine)
    with conn:
        c.execute(team_roster)
        return df

def draft_players():
    #makes one draft round
    pick_order = [2, 8, 4, 5, 3, 7, 1, 6, 6, 1, 7, 3, 5, 4, 8, 2, 2, 8, 4, 5, 3, 7, 1, 6, 6, 1, 7, 3, 5, 4, 8, 2, 2, 8, 4, 5, 3, 7, 1, 6, 6, 1, 7, 3, 5, 4, 8, 2,]
    with conn:
        for pick in pick_order:
            c.execute('SELECT id FROM players WHERE team_id IS NULL ORDER BY overall DESC')
            selected_player = c.fetchone()[0]
            c.execute('UPDATE players SET team_id=? WHERE id=?', (pick,selected_player,))
            team_name = get_team_name(pick)
            player_name = get_player_name(selected_player)
            print(f'{team_name} selects {player_name}')

    #select all player in overall desc order, fetch the first one and assign team id





#QUERIES
# select_teams = pd.read_sql('SELECT * FROM teams', engine)
# select_goalkeepers = pd.read_sql('SELECT * FROM players WHERE player_type=0', engine)
# select_shooters = pd.read_sql('SELECT id, first, last, age, power, precision, concentration, coolness FROM players WHERE player_type=1', engine)
# select_players = pd.read_sql('SELECT * FROM players', engine)
list_gk_overall = pd.read_sql('SELECT id, first, last, age, diving, positioning, instinct, overall, team_id FROM players WHERE player_type=0 ORDER BY overall DESC', engine)
# list_shooters_overall = pd.read_sql('SELECT first, last, age, power, precision, coolness, overall, team_id FROM players WHERE player_type=1 ORDER BY overall DESC', engine)
list_shooters_FAs = pd.read_sql('''SELECT id, first, last, age, power, precision, coolness, overall, team_id
    FROM players WHERE player_type=1 AND team_id IS NULL ORDER BY overall DESC''', engine)
list_gk_FAs = pd.read_sql('''SELECT id, first, last, age, diving, instinct, positioning, overall, team_id
    FROM players WHERE player_type=0 AND team_id IS NULL ORDER BY overall DESC''', engine)
list_players_team = pd.read_sql('''SELECT players.id, first, last, age, power, precision, coolness, concentration, diving, instinct, positioning, overall, teams.name
    FROM players INNER JOIN teams ON players.team_id = teams.id ORDER BY overall DESC''', engine)
list_players_overall = pd.read_sql('''SELECT id, first, last, age, player_type, overall, team_id, power, precision, coolness, concentration, diving, instinct, positioning
    FROM players WHERE team_id IS NULL ORDER BY overall DESC LIMIT 20''', engine)



#DB COMMAND



# draft_players()
# print(list_players_overall)

# with conn:
#     c.execute('ALTER TABLE teams ADD COLUMN short TEXT')


c.close()





# for i in range(50):
#     insert_shooter()
# # with conn:
#     c.execute('DELETE FROM players WHERE id > 50;')


# c.execute("""CREATE TABLE player_stats(
#     player_id INTEGER NOT NULL,
#     total_shots INTEGER,
#     scored INTEGER,
#     missed INTEGER,
#     saved INTEGER,
#     FOREIGN KEY (player_id)
#         REFERENCES players (id)
# )""")




# c.executescript('''
# DROP TABLE IF EXISTS teams;
#
# CREATE TABLE teams (
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name TEXT UNIQUE,
#     city TEXT
# );
# ''')
