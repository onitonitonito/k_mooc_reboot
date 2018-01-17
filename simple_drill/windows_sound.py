""" -------------- Window beep sound :: Play DO-RE-MI Song :
  refer to : Gist.github - https://goo.gl/7BzDDy
  reference blog : http://freeprog.tistory.com/353
"""
import time
import math
import winsound

TEMPO = 1000    # playing speed = 1000
DICT_NOTE = {   # DICT_NOTE = do, re, mi, pa, sol, ra, ti --->  Hz
    'do':261, 're':293, 'mi':329, 'pa':349, 'sol':391, 'ra':440, 'ti':493,
    'DO':530, 'RE':590, }
A_NOTES = [
    [['do', 'mi', 'mi', 'mi', 'sol', 'sol', 're', 'pa', 'pa', 'ra', 'ti', 'ti'],
     [4, 4, 2, 4, 4, 2, 4, 4, 2, 4, 4, 2]],

    [['sol', 'do', 'ra', 'pa', 'mi', 'do', 're'],
     [1, 1, 1, 1, 1, 1, 0.5]],

    [['sol', 'do', 'ra', 'ti', 'DO', 'RE', 'DO']+['end'],
     [1, 1, 1, 1, 1, 1, 0.5]+[0]],
    ]
    # print(len(A_NOTES))         # n = 3
    # print(len(A_NOTES[0]))      # n = 2
    # print(len(A_NOTES[0][0]))   # n = 12

def show_a_score(a_notes):  # Score of note
    print('__'*40)
    print('PLAYING NOTES for DO-RE-MI')
    print('..'*40)
    for num in enumerate(a_notes):
        print(a_notes[num][0])        # ['do', 're', 'me', ...]
    print()
    print('__'*40)

def get_ziped_music(a_notes): # IN= 'list' / OUT= ZIP_OBJ
    note = []
    hrzs = []
    for num in enumerate(a_notes):   # n=3
        note += a_notes[num][0]
        hrzs += a_notes[num][1]
    return zip(note, hrzs)

def get_play_sound(zip_music):      #IN= ZIP_OBJECT
    for key, duration in list(zip_music):
        if key != 'end':
            winsound.Beep(DICT_NOTE[key], int(TEMPO/duration))
        else:
            pass
            # return False  # play once ...
    return True             # play repeatedly ...

def main_abc_song():
    show_a_score(A_NOTES)

    for i in range(2):
        zip_music = get_ziped_music(A_NOTES)
        get_play_sound(zip_music)
# main_abc_song()


# """ -------------- Window beep sound :: calculating Hz :
#   refer to : stack overflow .com = 440 Hz is A4.
#   reference blog : https://goo.gl/k89nFG
#    - FRENCH SONG: "au clair de la lune"!! 'r' is a rest
# """

LABELS = ['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']

# the PERIOD expressed in second, computed from a tempo in bpm
PERIOD = lambda tempo: 1/(tempo/60)
NAME = lambda n: LABELS[n%len(LABELS)] + str(int((n+(9+4*12))/12))
FREQUENCY = lambda n: int(440*(math.pow(2, 1/12)**n))
NOTES = {NAME(n): FREQUENCY(n) for n in range(-42, 60)}

# play each note in sequence through the PC speaker at the given tempo
def play(song, tempo):
    for note in song.lower().split():
        if note in NOTES.keys():
            winsound.Beep(NOTES[note], int(PERIOD(tempo)*1000))
        else:
            time.sleep(PERIOD(tempo))

def show_notes_hrz():
    column_count = 1
    for key, value in zip(NOTES.keys(), NOTES.values()):
        print('%3s:%6s' %(key, value), end="   ")
        column_count += 1

        if column_count == 6:
            print()
            column_count = 0


def main_au_clair():
    show_notes_hrz()

    for i in range(2):
        play(('c4 c4 c4 d4 e4 r d4 r c4 e4 d4 d4 c4 r r r '
              'c4 C4 c4 d4 e4 r d4 r c4 e4 d4 d4 c4 r r r '
              'd4 d4 d4 d4 a3 r a3 r d4 c4 B3 a3 g3 r r r '
              'c4 c4 c4 d4 e4 r d4 r c4 e4 d4 d4 c4 r r r '), 180)
        # tempo = 180 bpm...

if __name__ == '__main__':
    main_abc_song()    # play 2 times
    main_au_clair()    # play 2 times
