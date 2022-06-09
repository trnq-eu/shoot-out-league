import random
import sqlite3

conn = sqlite3.connect('penalty_db.sqlite')
c = conn.cursor()

div1_ids = [1,2,3,4,5,6,7,8]
div2_ids = [9,10,11,12,13,14,15,16]
div3_ids = [17,18,19,20,21,22,23,24]
div4_ids = [25,26,27,28,29,30,31,32]

# week1 = [(team1,team2),(team5,team6),(team3,team8),(team4,team4)]
# week2 = [(team3,team1),(team2,team4),(team5,team7),(team6,team8)]
# week3 = [(team1,team4),(team3,team2),(team8,team5),(team7,team6)]
# week4 = [(team5,team1),(team2,team6),(team4,team3),(team7,team8)]
# week5 = [(team1,team6),(team5,team2),(team3,team7),(team8,team4)]
# week6 = [(team7,team1),(team2,team8),(team3,team5),(team4,team6)]
# week7 = [(team1,team8),(team7,team2),(team6,team3),(team5,team4)]

def schedule(team_ids, season_id):
    team1 = team_ids[0]
    team2 = team_ids[1]
    team3 = team_ids[2]
    team4 = team_ids[3]
    team5 = team_ids[4]
    team6 = team_ids[5]
    team7 = team_ids[6]
    team8 = team_ids[7]
    week1 = [(team1,team2),(team5,team6),(team3,team8),(team4,team4)]
    week2 = [(team3,team1),(team2,team4),(team5,team7),(team6,team8)]
    week3 = [(team1,team4),(team3,team2),(team8,team5),(team7,team6)]
    week4 = [(team5,team1),(team2,team6),(team4,team3),(team7,team8)]
    week5 = [(team1,team6),(team5,team2),(team3,team7),(team8,team4)]
    week6 = [(team7,team1),(team2,team8),(team3,team5),(team4,team6)]
    week7 = [(team1,team8),(team7,team2),(team6,team3),(team5,team4)]
    week1_sched = [(week1[0][0],week1[0][1],season_id,1,1), (week1[1][0],week1[1][1],season_id,1,2), (week1[2][0],week1[2][1],season_id,1,3), (week1[3][0],week1[3][1],season_id,1,4)]
    week2_sched = [(week2[0][0],week2[0][1],season_id,2,1), (week2[1][0],week2[1][1],season_id,2,2), (week2[2][0],week2[2][1],season_id,2,3), (week2[3][0],week2[3][1],season_id,2,4)]
    week3_sched = [(week3[0][0],week3[0][1],season_id,3,1), (week3[1][0],week3[1][1],season_id,3,2), (week3[2][0],week3[2][1],season_id,3,3), (week3[3][0],week3[3][1],season_id,3,4)]
    week4_sched = [(week4[0][0],week4[0][1],season_id,4,1), (week4[1][0],week4[1][1],season_id,4,2), (week4[2][0],week4[2][1],season_id,4,3), (week4[3][0],week4[3][1],season_id,4,4)]
    week5_sched = [(week5[0][0],week5[0][1],season_id,5,1), (week5[1][0],week5[1][1],season_id,5,2), (week5[2][0],week5[2][1],season_id,5,3), (week5[3][0],week5[3][1],season_id,5,4)]
    week6_sched = [(week6[0][0],week6[0][1],season_id,6,1), (week6[1][0],week6[1][1],season_id,6,2), (week6[2][0],week6[2][1],season_id,6,3), (week6[3][0],week6[3][1],season_id,6,4)]
    week7_sched = [(week7[0][0],week7[0][1],season_id,7,1), (week7[1][0],week6[1][1],season_id,7,2), (week7[2][0],week7[2][1],season_id,7,3), (week7[3][0],week7[3][1],season_id,7,4)]
    week8_sched = [(week1[0][1],week1[0][0],season_id,8,1), (week1[1][1],week1[1][0],season_id,8,2), (week1[2][1],week1[2][0],season_id,8,3), (week1[3][1],week1[3][0],season_id,8,4)]
    week2_sched = [(week2[0][1],week2[0][0],season_id,9,1), (week2[1][1],week2[1][0],season_id,9,2), (week2[2][1],week2[2][0],season_id,9,3), (week2[3][1],week2[3][0],season_id,9,4)]
    week3_sched = [(week3[0][1],week3[0][0],season_id,10,1), (week3[1][1],week3[1][0],season_id,10,2), (week3[2][1],week3[2][0],season_id,10,3), (week3[3][1],week3[3][0],season_id,10,4)]
    week4_sched = [(week4[0][1],week4[0][0],season_id,11,1), (week4[1][1],week4[1][0],season_id,11,2), (week4[2][1],week4[2][0],season_id,11,3), (week4[3][1],week4[3][0],season_id,11,4)]
    week5_sched = [(week5[0][1],week5[0][0],season_id,12,1), (week5[1][1],week5[1][0],season_id,12,2), (week5[2][1],week5[2][0],season_id,12,3), (week5[3][1],week5[3][0],season_id,12,4)]
    week6_sched = [(week6[0][1],week6[0][0],season_id,13,1), (week6[1][1],week6[1][0],season_id,13,2), (week6[2][1],week6[2][0],season_id,13,3), (week6[3][1],week6[3][0],season_id,13,4)]
    week7_sched = [(week7[0][1],week7[0][0],season_id,14,1), (week7[1][1],week6[1][0],season_id,14,2), (week7[2][1],week7[2][0],season_id,14,3), (week7[3][1],week7[3][0],season_id,14,4)]

    with conn:
        c.executemany('''INSERT INTO matches (home_team_id, away_team_id, season_id,  week, game_n) VALUES (?, ?, ?, ?, ?)''', week1_sched)
    c.close()


schedule(div1_ids, 1)

