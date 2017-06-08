# (1) Variable
def simVAR():
    a = 1
    print ("val=",a," \n")

    a=5
    print("val=",a, "\n")
# simVAR()

# (2) Array = List type Variable
def listVAR():
    a=[1,2,3,4,5]               # GLOABL Var. --> LOCAL
    for i in range(5):
        print ("a(%s)=%d" %(i,a[i]) )
def main():
    listVAR()
    a = 3
    print ("\n", a)
#main()

# (3) Tuple Var.
def tupleVAR():
    a=(1,[2,3,4,5],"Target",3.141592)   # Tuple (Not changable)
    for i in range(4):
        print (a[i])
def main():
    # a[0] = 3
    tupleVAR()
#main()

# (4) Dic Var.
def dicVAL():
    a={
        "Name":"DAVE the Asshole", "Age":45,\
        "Strength":10, "Inteligence":110,\
        "Pocket": {"knife",3, "Money",1000},\
        "Backpack" : {"water":3, "axe":2} } # defined with fair

    print("\tNAME: ",a["Name"],"\n\tBACKPACK: ", a["Backpack"])

def header():
    print("\n\t   --INVENTORY--")
    print("\n","-"*40)

def footer():
    print("-"*40)

def main():
    header()
    dicVAL()
    footer()

#main()


def dynamic_limited_calc(a,b):          # from codefighter
    if not(a >= -100 and a <=1000):
        a = False

    if not(b >= -100 and b <=1000):
        b = False

    if a and b:
        sum =  a + b
        print("%s + %s = "%(a,b),sum)
        return True
    else:
        print("*** ERROR: Out Of Range Error!")
        print ("a=%s, b=%s"%(a,b))

        return False
def main():
    a = dynamic_limited_calc(100,-1000)
    print(a)

main()
