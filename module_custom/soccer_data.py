class SoccerPlayer(object):
    def __init__(self, idx, name, b_number, position):
        self.UID_LIST = ['unins','tamtam','funxd','nitto','haha','hehe','hoho',]
        self.NAME_LIST = ["Alan","Steve","Geremy","Kris","Liam","Aiden","Willam",]
        self.POS_LIST = ["FW","FW","MF","MF","DF","GK","MF",]
        self.BNUM_LIST = [18,10,13,12,11,1,17,]

        self.PLAYER_DICT = { p_id:[p_name, p_position, p_number]
            for p_id, p_name, p_position, p_number
            in zip(self.UID_LIST, self.NAME_LIST, self.POS_LIST, self.BNUM_LIST)
            }

        self.PLAYER_DICT[idx]=[name, position, b_number]
        print('DONE .. Player: {%s}/{%d} is added in PLAYER_DICT @{%s}\n' %(name, b_number,len(self.PLAYER_DICT)) )

    def __str__(self):
        return self.NAME_LIST[-1]        # name

    def view_player_data(self,uid):
        self.intro = "\
##    Hi~!, My name is {%s},\n\
##    I'm Playing as {%s} in National Soccer Team.\n\
##    My back number is {%s}"%(
self.PLAYER_DICT[uid][0], self.PLAYER_DICT[uid][1], self.PLAYER_DICT[uid][2],)

        print("#"*10," %s(%s)'s' INFORMATION  "%(self.PLAYER_DICT[uid][0],uid),"#"*13)
        print(self.intro)
        print("#"*55,"\n")

    def view_player_dict(self):
        n = 0
        for uid in self.PLAYER_DICT.keys():
            n+=1
            print("\t%d.%s = "%(n,uid),self.PLAYER_DICT[uid])
        print()

    def change_player_position(self, uid, new_pos):
        old_pos = self.PLAYER_DICT[uid][1]
        self.PLAYER_DICT[uid][1] = new_pos
        print(
            "{position} CHANGED: --------\
            \n\t{%s[%s]'s} old position:{%s} is changed to New position:{%s}~!!\n"
            %(self.PLAYER_DICT[uid][0],uid, old_pos, self.PLAYER_DICT[uid][1]),
        )
        self.view_player_dict()

    def change_player_number(self, uid, new_number):
        old_number = self.PLAYER_DICT[uid][2]
        self.PLAYER_DICT[uid][2] = new_number
        print(
            "{number} CHANGED: -----------\
            \n\t{%s[%s]'s} old number:{%d} is changed to New number:{%d}~!!\n"
            %(self.PLAYER_DICT[uid][0],uid, old_number, self.PLAYER_DICT[uid][2])
        )
        self.view_player_dict()

    def add_player(self, uid, name, position, b_number):
        self.PLAYER_DICT[uid] = [name,position,b_number]
        print(
"1 player( %s[%s],%s,%d) is added. Total %s players were registered."
%(name,uid,position,b_number,len(self.PLAYER_DICT))
        )
        self.view_player_dict()


class TemporaryClass():
    pass


class Useless():
    pass
