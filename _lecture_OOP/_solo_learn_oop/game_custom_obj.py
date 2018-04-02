import os
import sys

# '루트'와 '작업'디렉토리 설정 - for 스크립트런
DIRS = os.path.dirname(__file__).partition("k_mooc_reboot")
ROOT = DIRS[0] + DIRS[1]
WORK_DIR = os.path.join(ROOT, "_static", "module_custom", "")
sys.path.append(WORK_DIR)
sys.path.append(ROOT)

# 위치가 달라서, Character() 카운팅이 되지 않음  ... ERROR
# from _static.module_custom.game_character import Character
# from _static.module_custom.game_player import Player, Warrior, Magician
# from _static.module_custom.game_monster import Monster, FireMonster, IceMonster

from game_character import Character
from game_player import Player, Warrior, Magician
from game_monster import Monster, FireMonster, IceMonster


def status_obj_creation():
    print("\n\n")
    print("총 오브젝트=", Character._total_count)
    print("=========================")
    print("플레이어  =", Player._total_count)
    print("--------------")
    print(" 전 투 병 =", Warrior._total_count)
    print(" 마 법 사 =", Magician._total_count, "\n")

    print("몬스터괴물 =", Monster._total_count)
    print("--------------")
    print("  불꽃괴물 =", FireMonster._total_count)
    print("  얼음괴물 =", IceMonster._total_count)





if __name__ == '__main__':
    a = Warrior()
    b = Magician()
    c = IceMonster()
    d = FireMonster()

    status_obj_creation()
