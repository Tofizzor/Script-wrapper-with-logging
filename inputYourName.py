#!/usr/bin/python

import sys, getopt

#Example script with two arguments available -f -l

def main(argv):
    inputfile = ''
    outputfile = ''
    inputexist = False
    outputexist = False
    print("\n Script where you input your name")
    try:
        opts, args = getopt.getopt(argv,"hf:l:",["fname=","lname="])
    except getopt.GetoptError:
        print('inputYourName.py -f <FirstName> -l <LastName>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('inputYourName.py -f <FirstName> -l <LastName>')
            sys.exit()
        elif opt in ("-f", "--fname"):
            inputexist = True
            inputfile = arg
        elif opt in ("-l", "--lname"):
            outputexist = True
            outputfile = arg
    if inputexist:
        print('First name is: ', inputfile)
    if outputexist:
        print('Last name is: ', outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])