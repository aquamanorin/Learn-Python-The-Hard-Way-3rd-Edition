from random import randint
from math import fabs
from ex45judge_num import judge_num

class Table(object):

    def __init__(self):
        self.table_num = 0
        self.game_num = 0
        self.guest_point = [0, 0, 0, 0, 0]
        self.host_point = [0, 0, 0, 0, 0]

    def play(self):
        print "Let's play!"
        guest_win = 0
        host_win = 0

        while guest_win < 3 and host_win < 3 and self.game_num != 5:
            print "\n-----------------------"
            print "Round %d" % (self.game_num+1)
            print "-------- Score --------"
            print "Player:", self.guest_point
            print "Host  :", self.host_point
            print "-----------------------"
            guest_num = raw_input(">The Player number is (000-999): ")
            judge_num_state = judge_num(guest_num)
            while judge_num_state is False:
                guest_num = raw_input(">Keep the number in (000-999): ")
                judge_num_state = judge_num(guest_num)

            host_num = "%d%d%d" % (randint(0,9), randint(0,9), randint(0,9))
            print ">The  Host  number is (000-999):",host_num

            std_num = "%d%d%d" % (randint(0,9), randint(0,9), randint(0,9))
            print "The standard number is:",std_num

            fabs1 = fabs(int(guest_num)-int(std_num))
            fabs2 = fabs(int(host_num)-int(std_num))
            print "Player: %d Host: %d" % (fabs1, fabs2)
            if fabs1 < fabs2:
                print "You win!"
                self.guest_point[self.game_num] += 1
            else:
                print "You lose!"
                self.host_point[self.game_num] += 1

            guest_win = sum(self.guest_point)
            host_win = sum(self.host_point)

            if guest_win == 3:
                print "\n-------- Score --------"
                print "Player:", self.guest_point
                print "Host  :", self.host_point
                print "-----------------------"
                print "You win this game!"
                print "-----------------------"
                return (1)
            elif host_win == 3:
                print "\n-------- Score --------"
                print "Player:", self.guest_point
                print "Host  :", self.host_point
                print "-----------------------"
                print "You lose this game!"
                print "-----------------------"
                return (0)
            else:
                self.game_num += 1
