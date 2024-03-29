#Dominik Wrobel 2023

#list of all possible places pieces can be scored
#First chaarcter: B is Box/cuBe: C is Cone: A is All
#Second character is determining the level, E.G in B38, 3 would symbolize it is on the 3rd level
#Third character is determining the position, E.G in C26, the 6 represents that it is the 6th in it's row in that level
places = ["C31","B32","C33","C34","B35","C36","C37","B38","C39","C21","B22","C23","C24","B25","C26","C27","B28","C29","A11","A12","A13","A14","A15","A16","A17","A18","A19"]

bot1_piece = (input("bot_1 piece CUBE,CONE, or BOTH? "))[2].upper()
bot1_level = int(input("bot level? 1,2 or 3"))
bot2_piece = (input("bot_2 piece CUBE,CONE, or BOTH? "))[2].upper()
bot2_level = int(input("bot level? 1,2 or 3"))
bot3_piece = (input("bot_3 piece CUBE,CONE, or BOTH? "))[2].upper()
bot3_level = int(input("bot level? 1,2 or 3"))

def bot(piece, level):
#Variable assignment
    time_auto = 15
    time_tele = 132
    load_time_low = 3
    load_time_med = 8
    load_time_high = 11
    tele_pickup_time = 10
    auto_pickup_time = 6

    # indents the "places" list so the code only reads the level it is assigned to
    if piece == "B": #Checks if the game piece selected is a cuBe

        points = 0

        for i in range(27): #repeats for every possible selection in place

                if int(places[i][1]) == 1: #looks at the level and determines how much time that would take
                    level_diff = load_time_low

                if int(places[i][1]) == 2:
                    level_diff = load_time_med

                if int(places[i][1]) == 3:
                    level_diff = load_time_high

                if places[i][-1] != "!" and places[i][-1] != "L":

                    if places[i][0] == "A" or places[i][0] == "B":#Checks if the game piece selected is a cuBe or All

                        if level >= int(places[i][1]): #checks if the robot is able to score on the level of the piece

                            if time_tele - (level_diff + tele_pickup_time) >= 0: #Checks if the robot has time to get said piece

                                time_tele -= (level_diff + tele_pickup_time)#subtracts the time it took to get and score the piece from the time remaining

                                places[i] = places[i] + "!"


                                # deternmines the points based on the level
                                if int(places[i][1]) == 1:
                                    level_points = 2

                                if int(places[i][1]) == 2:
                                    level_points = 3

                                if int(places[i][1]) == 3:
                                    level_points = 5

                                print("scored " + str(level_points) +" on" + places[i])

                                points = points + level_points


    if piece == "N":  # Checks if the game piece selected is a coNe

        points = 0

        for i in range(27):  # repeats for every possible selection in place

            if int(places[i][1]) == 1:  # looks at the level and determines how much time that would take
                level_diff = load_time_low

            if int(places[i][1]) == 2:
                level_diff = load_time_med

            if int(places[i][1]) == 3:
                level_diff = load_time_high

            if places[i][-1] != "!" and places[i][-1] != "L":

                if places[i][0] == "A" or places[i][0] == "C":  # Checks if the game piece selected is a Cone or All

                    if level >= int(places[i][1]):  # checks if the robot is able to score on the level of the piece

                        if time_tele - (level_diff + tele_pickup_time) >= 0:  # Checks if the robot has time to get said piece

                            time_tele -= (
                                        level_diff + tele_pickup_time)  # subtracts the time it took to get and score the piece from the time remaining

                            places[i] = places[i] + "!"

                            # deternmines the points based on the level
                            if int(places[i][1]) == 1:
                                level_points = 2

                            if int(places[i][1]) == 2:
                                level_points = 3

                            if int(places[i][1]) == 3:
                                level_points = 5

                            print("scored " + str(level_points) + " on" + places[i])

                            points = points + level_points



    if piece == "T":  # Checks if the game piece selected is boTh

        points = 0

        for i in range(27):  # repeats for every possible selection in place

            if int(places[i][1]) == 1:  # looks at the level and determines how much time that would take
                level_diff = load_time_low

            if int(places[i][1]) == 2:
                level_diff = load_time_med

            if int(places[i][1]) == 3:
                level_diff = load_time_high

            if places[i][-1] != "!" and places[i][-1] != "L":

                if places[i][0] == "A" or places[i][0] == "C" or places[i][0] == "B":  # Checks if the game piece selected is a Cone, cuBe or All

                    if level >= int(places[i][1]):  # checks if the robot is able to score on the level of the piece

                        if time_tele - (level_diff + tele_pickup_time) >= 0:  # Checks if the robot has time to get said piece

                            time_tele -= (level_diff + tele_pickup_time)  # subtracts the time it took to get and score the piece from the time remaining

                            places[i] = places[i] + "!" #adds a symbol to tell the program that htis spot has already been scored on

                            # deternmines the points based on the level
                            if int(places[i][1]) == 1:
                                level_points = 2

                            if int(places[i][1]) == 2:
                                level_points = 3

                            if int(places[i][1]) == 3:
                                level_points = 5

                            print("scored " + str(level_points) + " on" + places[i])

                            points = points + level_points

    #Link checker
    for i in range(27):  # repeats for every possible selection in place
        if places[i-1][-1] == "!" and places[i][-1] == "!" and places[i+1][-1] == "!" and i != 0 and i != 8 and i != 9 and i != 17 and i != 18 and i != 26: #chacks if the pieces bside are activated and makes sure it ony checks peices that can have a piece on both sides
            points += 5
            print("link!")
            #adds an L on the end so these pieces can't be used for more than one link
            places[i - 1] += "L"
            places[i] += "L"
            places[i + 1] += "L"






    return points




print((bot(bot1_piece,bot1_level)) + (bot(bot2_piece,bot2_level)) + (bot(bot3_piece,bot3_level)))
print("^^ Total team points ^^")
print(places)
