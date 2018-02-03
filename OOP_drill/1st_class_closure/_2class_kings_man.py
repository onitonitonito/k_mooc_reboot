import time
import datetime


class Agent(object):
    inventory_dict = {1:'hand_gun', 2:'hidden_knife'}
    magazine = 5
    poison = 1

    def __init__(self, u_id, u_pw):
        self.registered_time = datetime.datetime.now()
        self.id = u_id
        self.pw = u_pw
        print("YOU are registered AGENT-'{}'".format(self.id).upper())
        # print(self.registered_time.strftime("%h %m %s"))
        print("registered time = {:}".format(
            self.registered_time.strftime('%I:%M:%S'),
            ))

    def show_attribute(self):
        print('==============')
        print('My ID :', self.id)
        print('My PW :', '*' * len(str(self.pw)))
        print(' - bullet :', self.magazine)
        print(' - poison :', self.poison)
        print('==============\n\n')

kay = Agent('Jaguare', 1234)
kay.show_attribute()

class KingsMan(Agent):
    suit = 1
    shoes = 1
    magazine = Agent.magazine * 3
    poison = Agent.poison * 5

time.sleep(5)
jay = KingsMan('tiger_hope', 34455)
jay.show_attribute()


kay.show_attribute()
