from ex45table import Table
from sys import exit

t1 = t2 = t3 = t4 = t5 = 0
n = 1
table_map = [t1, t2, t3, t4, t5]

g_point = [0, 0, 0, 0, 0]
h_point = [0, 0, 0, 0, 0]
g_win = 0
h_win = 0

for i in table_map:
    i = Table()
    print "\n--------------------------------------\n"
    print "Welcome to Table Game. This is GAME #%d." % n
    game_result = i.play()
    if game_result == 1:
        i = 1
        g_win += 1
        g_point[n-1] = 1
    else:
        i = 0
        h_win += 1
        h_point[n-1] = 1
    print "****** Game Score ******"
    print "Player:", g_point
    print "Host  :", h_point
    print "************************"
    if g_win == 3:
        print "\n--------------------------------\n"
        print "********************************"
        print "*WINNER WINNER, CHICKEN DINNER!*"
        print "********************************"
        exit(1)
    elif h_win == 3:
        print "\n-----------------------------\n"
        print "*****************************"
        print "*LOSER LOSER, WHAT A SUCKER!*"
        print "*****************************"
        exit(1)
    else:
        n += 1

