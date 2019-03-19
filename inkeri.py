'''
    This script was written in python 3.x.
    In order to run this script, please make sure your python version is 3.x or above.
    How to run:
        python inkeri.py
    or if it doesn't work use this one:
        python3 inkeri.py
    Author: Pedja <pedja.terzic@hotmail.com>
'''
print("                        ***** INKERI *****\n\n\n")
while True:
    n=int(input("Enter the exponent : "))
    if n < 2:
        print("Exponent must be greater than one")
    else:
        s=22
        F=2**2**n+1
        ctr=1
        while ctr<=2**n-2:
            s=(s**2-2)%F
            ctr=ctr+1
        if s==0:
            print("2^2^"+str(n)+"+1 is prime")
        else:
            print("2^2^"+str(n)+"+1 is composite")
    try_again = ""
    # Loop until users opts to go again or quit
    while not(try_again == "1") and not(try_again == "0"):
        try_again = input("Press 1 to try again, 0 to exit. ")
        if try_again in ["1", "0"]:
            continue  # a valid entry found
        else:
            print("Invalid input- Press 1 to try again, 0 to exit.") 
    # at this point, try_again must be "0" or "1"
    if try_again == "0":
        break 