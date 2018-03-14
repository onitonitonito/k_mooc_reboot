import os
import time

DIRS = os.path.dirname(__file__).partition("k_mooc_reboot\\")
ROOT = DIRS[0] + DIRS[1]
# print(ROOT); quit()       # 테스트용.

filename_with_dir = os.path.join(ROOT, '_static', '_log', "i_have_a_dream1.pdb")

try:
    for line in open(filename_with_dir, 'r').readlines():
        print(line, end='', flush=True)
        time.sleep(0.2)
except:
    print("Problem with %s" % filename_with_dir, flush=True)
