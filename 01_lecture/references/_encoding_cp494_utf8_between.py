""" Understanding UNICODE & encoding UTF-8
  - it only can work in 'Console' <f5>,
    not in script-run <shift+ctrl+B>
    for detail : published 2016.3/2 - understanding UNICODE
        https://www.slideshare.net/dahlmoon/string-20160310
        https://www.slideshare.net/JaehoonJung/ss-49316384?next_slideshow=2

    for Korean-'Hangul' : https://libsora.so/posts/python-hangul/

    also refer here: Unicode FileFormat.Info:
        http://www.fileformat.info/info/unicode/char/0180/index.htm
 """

import io
import sys
""" make stdout environment cp494 to utf-8 [WINDOWS-7]
  1.BEFORE: 안녕세계 = �ȳ缼��
    - sys.getdefaultencoding() = utf-8
    - sys.stdout.encoding = cp949        ---> change to 'utf-8'

  2.AFTER: 안녕세계 = 안녕세계
    - sys.getdefaultencoding() = utf-8
    - sys.stdout.encoding = 'utf-8'
 """
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import unicodedata
SEPARATOR = '__'*30 + '\n\n'

def test0_system_stdout_environment():
    """ Test this with / without stdout,err change above """
    string = u'안녕세계'
    print(string)
    print(sys.getdefaultencoding())
    print(sys.stdout.encoding)
test0_system_stdout_environment()

def test1_unicode_conversion():
    """ SHOW each of UNICODE range 1 ~ 4 bytes """
    print('\tDEFAULT SET = ', sys.getdefaultencoding())
    print(SEPARATOR)
    # U+0000 ~ U+007F

    print('CHR(0x32) = ', chr(0x32))
    s1 = u'\u0032'      # chr(0x32) = chr(50) = '2'
    ki = unicodedata.name(s1)
    print('ki = ', ki)
    print('1 bytes : \'%s\' <--> %s '% (s1, s1.encode(encoding='utf_8')), '\n\n')

    s2 = u'\u0180'   #b
    ki = unicodedata.name(s2)
    print('ki = ', ki)
    print('2 bytes : \'%s\' <--> %s '% (s2, s2.encode(encoding='utf_8')), '\n\n')

    s3 = u'\uac10'   #감
    ki = unicodedata.name(s3)
    print('ki = ', ki)
    print('3 bytes : \'%s\' <--> %s '% (s3, s3.encode(encoding='utf_8')), '\n\n')

    s4 = u'\U00011100' # '𑄀'
    # s4 = u'\u5940'
    ki = unicodedata.name(s4)
    print('ki = ', ki)
    print('4 bytes : \'%s\' <--> %s '% (s4, s4.encode(encoding='utf_8')), '\n\n')
test1_unicode_conversion()

def test1_encode_decode_repeatation():
    """ ENCODE <--> DECODE
    SHOW Relationship BTW. str (on certain Env.) <--> CODE(bytes)
     (1) string in certain Env. (encode)--> bytes=CODE
     (2) Bytes(CODE) (decode)--> string
    """
    string='乚卜己卜口卜己从卜口丨匸丌口勹丌勹口丬丨匸卜己卜'
    str_arr = []
    for letter in string:
        str_arr.append(letter.encode('utf-8'))

    bytes0 = b'\xe5\xa5\x80\xe5\x88\x80\xe5\x8d\x9c\xe5\xb7\xb1\xe5\x8d\x9c \xe4\
\xba\xba\xe4\xb8\xa8\xe5\xbb\xbf\xe5\x8d\x9c\xe5\xb7\xb1\xe5\x8d\x9c\xe5\x8f\
\xa3\xe5\x8d\x9c'

    bytes1 = b'\xe4\xb9\x9a\xe5\x8d\x9c\xe5\xb7\xb1\xe5\x8d\x9c\xe5\x8f\xa3\
\xe5\x8d\x9c\xe5\xb7\xb1\xe4\xbb\x8e\xe5\x8d\x9c\xe5\x8f\xa3\xe4\xb8\xa8\
\xe5\x8c\xb8\xe4\xb8\x8c\xe5\x8f\xa3\xe5\x8b\xb9\xe4\xb8\x8c\xe5\x8b\xb9\
\xe5\x8f\xa3\xe4\xb8\xac\xe4\xb8\xa8\xe5\x8c\xb8\xe5\x8d\x9c\xe5\xb7\xb1\
\xe5\x8d\x9c'

    print(string)
    print(bytes0.decode('utf-8'))
    print(bytes1.decode('utf-8'))
test1_encode_decode_repeatation()

print('찦차를 타고온 팹시맨과 쑛다리 똠방각하')
