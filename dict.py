def printinput(name):
    print "hello {}".format(name) 

def squarecube(value):
    return (value*value, value*value*value)

def manyparms(first,*args,**kwargs):
    print "first = {}".format(first)

    print "*args = {}".format(args)
    for item in args:
        print "varargs = {}".format(item)

    print "*kwargs = {}".format(kwargs)
    for kwitem in kwargs.keys():
        print "kwkeys   = {}".format(kwitem)
    for kwitem in kwargs.values():
        print "kwvalues = {}".format(kwitem)

def main():

    printinput("john")

    initvalue = input("please input a number")
    square, cube = squarecube(initvalue)
    print initvalue
    print square
    print cube

    manyparms("arg1",2,3,4.4,kw1="John",kw2="William",kw3="Fenwick")

if __name__ == "__main__":
    main()
