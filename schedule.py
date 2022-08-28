import random
import sqlite3

conn = sqlite3.connect('penalty_db.sqlite')
c = conn.cursor()

div1_ids = [1,2,3,4,5,6,7,8]
div2_ids = [9,10,11,12,13,14,15,16]
div3_ids = [17,18,19,20,21,22,23,24]
div4_ids = [25,26,27,28,29,30,31,32]

# week1 = [(team1,team2),(team5,team6),(team3,team8),(team4,team7)]
# week2 = [(team3,team1),(team2,team4),(team5,team7),(team6,team8)]
# week3 = [(team1,team4),(team3,team2),(team8,team5),(team7,team6)]
# week4 = [(team5,team1),(team2,team6),(team4,team3),(team7,team8)]
# week5 = [(team1,team6),(team5,team2),(team3,team7),(team8,team4)]
# week6 = [(team7,team1),(team2,team8),(team3,team5),(team4,team6)]
# week7 = [(team1,team8),(team7,team2),(team6,team3),(team5,team4)]




def schedule_reg_season(team_ids, season_id, division_id):
    team1 = team_ids[0]
    team2 = team_ids[1]
    team3 = team_ids[2]
    team4 = team_ids[3]
    team5 = team_ids[4]
    team6 = team_ids[5]
    team7 = team_ids[6]
    team8 = team_ids[7]
    week1 = [(team1,team2),(team5,team6),(team3,team8),(team4,team7)]
    week2 = [(team3,team1),(team2,team4),(team5,team7),(team6,team8)]
    week3 = [(team1,team4),(team3,team2),(team8,team5),(team7,team6)]
    week4 = [(team5,team1),(team2,team6),(team4,team3),(team7,team8)]
    week5 = [(team1,team6),(team5,team2),(team3,team7),(team8,team4)]
    week6 = [(team7,team1),(team2,team8),(team3,team5),(team4,team6)]
    week7 = [(team1,team8),(team7,team2),(team6,team3),(team5,team4)]
    week1_sched = [(week1[0][0],week1[0][1],season_id,division_id,1,1), (week1[1][0],week1[1][1],season_id,division_id,1,2), (week1[2][0],week1[2][1],season_id,division_id,1,3), (week1[3][0],week1[3][1],season_id,division_id,1,4)]
    week2_sched = [(week2[0][0],week2[0][1],season_id,division_id,2,1), (week2[1][0],week2[1][1],season_id,division_id,2,2), (week2[2][0],week2[2][1],season_id,division_id,2,3), (week2[3][0],week2[3][1],season_id,division_id,2,4)]
    week3_sched = [(week3[0][0],week3[0][1],season_id,division_id,3,1), (week3[1][0],week3[1][1],season_id,division_id,3,2), (week3[2][0],week3[2][1],season_id,division_id,3,3), (week3[3][0],week3[3][1],season_id,division_id,3,4)]
    week4_sched = [(week4[0][0],week4[0][1],season_id,division_id,4,1), (week4[1][0],week4[1][1],season_id,division_id,4,2), (week4[2][0],week4[2][1],season_id,division_id,4,3), (week4[3][0],week4[3][1],season_id,division_id,4,4)]
    week5_sched = [(week5[0][0],week5[0][1],season_id,division_id,5,1), (week5[1][0],week5[1][1],season_id,division_id,5,2), (week5[2][0],week5[2][1],season_id,division_id,5,3), (week5[3][0],week5[3][1],season_id,division_id,5,4)]
    week6_sched = [(week6[0][0],week6[0][1],season_id,division_id,6,1), (week6[1][0],week6[1][1],season_id,division_id,6,2), (week6[2][0],week6[2][1],season_id,division_id,6,3), (week6[3][0],week6[3][1],season_id,division_id,6,4)]
    week7_sched = [(week7[0][0],week7[0][1],season_id,division_id,7,1), (week7[1][0],week6[1][1],season_id,division_id,7,2), (week7[2][0],week7[2][1],season_id,division_id,7,3), (week7[3][0],week7[3][1],season_id,division_id,7,4)]
    week8_sched = [(week1[0][1],week1[0][0],season_id,division_id,8,1), (week1[1][1],week1[1][0],season_id,division_id,8,2), (week1[2][1],week1[2][0],season_id,division_id,8,3), (week1[3][1],week1[3][0],season_id,division_id,8,4)]
    week9_sched = [(week2[0][1],week2[0][0],season_id,division_id,9,1), (week2[1][1],week2[1][0],season_id,division_id,9,2), (week2[2][1],week2[2][0],season_id,division_id,9,3), (week2[3][1],week2[3][0],season_id,division_id,9,4)]
    week10_sched = [(week3[0][1],week3[0][0],season_id,division_id,10,1), (week3[1][1],week3[1][0],season_id,division_id,10,2), (week3[2][1],week3[2][0],season_id,division_id,10,3), (week3[3][1],week3[3][0],season_id,division_id,10,4)]
    week11_sched = [(week4[0][1],week4[0][0],season_id,division_id,11,1), (week4[1][1],week4[1][0],season_id,division_id,11,2), (week4[2][1],week4[2][0],season_id,division_id,11,3), (week4[3][1],week4[3][0],season_id,division_id,11,4)]
    week12_sched = [(week5[0][1],week5[0][0],season_id,division_id,12,1), (week5[1][1],week5[1][0],season_id,division_id,12,2), (week5[2][1],week5[2][0],season_id,division_id,12,3), (week5[3][1],week5[3][0],season_id,division_id,12,4)]
    week13_sched = [(week6[0][1],week6[0][0],season_id,division_id,13,1), (week6[1][1],week6[1][0],season_id,division_id,13,2), (week6[2][1],week6[2][0],season_id,division_id,13,3), (week6[3][1],week6[3][0],season_id,division_id,13,4)]
    week14_sched = [(week7[0][1],week7[0][0],season_id,division_id,14,1), (week7[1][1],week6[1][0],season_id,division_id,14,2), (week7[2][1],week7[2][0],season_id,division_id,14,3), (week7[3][1],week7[3][0],season_id,division_id,14,4)]

    with conn:
        c.executemany('''INSERT INTO matches (home_team_id, away_team_id, season_id, division_id, week, game_n) VALUES (?, ?, ?, ?, ?, ?)''', week1_sched)
        c.executemany('''INSERT INTO matches (home_team_id, away_team_id, season_id, division_id, week, game_n) VALUES (?, ?, ?, ?, ?, ?)''', week2_sched)
        c.executemany('''INSERT INTO matches (home_team_id, away_team_id, season_id, division_id, week, game_n) VALUES (?, ?, ?, ?, ?, ?)''', week3_sched)
        c.executemany('''INSERT INTO matches (home_team_id, away_team_id, season_id, division_id, week, game_n) VALUES (?, ?, ?, ?, ?, ?)''', week4_sched)
        c.executemany('''INSERT INTO matches (home_team_id, away_team_id, season_id, division_id, week, game_n) VALUES (?, ?, ?, ?, ?, ?)''', week5_sched)
        c.executemany('''INSERT INTO matches (home_team_id, away_team_id, season_id, division_id, week, game_n) VALUES (?, ?, ?, ?, ?, ?)''', week6_sched)
        c.executemany('''INSERT INTO matches (home_team_id, away_team_id, season_id, division_id, week, game_n) VALUES (?, ?, ?, ?, ?, ?)''', week7_sched)
        c.executemany('''INSERT INTO matches (home_team_id, away_team_id, season_id, division_id, week, game_n) VALUES (?, ?, ?, ?, ?, ?)''', week8_sched)
        c.executemany('''INSERT INTO matches (home_team_id, away_team_id, season_id, division_id, week, game_n) VALUES (?, ?, ?, ?, ?, ?)''', week9_sched)
        c.executemany('''INSERT INTO matches (home_team_id, away_team_id, season_id, division_id, week, game_n) VALUES (?, ?, ?, ?, ?, ?)''', week10_sched)
        c.executemany('''INSERT INTO matches (home_team_id, away_team_id, season_id, division_id, week, game_n) VALUES (?, ?, ?, ?, ?, ?)''', week11_sched)
        c.executemany('''INSERT INTO matches (home_team_id, away_team_id, season_id, division_id, week, game_n) VALUES (?, ?, ?, ?, ?, ?)''', week12_sched)
        c.executemany('''INSERT INTO matches (home_team_id, away_team_id, season_id, division_id, week, game_n) VALUES (?, ?, ?, ?, ?, ?)''', week13_sched)
        c.executemany('''INSERT INTO matches (home_team_id, away_team_id, season_id, division_id, week, game_n) VALUES (?, ?, ?, ?, ?, ?)''', week14_sched)
    
def create_purgatory(season_id):
    c.execute('SELECT season_id, team_id FROM league_tables WHERE division_id = ? ORDER BY PPG DESC', ('1'))
    div1_teams = c.fetchall()
    c.execute('SELECT season_id, team_id FROM league_tables WHERE division_id = ? ORDER BY PPG DESC', ('2'))
    div2_teams = c.fetchall()
    c.execute('SELECT season_id, team_id FROM league_tables WHERE division_id = ? ORDER BY PPG DESC', ('3'))
    div3_teams = c.fetchall()
    c.execute('SELECT season_id, team_id FROM league_tables WHERE division_id = ? ORDER BY PPG DESC', ('4'))
    div4_teams = c.fetchall()
    division_a_teams = [div1_teams[2][1], div2_teams[3][1], div3_teams[4][1], div4_teams[5][1]]
    division_b_teams = [div1_teams[5][1], div2_teams[2][1], div3_teams[3][1], div4_teams[4][1]]
    division_c_teams = [div1_teams[4][1], div2_teams[5][1], div3_teams[2][1], div4_teams[3][1]]
    division_d_teams = [div1_teams[3][1], div2_teams[4][1], div3_teams[5][1], div4_teams[2][1]]
    division_a = [(season_id,division_a_teams[0],5,0,0,0,0,0,0),(season_id,division_a_teams[1],5,0,0,0,0,0,0),(season_id,division_a_teams[2],5,0,0,0,0,0,0),(season_id,division_a_teams[3],5,0,0,0,0,0,0)]
    division_b = [(season_id,division_b_teams[0],6,0,0,0,0,0,0),(season_id,division_b_teams[1],6,0,0,0,0,0,0),(season_id,division_b_teams[2],6,0,0,0,0,0,0),(season_id,division_b_teams[3],6,0,0,0,0,0,0)]
    division_c = [(season_id,division_c_teams[0],7,0,0,0,0,0,0),(season_id,division_c_teams[1],7,0,0,0,0,0,0),(season_id,division_c_teams[2],7,0,0,0,0,0,0),(season_id,division_c_teams[3],7,0,0,0,0,0,0)]
    division_d = [(season_id,division_d_teams[0],8,0,0,0,0,0,0),(season_id,division_d_teams[1],8,0,0,0,0,0,0),(season_id,division_d_teams[2],8,0,0,0,0,0,0),(season_id,division_d_teams[3],8,0,0,0,0,0,0)]
    
    with conn:
        c.executemany('''INSERT INTO league_tables (season_id, team_id, division_id, points, goal_diff, wins, draws, losses, games_played)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', division_a)
        c.executemany('''INSERT INTO league_tables (season_id, team_id, division_id, points, goal_diff, wins, draws, losses, games_played)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', division_b)
        c.executemany('''INSERT INTO league_tables (season_id, team_id, division_id, points, goal_diff, wins, draws, losses, games_played)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', division_c)
        c.executemany('''INSERT INTO league_tables (season_id, team_id, division_id, points, goal_diff, wins, draws, losses, games_played)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', division_d)

create_purgatory(1)
# schedule_reg_season(div1_ids, 1, 1)
# schedule_reg_season(div2_ids, 1, 2)
# schedule_reg_season(div3_ids, 1, 3)
# schedule_reg_season(div4_ids, 1, 4)

c.close()
