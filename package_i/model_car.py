FORM_INTRO='''\
=================================
\tVEHICLE INFORMATION
---------------------------------
1. MODEL     : %s (%s)
2. MAX SPEED :      %d km/h
3. ACCELARAT :   +_ %d kmh
4. STATUS    :      %d kmh
---------------------------------\n\n\n'''

class Car(object):
    def __init__(self,arg_model):
        self.attr = {
            'MODEL'      :  arg_model,
            'KIND'      :   'Normal',
            'MAX_SPEED' :   130,
            'SPEED'     :   0,
            'S_ABLE'    :   20,
        }
        print('NEW CAR!! has come..........')
        print(self.__str__())

    def __str__(self):
        self.intro = FORM_INTRO %(
            self.attr['MODEL'],self.attr['KIND'],self.attr['MAX_SPEED'],
            self.attr['S_ABLE'],self.attr['SPEED'], )
        return self.intro

    def speed_up(self):
        self.attr['SPEED'] += self.attr['S_ABLE']

        if self.attr['SPEED'] <= self.attr['MAX_SPEED']:
            print("%s: SPEED IS UP! .... NOW %s km/h" %(self.attr['MODEL'],self.attr['SPEED'],) )
        else:
            self.attr['SPEED'] = self.attr['MAX_SPEED']
            print("\nSORRY! SPEED IS LIMITED! @ %s km/h" %self.attr['SPEED'])
            print(self.__str__())

    def speed_down(self):
        self.attr['SPEED'] -= self.attr['S_ABLE']

        if self.attr['SPEED'] >= 0:
            print("%s: SPEED IS DOWN! .... NOW %s km/h" %(self.attr['MODEL'],self.attr['SPEED'],) )
        else:
            self.attr['SPEED'] = 0
            print("\nSORRY! CAR STOPPED! @ %s km/h" %self.attr['SPEED'])
            print(self.__str__())


class SportCar(Car):
    def __init__(self,arg_model):
        self.attr = {
            'MODEL'      :  arg_model,
            'KIND'      :   'Racing',
            'MAX_SPEED' :   300,
            'SPEED'     :   0,
            'S_ABLE'    :   60,
        }
        print('NEW CAR!! has come..........')
        print(self.__str__())


class Truck(Car):
    def __init__(self,arg_model):
        self.attr = {
            'MODEL'      :  arg_model,
            'KIND'      :   'Truck',
            'MAX_SPEED' :   80,
            'SPEED'     :   0,
            'S_ABLE'    :   10,
        }
        print('NEW CAR!! has come..........')
        print(self.__str__())


class Cart(Car):
    def __init__(self,arg_model):
        self.attr = {
            'MODEL'      :  arg_model,
            'KIND'      :   'Cart?',
            'MAX_SPEED' :   5,
            'SPEED'     :   0,
            'S_ABLE'    :   1,
        }
        print('NEW CAR has come..........!!?? Crazy??')
        print(self.__str__())
