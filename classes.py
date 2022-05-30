import sqlite3

conn = sqlite3.connect('penalty_db.sqlite')
c = conn.cursor()

class Team:
    def __init__(self, name, city, id=None):
        self.name = name
        self.city = city
        self.id = id
        self.partial = 0
        self.final = 0

    def add_keeper(self,team_id):
        #method to add goalkeepers to teams
        query = 'SELECT id FROM players WHERE player_type=0 and team_id=? ORDER BY overall DESC'
        with conn:
            c.execute(query, (team_id,))
            all_gks = c.fetchall()
        self.gk1 = all_gks[0][0]
        self.gk2 = all_gks[1][0]

    def add_shooter(self, team_id, player_id):
        #method to add players to teams
        if player not in shooter:
            self.players.append(player)

    def remove_players(self, player):
        #method to remove players from teams
        if player in players:
            self.players.remove(player)

    def __repr__(self):
        return "('{}', '{}')".format(self.name, self.city)

    def __str__(self):
        return '{}'.format(self.team_name())


class Player:
    #creator for players instances
    def __init__(self, first, last, age, id=None,):
        self.first = first
        self.last = last
        self.age = age
        self.id = id

    def fullname(self):
        print(f'{self.first} {self.last} ({self.team})')

    def __repr__(self):
        return f"{self.first} {self.last}"

    def __str__(self):
        return f"{self.first}, {self.last}"


class Goalkeeper(Player):
        #creator for goalkeepers instances
    def __init__(self, first, last, age, id, player_type, diving, positioning, instinct, concentration, power, precision, coolness, overall, team=None):
        super().__init__(first, last, age, id)
        self.player_type = player_type
        self.diving = diving
        self.positioning = positioning
        self.instinct = instinct
        self.concentration = concentration
        self.power = power
        self.precision = precision
        self.coolness = coolness
        self.overall = overall
        self.team = team

    def state_gk(self):
        print(f'{self.first} {self.last} {self.age} Diving: {self.diving} Positioning: {self.positioning}')


class Shooter(Player):
        #creator for penalty shooters instances
    def __init__(self, first, last, age, id, player_type, diving, positioning, instinct, concentration, power, precision, coolness, overall, team=None):
        super().__init__(first, last, age, id)
        self.player_type = player_type
        self.diving = diving
        self.positioning = positioning
        self.instinct = instinct
        self.concentration = concentration
        self.power = power
        self.precision = precision
        self.coolness = coolness
        self.overall = overall
        self.team = team





# def initiate_gk(player_id):
#     #takes a player id and initializes it
#     query = '''SELECT first, last, age, id, player_type, diving, positioning,
#         instinct, concentration, power, precision, coolness, overall, teams.name FROM players INNER JOIN teams ON players.team_id = teams.id WHERE id=?'''
#     with conn:
#         c.execute(query, (player_id,))
#         gk = c.fetchone()
#         return Goalkeeper(gk[0], gk[1], gk[2], gk[3], gk[4], gk[5], gk[6], gk[7], gk[8], gk[9], gk[10], gk[11], gk[12], gk[13])


select_all_gks = 'SELECT first, last, age, id, player_type, diving, positioning, instinct, concentration, power, precision, coolness, overall FROM players WHERE player_type = 0'

def initiate_gk_index(query, index):
    #takes a query and index number and initiates the player
    with conn:
        c.execute(query)
        gk = c.fetchall()[index]
        return Goalkeeper(gk[0], gk[1], gk[2], gk[3], gk[4], gk[5], gk[6], gk[7], gk[8], gk[9], gk[10], gk[11], gk[12])

def get_gk_by_id(id):
    #takes the ID of a players and returns the player
    c.execute("SELECT * FROM players WHERE player_type = 0 AND id=:id", {'id':id})
    return c.fetchall()

def initiate_teams(team_id):
    with conn:
        c.execute('SELECT id,name,city FROM teams WHERE id=:id', {'id': team_id})
        team = c.fetchall()[0]
        return Team({team[1]},{team[2]},{team[0]})
