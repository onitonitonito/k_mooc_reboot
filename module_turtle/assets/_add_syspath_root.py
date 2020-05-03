# ------ root path 를 sys.path.insert 시키는 코드 ... 최소 4줄 필요------
import os, sys                                                      # 1
top = "k_mooc_reboot"                                               # 2
root = "".join(os.path.dirname(__file__).partition(top)[:2])+"\\"   # 3
sys.path.insert(0, root)                                            # 4
# ---------------------------------------------------------------------





if __name__ == '__main__':
    print(root)
