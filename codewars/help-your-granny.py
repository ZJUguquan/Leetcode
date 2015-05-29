
friends1 = ["A1", "A2", "A3", "A4", "A5"]
fTowns1 = [["A1", "X1"], ["A2", "X2"], ["A3", "X3"], ["A4", "X4"]]
distTable1 = {"X1": 100.0, "X2": 200.0, "X3": 250.0, "X4": 300.0}
#test.assert_equals(tour(friends1, fTowns1, distTable1), 889)


def tour(friends, friend_towns, home_to_town_distances):
    d, last_distance = 0, 0
    for friend, town in friend_towns:

        if town in home_to_town_distances:
            this_distance = home_to_town_distances[town]
            print friend, town, this_distance
            if d == 0:
                d += this_distance
                last_distance = this_distance
            else:
                if this_distance > last_distance:
                    d += (this_distance**2 - last_distance**2)**.5
                    last_distance = this_distance
    d += home_to_town_distances[town]
    return int(round(d, 0))

print tour(friends1, fTowns1, distTable1)

########################################################################

def tour(friends, friend_towns, home_to_town_distances):

    d, last_distance = 0, 0

    friend_towns = [ (friend, town)  for (friend, town) in friend_towns if friend in friends]
    print friends,
    print friend_towns,
    print home_to_town_distances
    for friend, town in friend_towns:
        if friend not in friends: continue

        if town in home_to_town_distances :
            this_distance = home_to_town_distances[town]
            print friend, town, this_distance
            if d == 0:
                d += this_distance
                last_distance = this_distance
            else:
                if this_distance > last_distance:
                    d += (this_distance**2 - last_distance**2)**.5
                    last_distance = this_distance

    #town = friend_towns
    print town
    d += home_to_town_distances[town]
    print d
    return int(d) # int(round(d, 0))




