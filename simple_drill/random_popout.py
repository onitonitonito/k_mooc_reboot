import random
end=10

def random_pop0(data):
    for x in range(len(data)):
        number = random.randint(0, len(data)-1)
        print(data.pop(number),"\t pop!")         # Show and Remove

def random_pop1(data):
    for x in range(len(data)):
        number = random.choice(data)    # number = random.randint(0, len(data)-1)
        data.remove(number)             # Just Remove, not show.
        print(number,"\t remove!")

def main0():
    data = [x for x in range(1,end+1)]
    print("data=",data)
    random_pop0(data)
    print("data=",data)
    print("\n")

def main1():
    data = [x for x in range(1,end+1)]
    print("data=",data)
    random_pop1(data)
    print("data=",data)
    print("\n")

main0()
#main1()

#import webbrowser
#webbrowser.open_new_tab('https://github.com/onito')
