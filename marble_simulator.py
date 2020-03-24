import random
def simulate_season():
    current_standings={'savage speeders':70, 'hazers':65, 'galactic':60, 'snowballs':50, 'orangers':50, 'thunderbolts':47, 'green ducks':46, 'mellow yellow':43, 'primary':42, 'balls of chaos':26, 'limers':25, 'rojo rollers':23, 'midnight wisps':22, 'raspberry racers':19, 'momo':16, 'hornets':8}
    teams=['savage speeders', 'hazers', 'galactic', 'snowballs', 'orangers', 'thunderbolts', 'green ducks', 'mellow yellow', 'primary', 'balls of chaos', 'limers', 'rojo rollers', 'midnight wisps', 'raspberry racers', 'momo', 'hornets']
    point_totals=[70,65,60,50,50,47,46,43,42,26,25,23,22,19,16,8]
    race_1=random.sample(teams, len(teams))
    add_points_counter=1

    for i in race_1:
        if add_points_counter==1:
            point_totals[teams.index(i)]+=25
        elif add_points_counter==2:
            point_totals[teams.index(i)]+=18
        elif add_points_counter==3:
            point_totals[teams.index(i)]+=15
        elif add_points_counter==4:
            point_totals[teams.index(i)]+=12
        elif add_points_counter==5:
            point_totals[teams.index(i)]+=10
        elif add_points_counter==6:
            point_totals[teams.index(i)]+=8
        elif add_points_counter==7:
            point_totals[teams.index(i)]+=6
        elif add_points_counter==8:
            point_totals[teams.index(i)]+=4
        elif add_points_counter==9:
            point_totals[teams.index(i)]+=2
        elif add_points_counter==10:
            point_totals[teams.index(i)]+=1
        add_points_counter+=1
    point_totals[random.randint(0,15)]+=1
    race_2=random.sample(teams, len(teams))
    add_points_counter=1

    for i in race_2:
        if add_points_counter==1:
            point_totals[teams.index(i)]+=25
        elif add_points_counter==2:
            point_totals[teams.index(i)]+=18
        elif add_points_counter==3:
            point_totals[teams.index(i)]+=15
        elif add_points_counter==4:
            point_totals[teams.index(i)]+=12
        elif add_points_counter==5:
            point_totals[teams.index(i)]+=10
        elif add_points_counter==6:
            point_totals[teams.index(i)]+=8
        elif add_points_counter==7:
            point_totals[teams.index(i)]+=6
        elif add_points_counter==8:
            point_totals[teams.index(i)]+=4
        elif add_points_counter==9:
            point_totals[teams.index(i)]+=2
        elif add_points_counter==10:
            point_totals[teams.index(i)]+=1
        add_points_counter+=1
    point_totals[random.randint(0,15)]+=1
    winner=teams[point_totals.index(max(point_totals))]
    return winner

list_of_winners=[]
for i in range(10000):
    list_of_winners.append(simulate_season())
print(list_of_winners.count('savage speeders'))

