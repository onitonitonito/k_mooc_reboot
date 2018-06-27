#! Python
""" Name card Class oop : super(). func Drill..
  (1) OOP class - 2 kinds of NAMECARD = (NORMAL & EXCLUSSIVE)
  (2) Inharitance and call parent's func --> super().
"""

class NameCard(object):
    """ Name card Class oop : super(). func Drill..
      (1) OOP class - 2 kinds of NAMECARD = (NORMAL & EXCLUSSIVE)
      (2) Inharitance and call parent's func --> super().
    """
    count_card = 0

    def __init__(self, name, phone_num, email):
        __class__.count_card += 1
        self.name = name
        self.phone_num = phone_num
        self.email = email
        self.kind = 'NORMAL'

    def show_header(self):
        """ common header """
        print('__'*20)
        print('\tNAME CARD : %s'% self.kind)
        print('``'*20)

    def show_info_body(self):
        """ information part """
        print('NAME   = %s'% self.name)
        print('PHONE  = %s'% self.phone_num)
        print('E-MAIL = %s'% self.email)

    def show_footer(self):
        """ common footer = Total Number of Card """
        print('__'*20)
        print('CURRENT CARDS : \tTOTAL %s cards'% __class__.count_card)

    def whole_card(self):
        """ header + body + footer """
        self.show_header()
        self.show_info_body()
        self.show_footer()
        print('\n\n')


class NameCardExclussive(NameCard):
    """ Noram + Additional Info = Exclussive NameCard()
      - Inherit from parent (Normal Namecard)
    """
    def __init__(self, name, phone_num, email, memo):
        super().__init__(name, phone_num, email)

        # ADD - changing or add part
        self.memo = memo
        self.kind = 'EXCLUSSIVE'

    def show_info_body(self):
        super().show_info_body()

        # ADD - changing or add part
        print('..'* 15)
        print('MEMO   = %s'% self.memo)


def declar_2_objects_example():
    """  for Example : Kim & Park NameCard objects were Declaired!
      - Kim = is set as NORMAL NameCard
      - Park = is set as EXCLUSSIVE NAMECARD, contains MEMO Option
    """
    kim = NameCard(name='KIM',
                   phone_num='010-1232-1222',
                   email='kimsl@a.com')

    park = NameCardExclussive(name='PARK',
                              phone_num='010-2888-4444',
                              email='parksl@a.com',
                              memo='Very Handsome')
    return kim, park


if __name__ == '__main__':
    KIM, PARK = declar_2_objects_example()
    LEE = NameCard(name='LEE',
                   phone_num='010-4444-5555',
                   email='leesl@a.com')

    KIM.whole_card()
    LEE.whole_card()
    PARK.whole_card()
