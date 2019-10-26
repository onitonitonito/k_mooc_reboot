import re
import os
import sys
import subprocess


def extract_number(s):
    """숫자형식을 찾아 리스트로 반환"""
    return re.findall(r'\d+', s)

def extract_date(s):
    """날짜형식(dddd.dd.dd)을 찾아 첫번째 결과를 반환"""
    # return re.search(r'\d{4}.\d{2}.\d{2}', s).group()
    return re.findall(r'\d{4}.\d{2}.\d{2}', s)

def to_valid_filename(s):
    """특수문자는 '_'로 치환후 반환"""
    return re.sub(r'[^a-zA-Z0-9가-힣]', '_', s)

def update_size(s):
    """??"""
    sh = re.sub(r'height=\d{0,10}', 'height=10000', s)
    return re.sub(r'width=\d{0,10}', 'width=10000', sh)

def clean_text(s):
    """스페이스 공백 1개 이상은 지운다"""
    return re.sub(r'\s{2,}', '', s)

def dir_window_open(path):
    """해당Dir explorer를 연다(win32)"""
    try:
        if sys.platform == 'win32':
            os.startfile(path)
        elif sys.platform == 'darwin':
            subprocess.check_call(['open', '--', path])
        else:
            subprocess.check_call(['xdg-open', '--', path])
    except:
        pass



if __name__ == '__main__':
    import script_run
    results = [
        extract_number('1fd34tgw45e'),
        extract_date('dsds1921.11.424#@$343fdsfsdfa1924.07.13safd'),
        to_valid_filename('sfs@$@가나dfsd'),
        clean_text('ddd    f s  d af'),
        update_size("src='https' height='1,000' width='10,000'"),
        dir_window_open(os.path.dirname(__file__)),
        ]

    [print(r) for r in results]
