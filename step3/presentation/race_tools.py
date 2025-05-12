# race_tools.py

import random

def race_time(top_speed, distance):

    driver_factor = random.uniform(0.5, 1.0)  
    total_time = (distance / (top_speed * driver_factor)) * 3600

    minuts = int(total_time // 60)
    seconds = int((total_time % 60))

    return f"{minuts:02d}:{seconds:02d}"


def scoreboard(tournament_outcome):
    report_list = tournament_outcome.split(';')
    del report_list[0::2]
    cleaned = [li.split('-') for li in report_list]
    tab = [" Race Car     | 1st | 2nd | 3rd |score"]
    table = []
    wins = {}
    secp = {}
    third = {}

    for par in cleaned:
        wins[par[0]] = wins.get(par[0], 0) + 1
        secp[par[1]] = secp.get(par[1], 0) + 1
        third[par[2]] = third.get(par[2], 0) + 1

    points = {
        key: 100* wins.get(key,0) + 40* secp.get(key,0) + 10* third.get(key,0) 
        for key in cleaned[0]
    } 

    for k in cleaned[0][:-1]:           
        table.append("{0:14}|{1:>4} |{2:>4} |{3:>4} |{4:>4} ".format(k, wins.get(k,0),secp.get(k,0),third.get(k,0),points.get(k,0)))
    
    table = sorted(table, key =lambda line: (-int(line[-5:]), line[0]))

    return tab + table