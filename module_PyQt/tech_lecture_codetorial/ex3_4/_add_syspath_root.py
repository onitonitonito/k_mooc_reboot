# ------ root path 를 sys.path.insert 시키는 코드 ... 최소 4줄 필요------
import os, sys                                                      # 1
top = "k_mooc_reboot"                                               # 2
root = "".join(os.path.dirname(__file__).partition(top)[:2])+"\\"   # 3
sys.path.insert(0, root + "module_PyQt")                            # 4 (o)
# ---------------------------------------------------------------------
# sys.path.insert(0, root)     # ROOT 기준 대신 프로젝트 ROOT(HOME)를 등록
