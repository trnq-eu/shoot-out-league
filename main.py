import sqlite3
import random
from classes import *
import time

conn = sqlite3.connect('penalty_db.sqlite')
c = conn.cursor()

def initiate_gk(player_id):
    #takes a player id and initializes it
    query = '''SELECT first, last, age, players.id, player_type, diving, positioning,
        instinct, concentration, power, precision, coolness, overall, teams.name FROM players INNER JOIN teams ON players.team_id = teams.id WHERE players.id=?'''
    with conn:
        c.execute(query, (player_id,))
        gk = c.fetchone()
        return Goalkeeper(gk[0], gk[1], gk[2], gk[3], gk[4], gk[5], gk[6], gk[7], gk[8], gk[9], gk[10], gk[11], gk[12], gk[13])

def initiate_shooter(player_id):
    #takes a player id and initializes it
    query = '''SELECT first, last, age, players.id, player_type, diving, positioning,
        instinct, concentration, power, precision, coolness, overall, teams.name FROM players INNER JOIN teams ON players.team_id = teams.id WHERE players.id=?'''
    with conn:
        c.execute(query, (player_id,))
        gk = c.fetchone()
        return Shooter(gk[0], gk[1], gk[2], gk[3], gk[4], gk[5], gk[6], gk[7], gk[8], gk[9], gk[10], gk[11], gk[12], gk[13])

def initiate_team(team_id):
    #takes a team id and initializes the object
    query = 'SELECT name, city, id FROM teams WHERE teams.id=?'
    with conn:
        c.execute(query, (team_id,))
        team = c.fetchone()
        return Team(team[0], team[1], team[2])

def match(team1_id,team2_id):
    team1 = initiate_team(team1_id)
    team2 = initiate_team(team2_id)
    team1.partial = 0
    team2.partial = 0
    team1.final = 0
    team2.final = 0
    c.execute('SELECT id FROM players WHERE player_type = 0 AND team_id=? ORDER BY overall DESC',(team1_id,))
    team1_gks = c.fetchall()
    tm1_gk = initiate_gk(team1_gks[0][0])
    c.execute('SELECT id FROM players WHERE player_type = 0 AND team_id=? ORDER BY overall DESC',(team2_id,))
    team2_gks = c.fetchall()
    tm2_gk = initiate_gk(team2_gks[0][0])
    c.execute('SELECT id FROM players WHERE player_type = 1 AND team_id=? ORDER BY overall DESC',(team1_id,))
    team1_shooters = c.fetchall() #return a tuple made of id, first, last
    c.execute('SELECT id FROM players WHERE player_type = 1 AND team_id=? ORDER BY overall DESC',(team2_id,))
    team2_shooters = c.fetchall()
    conn.commit()
    tm2_sht1 = initiate_shooter(team2_shooters[0][0])
    tm2_sht2 = initiate_shooter(team2_shooters[1][0])
    tm2_sht3 = initiate_shooter(team2_shooters[2][0])
    tm2_sht4 = initiate_shooter(team2_shooters[3][0])
    tm2_sht5 = initiate_shooter(team2_shooters[4][0])
    tm1_sht1 = initiate_shooter(team1_shooters[0][0])
    tm1_sht2 = initiate_shooter(team1_shooters[1][0])
    tm1_sht3 = initiate_shooter(team1_shooters[2][0])
    tm1_sht4 = initiate_shooter(team1_shooters[3][0])
    tm1_sht5 = initiate_shooter(team1_shooters[4][0])
    time.sleep(1)
    print('Formations:\n')
    time.sleep(1)
    print(f'{team1.name}:\n')
    time.sleep(1)
    print(f'Goalkeeper: {tm1_gk.first} {tm1_gk.last} {tm1_gk.overall}')
    time.sleep(1)
    print(f'First shooter: {tm1_sht1.first} {tm1_sht1.last} {tm1_sht1.overall}')
    time.sleep(1)
    print(f'Second shooter: {tm1_sht2.first} {tm1_sht2.last} {tm1_sht2.overall}')
    time.sleep(1)
    print(f'Third shooter: {tm1_sht3.first} {tm1_sht3.last} {tm1_sht3.overall}')
    time.sleep(1)
    print(f'Fourth shooter: {tm1_sht4.first} {tm1_sht4.last} {tm1_sht4.overall}')
    time.sleep(1)
    print(f'Fifth shooter: {tm1_sht5.first} {tm1_sht5.last} {tm1_sht5.overall}\n')
    time.sleep(2)
    print(f'{team2.name}:\n')
    time.sleep(1)
    print(f'Goalkeeper: {tm2_gk.first} {tm2_gk.last} {tm2_gk.overall}')
    time.sleep(1)
    print(f'First shooter: {tm2_sht1.first} {tm2_sht1.last} {tm2_sht1.overall}')
    time.sleep(1)
    print(f'Second shooter: {tm2_sht2.first} {tm2_sht2.last} {tm2_sht2.overall}')
    time.sleep(1)
    print(f'Third shooter: {tm2_sht3.first} {tm2_sht3.last} {tm2_sht3.overall}')
    time.sleep(1)
    print(f'Fourth shooter: {tm2_sht4.first} {tm2_sht4.last} {tm2_sht4.overall}')
    time.sleep(1)
    print(f'Fifth shooter: {tm2_sht5.first} {tm2_sht5.last} {tm2_sht5.overall}\n')
    time.sleep(3)
    print('1st ROUND')
    outcome = penalty(tm1_gk,tm2_sht1)
    update = update_result(outcome)
    team2.partial += update
    print_partial(outcome,team1,team2)

    outcome = penalty(tm2_gk,tm1_sht1)
    update = update_result(outcome)
    team1.partial += update
    print_partial(outcome,team1,team2)

    print('2nd ROUND')
    outcome = penalty(tm1_gk,tm2_sht2)
    update = update_result(outcome)
    team2.partial += update
    print_partial(outcome,team1,team2)

    outcome = penalty(tm2_gk,tm1_sht2)
    update = update_result(outcome)
    team1.partial += update
    print_partial(outcome,team1,team2)

    print('3rd ROUND')
    outcome = penalty(tm1_gk,tm2_sht3)
    update = update_result(outcome)
    team2.partial += update
    print_partial(outcome,team1,team2)

    outcome = penalty(tm2_gk,tm1_sht3)
    update = update_result(outcome)
    team1.partial += update
    print_partial(outcome,team1,team2)

    print('4th ROUND')
    outcome = penalty(tm1_gk,tm2_sht4)
    update = update_result(outcome)
    team2.partial += update
    print_partial(outcome,team1,team2)

    outcome = penalty(tm2_gk,tm1_sht4)
    update = update_result(outcome)
    team1.partial += update
    print_partial(outcome,team1,team2)

    print('5th ROUND')
    outcome = penalty(tm1_gk,tm2_sht5)
    update = update_result(outcome)
    team2.partial += update
    print_partial(outcome,team1,team2)

    outcome = penalty(tm2_gk,tm1_sht5)
    update = update_result(outcome)
    team1.partial += update
    print_partial(outcome,team1,team2)

    print(f'Final result: {team1.name}: {team1.partial} - {team2.name}: {team2.partial}')


def penalty(gk, shooter):
    time.sleep(5)
    # print(f'''GK quality: {gk.overall}, SHOOTER quality: {shooter.overall}''')
    prob_goal = 73
    prob_miss = 7
    prob_save = 20
    outcome = ['goal', 'miss', 'save']
    outcome_prob = [prob_goal,prob_miss,prob_save]
    strike_pace = [50, 75, 100]
    run_length = ['short', 'long']
    run_pace = ['slow', 'medium', 'fast']
    direction = ['left-low', 'left-high', 'center', 'right-low', 'right-high']
    shooter_strategy = ['feint', 'check', 'just-shoot']
    gk_strategy = ['just-dive','wait','distract']
    penalty_style = ['powerstrike', 'precisionstrike', 'panenka']
    penalty_outcome = random.choices(outcome, weights=(outcome_prob), k=1)
    shooter_decision = random.choices(shooter_strategy, weights=(10,25,65), k=1)
    gk_decision = random.choices(gk_strategy, weights=(60,25,15), k=1)
    chosen_style = random.choices(penalty_style, weights=(65,30,5), k=1)
    print(f'{shooter.last} ({shooter.team}) decides to {chosen_style[0]} {shooter_decision[0]} while {gk.last} ({gk.team}) decides to {gk_decision[0]}')
    if chosen_style[0] == 'powerstrike':
        if shooter.power > shooter.precision:
            power_delta = shooter.power - shooter.precision
            if power_delta > 5:
                prob_goal -= 3
                prob_miss += 3
        elif gk.diving > shooter.power:
            power_delta = gk.diving - shooter.power
            if power_delta > 5:
                prob_goal -= 5
                prob_miss += 5
    if chosen_style[0] == 'precisionstrike':
        if shooter.precision < gk.diving:
            prob_goal -= 2
            prob_save += 2
        if shooter.power < gk.instinct:
            prob_goal -= 2
            prob_save += 2
        elif gk.diving > shooter.power:
            power_delta = gk.diving - shooter.power
            if power_delta > 5:
                prob_goal -= 5
                prob_miss += 5
    if chosen_style[0] == 'panenka' and gk_decision[0] == 'wait':
                prob_goal -= 10
                prob_save += 10
    if shooter_decision[0] == 'just-shoot' and gk_decision[0] == 'just-dives':
        shot_direction = random.choice(direction)
        dive_direction = random.choice(direction)
        print(f'{shooter.last} ({shooter.team}) shots {shot_direction} and {gk.last} ({gk.team}) dives {dive_direction}')
        if shot_direction == dive_direction:
            shot_quality = shooter.power + shooter.precision
            dive_quality = gk.diving + gk.instinct
            quality_diff = dive_quality - shot_quality
            if shot_quality >= dive_quality:
                prob_goal -= 3
                prob_save += 3
                # return penalty_outcome[0]
            elif quality_diff > 10:
                prob_goal -= 8
                prob_save += 8
                # return penalty_outcome[0]
            else:
                prob_goal -= 5
                prob_save += 5
                # return penalty_outcome[0]
        else:
            prob_goal += 2
            prob_save -= 2
            # return penalty_outcome[0]
    elif shooter_decision[0] == 'check' and gk_decision[0] == 'just-dive':
        shot_quality = shooter.coolness + shooter.precision
        dive_quality = gk.concentration + gk.instinct
        quality_diff = dive_quality - shot_quality
        if shot_quality >= dive_quality:
            prob_goal += 5
            prob_save -= 5
            # return penalty_outcome[0]
        else:
            prob_goal += 3
            prob_save -= 3
            # return penalty_outcome[0]
    elif shooter_decision[0] == 'feint' and gk_decision[0] == 'just-dive':
        shot_quality = shooter.coolness + shooter.precision
        dive_quality = gk.concentration + gk.instinct
        quality_diff = dive_quality - shot_quality
        if shot_quality >= dive_quality:
            prob_goal += 4
            prob_save -= 4
            # return penalty_outcome[0]
        elif quality_diff > 10:
            prob_goal -= 2
            prob_save += 2
            # return penalty_outcome[0]
        # else:
        #     # return penalty_outcome[0]
    elif shooter_decision[0] == 'feint' and gk_decision[0] == 'wait':
        shot_quality = shooter.coolness + shooter.precision + shooter.power
        dive_quality = gk.concentration + gk.instinct + gk.diving
        quality_diff = dive_quality - shot_quality
        if shot_quality >= dive_quality:
            prob_goal -= 3
            prob_save += 3
            # return penalty_outcome[0]
        elif quality_diff > 10:
            prob_goal -= 10
            prob_save += 10
            # return penalty_outcome[0]
        else:
            prob_goal -= 6
            prob_save += 6
            # return penalty_outcome[0]
    elif shooter_decision[0] == 'check' and gk_decision[0] == 'wait':
        shot_quality = shooter.coolness + shooter.precision + shooter.power
        dive_quality = gk.concentration + gk.instinct + gk.diving
        quality_diff = dive_quality - shot_quality
        if shot_quality >= dive_quality:
            prob_goal -= 1
            prob_save += 1
            # return penalty_outcome[0]
        elif quality_diff > 10:
            prob_goal -= 5
            prob_save += 5
            # return penalty_outcome[0]
        else:
            prob_goal -= 3
            prob_save += 3
            # return penalty_outcome[0]
    elif shooter_decision[0] == 'just-shoot' and gk_decision[0] == 'wait':
        shot_quality = shooter.coolness + shooter.precision + shooter.power
        dive_quality = gk.concentration + gk.instinct + gk.diving
        quality_diff = dive_quality - shot_quality
        if shot_quality >= dive_quality:
            prob_goal -= 2
            prob_save += 2
            # return penalty_outcome[0]
        elif quality_diff > 10:
            prob_goal -= 10
            prob_save += 10
            # return penalty_outcome[0]
        else:
            prob_goal -= 5
            prob_save += 5
            # return penalty_outcome[0]
    elif shooter_decision[0] == 'feint' and gk_decision[0] == 'distract':
        shot_quality = shooter.coolness + shooter.precision + shooter.concentration
        dive_quality = gk.concentration + gk.instinct + gk.diving
        quality_diff = dive_quality - shot_quality
        if shot_quality >= dive_quality:
            prob_goal += 1
            prob_save -= 1
            # return penalty_outcome[0]
        elif quality_diff > 10:
            prob_goal -= 7
            prob_save += 7
            # return penalty_outcome[0]
        else:
            prob_goal -= 3
            prob_save += 3
            # return penalty_outcome[0]
    elif shooter_decision[0] == 'check' and gk_decision[0] == 'distract':
        shot_quality = shooter.coolness + shooter.precision + shooter.concentration
        dive_quality = gk.concentration + gk.instinct + gk.diving
        quality_diff = dive_quality - shot_quality
        if shot_quality >= dive_quality:
            prob_goal += 1
            prob_save -= 1
            # return penalty_outcome[0]
        elif quality_diff > 10:
            prob_goal -= 11
            prob_save += 11
            # return penalty_outcome[0]
        else:
            prob_goal -= 7
            prob_save += 7
            # return penalty_outcome[0]
    return penalty_outcome[0]



def update_result(outcome):
    if outcome == 'goal':
        return 1
    else:
        return 0

def print_partial(outcome, team1, team2):
        print(f'{outcome.title()}!')
        print(f'{team1.name}: {team1.partial} - {team2.name}: {team2.partial}\r\n')

match(1,6)



c.close()
