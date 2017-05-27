class SoccerPlayer(object):

    def __init__(self, name, back_number, position):
        self.name = name
        self.back_number = back_number
        self.position = position

    def __str__(self):
        self.intro = "D'oh!"
        return self.intro

    def view_player_information(self):
        print('My name is %s my position is %s' %(name, position))

    def change_player_information(self, new_number):
        print("changed back number from %d to %d" %(self.back_number, new_number))
        self.back_number = new_number
