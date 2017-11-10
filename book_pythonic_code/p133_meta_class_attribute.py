#! python
""" 'The RULE of Least Surprise' :
 Use at least complicate mathod that anyone elses aren't familiar with.
 BETTER WAY 29 - Use @property, instead of using Getter & Setter
 """

class Old_Registor(object):
    """ NORM in others but NOT Python
    Conception : Getter & Setter aren't Pythonic at all !!
    """
    def __init__(self, ohms):
        """ double under score = secret value """
        self.__ohms = ohms

    def get_ohms(self):
        """ This Is Getter : get value """
        return self.__ohms

    def set_ohms(self, ohms):
        """ This Is Setter : change value """
        self.__ohms = ohms


def test1_use_getter_setter():
    """ .. aren't Pythonic..!! """
    r0 = Old_Registor(50e3)
    # print('BEFORE= ', r0.__ohms)
    # # AttributeError: 'old_registor' object has no attribute '__ohms'
    print('BEFORE= ', r0.get_ohms())
    r0.set_ohms(30e3)
    print('... r0.set_ohms(30e3) ...\n')
    print('AFTER.1= ', r0.get_ohms())

    r0.set_ohms(r0.get_ohms() + 50e3)
    print('... r0.set_ohms(r0.get_ohms() + 50e3) ...\n')
    print('AFTER.2= ', r0.get_ohms())
# test1_use_getter_setter()


class Py_Registor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


def test1_dont_use_be_pythonic():
    """ This is the same & Pythonic """
    r1 = Py_Registor(50e3)

    print('BEFORE= ', r1.ohms)
    r1.ohms = 30e3
    print('... r1.ohms = 30e3 ...\n')
    print('AFTER.1= ', r1.ohms)

    r1.ohms += 50e3
    print('... r1.ohms += 50e3 ...\n')
    print('AFTER.2= ', r1.ohms)
# test1_dont_use_be_pythonic()


class Voltage_Resistance(Py_Registor):
    def __init__(self, ohms):
        """ V,I = 0, ohms = ohms / _voltage = 0 : RESET ALL,  """
        super().__init__(ohms)
        self._voltage = 0

    # Define Built-in Decorator @property voltage() = _voltage (temp)
    @property
    def voltage(self):
        """ voltage() = _voltage  :temp """
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        """ V = IR, I = V/R """
        self._voltage = voltage
        self.current = self._voltage / self.ohms


def test2_current_decorate():
    """ How to use b/i-Decorator @property & Setter
     - Define =  @property,      voltage()..1
     - Setting = @volage.setter, voltage(Volt)..2, return I = V/R
    """
    r2 = Voltage_Resistance(10e3)           # R = 10k

    print('BEFORE I = %s amph, %dk ohm' %(r2.current, r2.ohms/1e3))    # R=10K, V=0 ... I=0
    r2.voltage = 10
    r2.ohms = 30e3
    print('... r2.voltage = 10 v ...\n')
    print('AFTER.1 I = %s amph, %dk ohm' %(r2.current, r2.ohms/1e3))

    r2.voltage += 20
    r2.ohms += 30e3
    print('... r2.voltage += 5 v ...\n')
    print('AFTER.2 I = %s amph, %dk ohm' %(r2.current, r2.ohms/1e3))
# test2_current_decorate()


class Bounded_Resistance(Py_Registor):
    def __init__(self, ohms):
        """ V,I = 0, ohms = ohms : RESET ALL,  """
        super().__init__(ohms)

    # Define Built-in Decorator @property voltage() = _voltage (temp)
    @property
    def ohms(self):
        """ voltage() = _voltage  :temp """
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        """ If Value is improper, raise Error """
        if ohms <= 0:
            raise ValueError('%.4f ohms must be > 0' %ohms)
        self._ohms = ohms

def test2_if_exceptional_0_raise_ERR():
    r3 = Bounded_Resistance(10e3)
    # r4 = Bounded_Resistance(-5)     # ERROR.2 - wrong init
    r3.ohms = 0                     # ERROR.1 - wrong change
# test2_if_exceptional_0_raise_ERR()


class Fixed_Resistance(Py_Registor):
    def __init__(self, ohms):
        """ V,I = 0, ohms = ohms : RESET ALL,  """
        super().__init__(ohms)

    # Define Built-in Decorator @property voltage() = _voltage (temp)
    @property
    def ohms(self):
        """ voltage() = _voltage  :temp """
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        """ If Value is improper, raise Error """
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms

def test3_cant_change_ohms():
    r4 = Fixed_Resistance(10e3)
    r4.ohms = 2e3           # ERROR (ohms=function)
# test3_cant_change_ohms()



class Mysterious_Resistance(Py_Registor):
    def __init__(self, ohms):
        """ V,I = 0, ohms = ohms : RESET ALL,  """
        super().__init__(ohms)

    # Define Built-in Decorator @property voltage() = _voltage (temp)
    @property
    def ohms(self):
        """ voltage() = _voltage  :temp """
        self.voltage = self._ohms * self.current    # V = R.I
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        """ If Value is improper, raise Error """
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms

r7 = Mysterious_Resistance(10e3)
r7.current = 0.01

print('BEFORE: %5r' %r7.voltage)
r7.ohms

print('AFTER: %5r' %r7.voltage)
