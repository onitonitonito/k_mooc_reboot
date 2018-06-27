from package_i.soccer_data import SoccerPlayer


onito = SoccerPlayer('onito', 'Kay', 18, 'MF')  # Declaor OBJECT

onito.view_player_data('hoho')
print(onito)
onito.change_player_number('hoho',20)
onito.change_player_position('hoho','FW')
onito.view_player_data('hoho')

onito.view_player_dict()

onito.add_player('kkkk','Zen','MF',99)
