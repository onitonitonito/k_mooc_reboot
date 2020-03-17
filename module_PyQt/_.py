"""
# split into query_dict from whole target url
"""
import configparser
from assets.config import dir_ini      # location of ini file


# to load the information from config_invisible.ini(*hidden)
config = configparser.ConfigParser()
config.read(dir_ini + 'config_invisible.ini')

try:
    url_target = config.get('url_query', 'daum_search')
except:
    # https://stackoverflow.com/questions/14340366/configparser-and-string-with
    print("\n *** ERROR *** - NO INI FILES!"); quit()


def get_query_dict(url_target):
    if not "?" in url_target:
        print("*** NO QUERY ***")
        quit()

    str_query = url_target.split("?")[-1]
    items_equal_array = [items_equal for items_equal in str_query.split('&')]

    query_dict = {}
    for items in [items_equal.split('=') for items_equal in items_equal_array]:
        query_dict[str(items[0])] = str(items[1])
    return query_dict



if __name__ == '__main__':
    for key, val in get_query_dict(url_target).items():
        print(f"{key} : {val}")
