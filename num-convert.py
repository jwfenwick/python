"""
Converts an integer number to an ordinal-type name string
Example:  
    int(123456789) -> "123 million 456 thousand 789 units"

Input range:  
    signed 32-bit integers  0 .. 2^31 

Algorithm:
     convert positional blocks in the thousands/millions|billions range
        by using modulus operation by powers of 1000 at each step
     save the integer and fractional parts of modulus for next step

Extensions:
    easily extended to increase the positional range
        simply extend the range variables in the loop
        (optional) modify the code to make range values computed not static

Testing and Error Checking:
    apply to range limits 0 and 2^31 - 1
    apply to random values with this range 
    apply to out-of-range inputs
    apply to not-number inputs

Requirements:
    uses Python math module, modf function

Performance:
    O(n-1) performance, n = number of positonal blocks
    math library dependant (very fast)

"""

from math import modf

# strings   names of ranges to convert.  Ordered list, in increasing order
#           extend by adding static entries
# values    computer number for each positional location

strings=["units", "thousands,", "milions,", "billions,"]   # output strings

def main():

    while True :

        values=[]                                                  # values[index]
        # get a valid user input
        try:
            userinput = input("\nPlease input a number in range 1..2^31: ")

            number    = int(userinput)
            if   ( number < 1 )  or ( number > 2**31 - 1):
                print "number out of range, please try again"
            else:
                # modulus convert: value rewritten each loop, last value is billions
                for block in strings:
                    remainder,number = modf( number/1000.0 )
                    print remainder, number
                    values.append(int(remainder*1000))
            
                # want output in decreasing order so traverse list in reverse order
                print ("Here is your converted number: ")
                index = len(values) - 1
                for value in values:    
                    print int(values[index]),
                    print strings[index],
                    index -= 1
            
        except:
            print ("invalid number detected, please try again")

if __name__ == "__main__":
    main()

