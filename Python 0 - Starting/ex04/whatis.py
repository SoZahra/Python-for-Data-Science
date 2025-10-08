
import sys

if len(sys.argv) == 1:
    print("")
elif len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
else:
    try:
        nb = int(sys.argv[1])
        if nb % 2:
            print("I'm Odd.")
        else:
            print("I'm Even.")
    except:
        print("AssertionError: argument is not an integer")
