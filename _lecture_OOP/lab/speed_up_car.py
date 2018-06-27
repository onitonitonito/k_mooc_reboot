FORM_INTRO = '''\
=================================
\tVEHICLE INFORMATION
---------------------------------
1. MODEL     : %s (%s)
2. MAX speed :      %3d km/h
3. ACCELARAT :   +_ %3d kmh
4. STATUS    :      %3d kmh
---------------------------------\n\n'''


class Car(object):
    # 공통적으로 필요한 기본적인 '틀'을 만든다 -- '상속'해준다
    total_count = 0

    def __init__(self, model_name):
        Car.total_count += 1
        self.intro_message = 'NEW CAR!! has come..........'
        self.attr = {
            'model':  model_name,
            'kind':   'Normal',
            'max_speed':   130,
            'speed':   0,
            'accelarate':   10,
            }
        self.intro_title()

    def __repr__(self):
        self.intro = FORM_INTRO % (
            self.attr['model'],
            self.attr['kind'],
            self.attr['max_speed'],
            self.attr['accelarate'],
            self.attr['speed'], )
        return self.intro       # __str__ 과 같은 기능

    def intro_title(self):
        print(self.intro_message)
        print(self)

    def set_speed_up(self):
        # 인스턴스 속도를 한번 '가속'시키고, 결과를 반환한다.
        if self.attr['max_speed'] - self.attr['accelarate'] > self.attr['speed']:
            self.attr['speed'] += self.attr['accelarate']
            return True         # '가속'성공 ... 여분있음: 'True' 반환
        else:
            self.attr['speed'] = self.attr['max_speed']
            return False        # '가속'후  ... 맥스도달: 'False' 반환

    def set_speed_down(self):
        # 인스턴스 속도를 한번 '감속'시키고 결과를 반환한다
        if self.attr['speed'] - self.attr['accelarate'] > 0:
            self.attr['speed'] -= self.attr['accelarate']
            return True         # '감속'성공 .. 잔여속도 있음 : 'True' 반환.
        else:
            self.attr['speed'] -= self.attr['accelarate']
            return False        # '감속'후 .. 잔여속도 없음(정지): 'False' 반환


class SportCar(Car):
    def __init__(self, model_name):
        super().__init__(model_name)
        # 부모(Super)에게 '상속'을 받은 후 필요한 부분만 교체
        self.attr['kind'] = 'Racing'
        self.attr['max_speed'] = 300
        self.attr['accelarate'] = 60





if __name__ == '__main__':
    nn = Car('NN-Car')

    while nn.attr['speed'] < nn.attr['max_speed']:
        nn.set_speed_up()
        print(nn.attr['speed'])

    print(nn)
    print(Car.total_count)

    sc = SportCar('Porsche')

    while sc.attr['speed'] < sc.attr['max_speed']:
        sc.set_speed_up()
        print(sc.attr['speed'])

    print(sc)
    print(Car.total_count)
