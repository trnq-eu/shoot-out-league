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
    #generates new goalkeepers
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
    training_days = 0


    with conn:
        c.execute("""
        INSERT INTO players (first, last, age, player_type, diving, positioning, instinct, concentration, power, precision, coolness, improvement, improvement_pace, training_days)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (first, last, age, 0, diving, positioning, instinct, concentration, power, precision, coolness, improvement, improvement_pace, training_days))

def insert_shooter():
    #generates new shooters
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
    training_days = 0

    with conn:
        c.execute("""
        INSERT INTO players (first, last, age, player_type, diving, positioning, instinct, concentration, power, precision, coolness, improvement, improvement_pace, training_days)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (first, last, age, 1, diving, positioning, instinct, concentration, power, precision, coolness, improvement, improvement_pace, training_days))

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

def print_week_results(season_id, week_id):
    print('\nWeek ' + str(week_id) + ' results:\n')
    c.execute('''SELECT home_team_id, away_team_id, home_team_result, away_team_result FROM matches WHERE season_id = ? and week = ?''', (season_id, week_id))
    results = c.fetchall()
    for result in results:
        t1_id = result[0]
        t2_id = result[1]
        t1_result = result[2]
        t2_result = result[3]
        c.execute('''SELECT name FROM teams WHERE id = ? ''', (t1_id,))
        t1_name = c.fetchone()[0]
        c.execute('''SELECT name FROM teams WHERE id = ? ''', (t2_id,))
        t2_name = c.fetchone()[0]
        print(str(t1_name) + ' - ' + str(t2_name) + ' : ' + str(t1_result) + ' -  ' + str(t2_result))
    
def list_table(season_id):
    select_table = '''SELECT teams.name, teams.division_id AS division, league_tables.points AS points, league_tables.wins AS wins, league_tables.draws AS draws, league_tables.losses AS losses, league_tables.PPG
    FROM teams INNER JOIN league_tables ON teams.id = league_tables.team_id WHERE season_id = '%s' ORDER BY league_tables.PPG DESC''' % season_id
    df = pd.read_sql(select_table, engine)
    with conn:
        c.execute(select_table)
        print(df)

def list_table_div(season, division):
    c.execute('''SELECT teams.name, league_tables.points AS points, league_tables.wins AS wins, league_tables.draws AS draws, league_tables.losses AS losses, league_tables.PPG
    FROM teams INNER JOIN league_tables ON teams.id = league_tables.team_id WHERE league_tables.season_id = ? and league_tables.division_id = ? ORDER BY league_tables.PPG DESC''', (season, division))
    table = c.fetchall()
    print('DIVISION ' + str(division) + ":")
    for team in table:
        print('{0} {1:.3f}'.format(team[0], team[5]))
    

def list_scorers():
    select_table = '''SELECT players.first, players.last, player_stats.scored
    FROM players INNER JOIN player_stats ON players.id = player_stats.player_id ORDER BY player_stats.scored DESC LIMIT 10'''
    df = pd.read_sql(select_table, engine)
    with conn:
        c.execute(select_table)
        print(df)

def draft_players(pick_order):
    #makes one draft round
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
# list_gk_overall = pd.read_sql('SELECT id, first, last, age, diving, positioning, instinct, overall, team_id FROM players WHERE player_type=0 ORDER BY overall DESC', engine)
# # list_shooters_overall = pd.read_sql('SELECT first, last, age, power, precision, coolness, overall, team_id FROM players WHERE player_type=1 ORDER BY overall DESC', engine)
# list_shooters_FAs = pd.read_sql('''SELECT id, first, last, age, power, precision, coolness, overall, team_id
#     FROM players WHERE player_type=1 AND team_id IS NULL ORDER BY overall DESC''', engine)
# list_gk_FAs = pd.read_sql('''SELECT id, first, last, age, diving, instinct, positioning, overall, team_id
#     FROM players WHERE player_type=0 AND team_id IS NULL ORDER BY overall DESC''', engine)
# list_players_team = pd.read_sql('''SELECT players.id, first, last, age, power, precision, coolness, concentration, diving, instinct, positioning, overall, teams.name
#     FROM players INNER JOIN teams ON players.team_id = teams.id ORDER BY overall DESC''', engine)
# list_players_overall = pd.read_sql('''SELECT id, first, last, age, player_type, overall, team_id, power, precision, coolness, concentration, diving, instinct, positioning
#     FROM players WHERE team_id IS NULL ORDER BY overall DESC LIMIT 20''', engine)

table_lines = [(1, 1, 0, 0, 0, 0, 0),
            (1, 2, 0, 0, 0, 0, 0),
            (1, 3, 0, 0, 0, 0, 0),
            (1, 4, 0, 0, 0, 0, 0),
            (1, 5, 0, 0, 0, 0, 0),
            (1, 6, 0, 0, 0, 0, 0),
            (1, 7, 0, 0, 0, 0, 0),
            (1, 8, 0, 0, 0, 0, 0),]

africana = [(2, 'Nihils of the Nile', 'Alexandria', 'Egypt'), 
    (2, 'Rocambolesca Mozambique', 'Maputo', 'Mozambique'),
    (2, 'Equatoreana Penalties Libreville', 'Libreville', 'Gabon'),
    (2, 'Pirates of the Namibian Sea', 'Mariental', 'Namibia'),
    (2, 'Precisos de Lagos', 'Lagos', 'Angola'),
    (2, 'Metropol Carthago', 'Carthage', 'Tunisia'),
    (2, 'Botswana Bots Powershooters', 'Ghanzi', 'Botswana'),
    (2, 'Equatoriana Penalties Libreville', 'Libreville', 'Gabon')]

americana = [(3, 'Academia Brasileira Batidores', 'Salvador de Bahia', 'Brazil'), 
    (3, 'Tulsa Checklisters', 'Tulsa', 'USA'),
    (3, 'Canadian Fahrenheits', 'Montreal', 'Canada'),
    (3, 'Uruguagia Kickers', 'Montevideo', 'Uruguay'),
    (3, 'Mexicana Deep Shots', 'Tijuana', 'Mexico'),
    (3, 'Smooth Bolivians', 'Carthage', 'La Paz'),
    (3, 'Alaskickers', 'Anchorage', 'USA'),
    (3, 'Universidad Chilena de Panenka', 'Santiago', 'Chile')]


asiatica = [(4, 'Kyoto Blossom Penalties', 'Kyoto', 'Japan'), 
    (4, 'Varanasi Dukkhas', 'Varanasi', 'India'),
    (4, 'Shooters of the Gange', 'Kanpur', 'India'),
    (4, 'Thai Thai Goalies', 'Phuket', 'Thailand'),
    (4, 'Sichuan No-Nos', 'Chengduh', 'China'),
    (4, 'TWN', 'Taiwan', 'Taiwan'),
    (4, 'Puruogangri Cool Kicks', 'Nagqu', 'Tibet'),
    (4, 'Ulan Batteurs', 'Ulan Bator', 'Mongolia')]

league_tables_teams = [(1, 1, 1, 0, 0, 0, 0, 0),
                    (1, 2, 1, 0, 0, 0, 0, 0),
                    (1, 3, 1, 0, 0, 0, 0, 0),
                    (1, 4, 1, 0, 0, 0, 0, 0),
                    (1, 5, 1, 0, 0, 0, 0, 0),
                    (1, 6, 1, 0, 0, 0, 0, 0),
                    (1, 7, 1, 0, 0, 0, 0, 0),
                    (1, 8, 1, 0, 0, 0, 0, 0),
                    (1, 9, 2, 0, 0, 0, 0, 0),
                    (1, 10, 2, 0, 0, 0, 0, 0),
                    (1, 11, 2, 0, 0, 0, 0, 0),
                    (1, 12, 2, 0, 0, 0, 0, 0),
                    (1, 13, 2, 0, 0, 0, 0, 0),
                    (1, 14, 2, 0, 0, 0, 0, 0),
                    (1, 15, 2, 0, 0, 0, 0, 0),
                    (1, 16, 2, 0, 0, 0, 0, 0),
                    (1, 17, 3, 0, 0, 0, 0, 0),
                    (1, 18, 3, 0, 0, 0, 0, 0),
                    (1, 19, 3, 0, 0, 0, 0, 0),
                    (1, 20, 3, 0, 0, 0, 0, 0),
                    (1, 21, 3, 0, 0, 0, 0, 0),
                    (1, 22, 3, 0, 0, 0, 0, 0),
                    (1, 23, 3, 0, 0, 0, 0, 0),
                    (1, 24, 3, 0, 0, 0, 0, 0),
                    (1, 25, 4, 0, 0, 0, 0, 0),
                    (1, 26, 4, 0, 0, 0, 0, 0),
                    (1, 27, 4, 0, 0, 0, 0, 0),
                    (1, 28, 4, 0, 0, 0, 0, 0),
                    (1, 29, 4, 0, 0, 0, 0, 0),
                    (1, 30, 4, 0, 0, 0, 0, 0),
                    (1, 31, 4, 0, 0, 0, 0, 0),
                    (1, 32, 4, 0, 0, 0, 0, 0)]



#DB COMMAND
# print_week_results(1,13)
# list_table(1)

list_table_div(1, 1)
list_table_div(1, 2)
list_table_div(1, 3)
list_table_div(1, 4)



# with conn:
#     c.executemany('INSERT INTO league_tables (season_id, team_id, division_id, points, goal_diff, wins, draws, losses) VALUES (?,?,?,?,?,?,?,?);', league_tables_teams)


# team_ids = list(range(1,33))
# draft_order = random.sample(team_ids, len(team_ids))
# draft_order_copy = draft_order[:]
# snake_round = draft_order_copy.reverse()

# print(draft_order)
# print(draft_order_copy)


# for i in range(100):
#     insert_shooter()

# for i in range(20):
#     insert_gk()

# update_shooter()
# update_gks()

# draft_players(draft_order)
# draft_players(draft_order_copy)

# for i in range(50):
#     insert_gk()

# with conn:
#     c.execute('DELETE FROM players WHERE id > 50;')
# list_table(1)




# with conn:
#     c.executemany('INSERT INTO teams (division_id, name, city, country) VALUES (?,?,?,?);', africana)
#     c.executemany('INSERT INTO teams (division_id, name, city, country) VALUES (?,?,?,?);', americana)
#     c.executemany('INSERT INTO teams (division_id, name, city, country) VALUES (?,?,?,?);', asiatica)


  

#     c.executemany('''INSERT INTO league_tables (season_id, team_id, points, goal_diff, wins, draws, losses) 
#       VALUES (?,?,?,?,?,?,?);''', table_lines)

#     c.executemany('INSERT INTO matches (season_id, home_team_id, away_team_id) VALUES (1,?,?);', game1)
    # c.executemany('INSERT INTO matches (season_id, home_team_id, away_team_id) VALUES (1,?,?);', game2)
#     c.executemany('INSERT INTO matches (season_id, home_team_id, away_team_id) VALUES (1,?,?);', game3)
#     c.executemany('INSERT INTO matches (season_id, home_team_id, away_team_id) VALUES (1,?,?);', game4)
#     c.executemany('INSERT INTO matches (season_id, home_team_id, away_team_id) VALUES (1,?,?);', game5)
#     c.executemany('INSERT INTO matches (season_id, home_team_id, away_team_id) VALUES (1,?,?);', game6)
#     c.executemany('INSERT INTO matches (season_id, home_team_id, away_team_id) VALUES (1,?,?);', game7)
#     c.executemany('INSERT INTO matches (season_id, home_team_id, away_team_id) VALUES (1,?,?);', game8)




    # c.execute('INSERT INTO matches (id, season_id, home_team_id, away_team_id) VALUES ( ?, ?, ?, ?)', (1, 1, 2, 6,))
    # c.execute('INSERT INTO seasons (name) VALUES (?)', ('Test season',))


# c.executescript('''
#     DROP TABLE IF EXISTS matches;

#     CREATE TABLE matches(
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#         season_id INTEGER,
#         home_team_id INTEGER,
#         away_team_id INTEGER,
#         FOREIGN KEY (season_id)
#             REFERENCES seasons (id),
#         FOREIGN KEY (home_team_id)
#             REFERENCES teams (id),
#         FOREIGN KEY (away_team_id)
#             REFERENCES teams (id)
#     );
#     ''')


# c.executescript("""
#     DROP TABLE IF EXISTS league_tables;
#     CREATE TABLE league_tables(
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     season_id INTEGER,
#     team_id INTEGER,
#     division_id INTEGER,
#     points INTEGER,
#     goal_diff INTEGER,
#     wins INTEGER,
#     draws INTEGER,
#     losses INTEGER,
#     FOREIGN KEY (season_id)
#          REFERENCES seasons (id),
#     FOREIGN KEY (team_id)
#          REFERENCES teams (id)
#     FOREIGN KEY (division_id)
#          REFERENCES divisions (id)
#     )
# """)

c.close()

# c.executescript("""
#     DROP TABLE IF EXISTS team_stats;

#     CREATE TABLE team_stats(
#     team_id INTEGER NOT NULL UNIQUE,
#     total_wins INTEGER,
#     total_losses INTEGER,
#     total_draws INTEGER,
#     FOREIGN KEY (team_id)
#         REFERENCES teams (id)
# )""")

# c.executescript("""
#     DROP TABLE IF EXISTS player_stats;

#     CREATE TABLE player_stats(
#     player_id INTEGER NOT NULL UNIQUE,
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
