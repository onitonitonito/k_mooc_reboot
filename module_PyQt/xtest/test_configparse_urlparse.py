"""
# SPLIT into QUERY_DICT from WHOLE URL_TARGET
 - IN: URL W/ QUERY STRING
 - OUT: QUERY DICT
"""
print(__doc__)

import configparser
from urllib.parse import urlparse
from assets.config import dir_ini      # location of ini file

# to load the information from config_invisible.ini(*hidden)
config = configparser.ConfigParser()
config.read(dir_ini + 'config_invisible.ini')


# https://stackoverflow.com/questions/14340366/configparser-and-string-with
try:
    url_target = config.get('url_google', 'search_weather')
except:
    print("\n *** ERROR *** - NO INI FILES!")
    quit()


def get_query_dict(url_target):
    """ W/O urllib.parse"""
    if not "?" in url_target:
        print("*** NO QUERY STRING EXIST!***")
        quit()

    str_query = url_target.split("?")[-1]
    items_equal_array = [items_equal for items_equal in str_query.split('&')]

    query_dict = {}
    for items in [items_equal.split('=') for items_equal in items_equal_array]:
        query_dict[str(items[0])] = str(items[1])
    return query_dict



if __name__ == '__main__':
    # print(urlparse.__doc__)
    print("*** URL_TARGET from CONFIGPARSER ***")
    print(url_target, end="\n\n\n\n")

    titles = [      # Titile of 6-tuple components
        'scheme',
        'netloc',
        'path',
        'params',
        'query',
        'fragment',
    ]

    print("*** 6-COMPONETS OF URL-PARSE ***")
    _ = urlparse(url_target, scheme='netloc')
    [print(f"{titles[i]} : {item}") for i, item in enumerate(list(_))]
    print('\n\n\n')

    print("*** QUERY DICT ***")
    for key, val in get_query_dict(url_target).items():
        print(f"{key} : {val}")
