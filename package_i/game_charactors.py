FORM_INFORMATION='''\
=================================
\tTRIBE INFORMATION
---------------------------------
1.NAME(Trb): %s (%s)
2.HEALTH   : %s HP
3.HIT_POINT: %s points
4.ABBILATY : %s / [Demage:-%d]
---------------------------------
=================================\n\n'''

FORM_MESSAGE ='''\n+__+__+__+__+__+__+__+__+__+__+__+%s+^^+^^+^^+^^+^^+^^+^^+^^+^^+^^+^^\n'''


class Charactor(object):
    def __init__(self, name):
        self.super = {
            'NAME'  : name,
            'TRIBE' : 'common',
            'LIFE'  : 1000,
            'ABLE'  : 'Walking',
            'HIT'   : 50, }
        print(self.__str__())

    def __str__(self):
        self.intro = FORM_INFORMATION %(
            self.super['NAME'], self.super['TRIBE'], self.super['LIFE'], self.super['HIT'],
            self.super['ABLE'],self.super['HIT'], )

        return self.intro

    def attacked(self, arg_hit, verbose=None):
        self.damage = arg_hit
        self.super['LIFE'] -=self.damage

        if verbose != None:
            message = "\n   You(%s)'re under attack!!! \n   Life reduced by {-%d} points. \n   LIFE: {%d} remains\n"
            combine = message %(self.super['NAME'], self.damage, self.super['LIFE'])
            print(FORM_MESSAGE % combine )
        else:
            message = "\t%s: ** Auch!! .. (%s) **"
            print(message %(self.super['NAME'], self.super['LIFE']), )

        if self.super['LIFE'] <= 0:
            # os.system('cls')
            print("\n\n\n\n\n\n\n\n\n")
            print("%s(%s) is dead.. LIFE:%s \n\n\n== GAME OVER ==\n\n\n\n\n" %(
                self.super['NAME'],
                self.super['TRIBE'],
                self.super['LIFE'],) )

    def assult(self, obj_name):
        self.other = obj_name
        message = "\n[ %s(%s) ] attacked [ %s(%s) ] .... {%s} \nby -{%s} hit points"
        print( message % (self.super['NAME'],self.super['TRIBE'],self.other.super['NAME'],self.other.super['TRIBE'],
         self.super['ABLE'] ,self.super['HIT']), )
        self.other.attacked(arg_hit=self.super['HIT'], verbose=None)



class Warrior(Charactor):
    def __init__(self, name):
        self.super = {
            'NAME'  : name,
            'TRIBE' : 'Warrior',
            'LIFE'  : 1500,
            'ABLE'  : 'Throw deadlest AXE',
            'HIT'   : 400, }
        print(self.__str__())



class Magician(Charactor):
    def __init__(self, name):
        self.super = {
            'NAME'  : name,
            'TRIBE' : 'Magician',
            'LIFE'  : 500,
            'ABLE'  : 'Throw Masic Spell',
            'HIT'   : 300, }
        print(self.__str__())



class Begger(Charactor):
    def __init__(self, name):
        self.super = {
            'NAME'  : name,
            'TRIBE' : 'Begger',
            'LIFE'  : 100,
            'ABLE'  : 'Throw trash bean',
            'HIT'   : 5, }
        print(self.__str__())
