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

FORM_MESSAGE ='''\
 +__+__+__+__+__+__+__+__+__+__+__+\n
 %s
 +^^+^^+^^+^^+^^+^^+^^+^^+^^+^^+^^\n'''

class Charactor(object):
    def __init__(self, name):
        self.attribution = {
            'NAME'  : name,
            'TRIBE' : 'common',
            'LIFE'  : 1000,
            'ABLE'  : 'Walking',
            'HIT'   : 50, }

    def __str__(self):
        self.intro = FORM_INFORMATION % (
            self.attribution['NAME'],
            self.attribution['TRIBE'],
            self.attribution['LIFE'],
            self.attribution['HIT'],
            self.attribution['ABLE'],
            self.attribution['HIT'], )
        return self.intro

    def attacked(self, arg_hit, verbose=None):
        self.damage = arg_hit
        self.attribution['LIFE'] -= self.damage

        if verbose != None:
            message = "   You(%s)'re under attack!!! \n   Life reduced by {-%d} points. \n   LIFE: {%d} remains\n"
            combine = message % (
                self.attribution['NAME'],
                self.damage,
                self.attribution['LIFE'])
            print(FORM_MESSAGE % combine )
        else:
            message = "\t%s: ** Auch!! .. (%s) **"
            print(message % (
                self.attribution['NAME'],
                self.attribution['LIFE']), )

        if self.attribution['LIFE'] <= 0:
            # os.system('cls')
            print("\n\n\n\n\n\n\n\n\n")
            print("%s(%s) is dead.. LIFE:%s \n\n\n== GAME OVER ==\n\n\n\n\n" %(
                self.attribution['NAME'],
                self.attribution['TRIBE'],
                self.attribution['LIFE'],) )

    def assult(self, obj_name):
        self.other = obj_name
        message = "[ %s(%s) ] attacked [ %s(%s) ] .... {%s} \nby -{%s} hit points"
        print( message % (
            self.attribution['NAME'],
            self.attribution['TRIBE'],
            self.other.attribution['NAME'],
            self.other.attribution['TRIBE'],
            self.attribution['ABLE'],
            self.attribution['HIT']), )
        self.other.attacked(arg_hit=self.attribution['HIT'], verbose=None)

class Warrior(Charactor):
    def __init__(self, name):
        self.attribution = {
            'NAME'  : name,
            'TRIBE' : 'Warrior',
            'LIFE'  : 1500,
            'ABLE'  : 'Throw deadlest AXE',
            'HIT'   : 400, }

class Magician(Charactor):
    def __init__(self, name):
        self.attribution = {
            'NAME'  : name,
            'TRIBE' : 'Magician',
            'LIFE'  : 500,
            'ABLE'  : 'Throw Masic Spell',
            'HIT'   : 300, }

class Begger(Charactor):
    def __init__(self, name):
        self.attribution = {
            'NAME'  : name,
            'TRIBE' : 'Begger',
            'LIFE'  : 100,
            'ABLE'  : 'Throw trash bean',
            'HIT'   : 5, }


def main():
    a1 = Magician('MIST')
    a2 = Magician('LIST')
    a3 = Magician('KIST')
    a4 = Magician('FIST')

    # a1.assult(a2)

if __name__ == '__main__':
    main()


'''refer: OOP drill - Data Science with Python
https://goo.gl/71NsFY
'''
