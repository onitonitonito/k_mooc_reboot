# This is WITHOUT USING CLASS

NAME = ["Alan","Steve","Geremy","Kris","Liam","Aiden","Willam",]
POS = ["FW","FW","MF","MF","DF","GK","MF",]
NUM = [18,10,13,12,11,1,17,]

player_list = [[name, position, number] for name, position, number in zip(NAME,POS,NUM)]
# zipped and sent to list-data

order_id = ['onito', 'kaka', 'nitto', 'kay',]
order_name = ['Smith','Brian','Kevin','Aiden', ]
order_position = ['MF','MF','FW','DF',]
order_back_number = [18,15,10,4,]

player_dict = { uid:[name, position,back_number] for uid, name, position, back_number
    in zip(order_id, order_name, order_position, order_back_number) }
# zipped and sent to dict-data

def show_player_info(call_id):
    # call_id is Unique-Key
    # call_id = 'onito'                   # Unique-Key
    print()
    print ("uid=", call_id)                     #... Uid =  onito
    print ("NAME = ",player_dict[call_id][0])   #... NAME= Smith
    print ("POS = ",player_dict[call_id][1])    #... POS =  Midfielder
    print ("B.NUM = ",player_dict[call_id][2])  #... B.NUM =  18

print()
print("player_list=",player_list)
print("\n My name is %s \n My position is '%s' \n and My back number is %d"
    % (player_list[0][0],player_list[0][1],player_list[0][2]),)
# list-data can be called by form or array numbers

print()
print("player_dict=",player_dict)
print("\n My name is %s \n My position is '%s' \n and My back number is %d"
    % (player_dict['kaka'][0],player_dict['kaka'][1],player_dict['kaka'][2]),)
# dict-data can be called by Unique-Key (uid)
