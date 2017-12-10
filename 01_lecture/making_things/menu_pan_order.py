#! python
import os
import sys
import datetime
""" file-docs : OPEN A RESTAURANT : Making Order System
  (1) to Show MENU_PAN = MENU_PAN (changeable)
  (2) to Input order = by Item index & quantity
  (3) to Calculate the Bills = Including (Tax= 6.5%, Tip= 10%)

 * Release Note : correct sorting version
    - Dict can not be ordered / arrange 'list' first.
    - Question : _arr.sort() = None. sorted(_arr) = 'list' O.K
    - I don't know the differences btw .sort() & sorted()
"""
SEPARATOR = '__'*22
MENU_DICT = {
    1 : ['BACK_NOODLE', 5500],
    2 : ['RED_NOODLE', 6500],
    3 : ['ROLLED_RICE', 3500],
    4 : ['TTUK-BOK-KI', 3500],
    5 : ['FRIED_DUMPLINGS', 3000],
    6 : ['SPRITE(7-UP)', 1000],
    7 : ['BOTTLED_WATER', 500],}
MENU_PAN_FORMAT = ""                                +\
    "-------------------------------------------\n" +\
    "     MENU-PAN  / Onito's Restautant        \n" +\
    "-------------------------------------------\n" +\
    "%s"                                            +\
    "-------------------------------------------\n"
BILL_FORMAT = ""                                    +\
    "-------------------------------------------\n" +\
    "     $$$ BILL / Onito's Restautant $$$     \n" +\
    "-------------------------------------------\n" +\
    "%s"                                            +\
    "-------------------------------------------\n"
RATE_TAX = float(6.5/100)
RATE_TIP = float(11/100)
ORDER_TIME = datetime.datetime.now()

def show_menu_pan():
    menu_string = ''

    for i, item_arr in enumerate(MENU_DICT.values()):
        menu_string += '{:2}. {:<16} {:.<10} {:5,} won'.format(
            i+1,
            item_arr[0],
            '.',
            item_arr[1]) +\
            '\n'
    print(MENU_PAN_FORMAT% menu_string)

def get_input_str():
    input_message = ''                                      +\
        'Please, order menu by index-quantity & space\n'    +\
        '(Ex: 1-2 2-1 3-2 .... just once for each index)\n'
    return input(input_message)

def get_order_dict_from(input_str):
    """ order_dict : order bill
      - input_str = '1-2 2-2 3-1...'
      - key = 'int' 1, 2, 3, 4 .. same as MENU_DICT
      - value = 'int' quantity
    """
    menu_arr = input_str.strip().split()        # ['1-2', '2-1', ..]

    order_dict = {}
    for menu in menu_arr:                       # menu = 'str', '1-2'
        _key = int(menu.split('-')[0])          # _key = int('1')
        _value = int(menu.split('-')[1])        # _val = int('2')
        order_dict[_key] = _value               # { 1:2, 2:1, ...}
    return order_dict

def get_oder_bill_calculation(order_dict):
    menu_total = 0
    order_bill_str = ''
    for index, _key in enumerate(order_dict.keys(), 1):
        menu_name = MENU_DICT[_key][0]
        menu_price = MENU_DICT[_key][1]
        quantity = order_dict[_key]

        order_bill_str += '{:2}. {:<16} {:6,} x {:2} = {:6,} won \n'.format(
            index,
            menu_name,
            menu_price,
            quantity,
            menu_price * quantity
            )
        menu_total += menu_price * quantity
    return menu_total, order_bill_str

show_menu_pan()

# menu_input_str = get_input_str()
menu_input_str = '1-2 2-1 3-1 4-4'
# print(menu_input_str)

order_dict = get_order_dict_from(menu_input_str)
# print(order_dict)

menu_total, order_bill_str = get_oder_bill_calculation(order_dict)
print(BILL_FORMAT % order_bill_str)
print('\tMENU PRICE  {:.^13} {:7,} won'.format('.', menu_total))
print('\tTax ({:4}%%){:.^13} {:7,} won'.format(
    RATE_TAX *100,
    '.',
    int(menu_total*RATE_TAX)))
print('\tTip ({:4}%%){:.^13} {:7,} won'.format(
    RATE_TIP *100,
    '.',
    int(menu_total*RATE_TIP)))
print(SEPARATOR)
total_price = int((menu_total * (1 + RATE_TAX)) * (1 + RATE_TIP))
print('\tTOTAL PRICE {:.^13} {:7,} won'.format('.', total_price))
print('\tPAY AMOUNTS {:.^13} {:7,} won'.format('.', int(total_price/100)*100))
print(SEPARATOR)
print('ORDER TIME: {:>33}'.format(ORDER_TIME.strftime('%p. %I:%M:%S - %b %d, %a')))
