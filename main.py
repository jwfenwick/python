def printinput(name):
    print "hello {}".format(name) 

def squarecube(value):
    return (value*value, value*value*value)

def main():

    printinput("john")

    initvalue = input("please input a number: ")
    square, cube = squarecube(initvalue)
    
    print initvalue
    print square
    print cube
    

if __name__ == "__main__":
    main()
