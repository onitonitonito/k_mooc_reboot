#!/usr/bin/python3
import re
# print(re.__doc__)       # readme documentation

line = "Cats are smarter than dogs"

# ----------------------------------------------------------------------
def matchObjectShowGroup():
    matchObj = re.match( r'(.*) are (.*) (.*) (.*)', line, re.M|re.I)

    if matchObj:
       print ("matchObj.group(0) : ", matchObj.group(0))    # All sentence
       print ("matchObj.group(1) : ", matchObj.group(1))    # Cats
       print ("matchObj.group(2) : ", matchObj.group(2))    # smarter
       print ("matchObj.group(3) : ", matchObj.group(3))    # than
       print ("matchObj.group(4) : ", matchObj.group(4))    # dogs
    else:
       print ("No match!!")
# match_object_group()

# ----------------------------------------------------------------------
def matcjObjectByWord():
    matchObj = re.match( r'dogs', line, re.M|re.I)

    if matchObj:
       print("match --> matchObj.group(0) : ", matchObj.group(0))
    else:
       print("No match!!")

# ----------------------------------------------------------------------
def searchObjectByWord():
    searchObj = re.search( r'dogs', line, re.M|re.I)

    if searchObj:
       print("search --> searchObj.group() : ", searchObj.group())
    else:
       print("Nothing found!!")

# ----------------------------------------------------------------------
def main():
    # match_object_group()
    pass



if __name__ == '__main__':
    main()
