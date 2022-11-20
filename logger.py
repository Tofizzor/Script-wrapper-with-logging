#!/usr/bin/python

import getopt, sys, logging, getpass



#print("Env thinks the user is " + os.getlogin())
#print("Effective user is " + getpass.getuser())

#Help message in case wrong input was added when running the script
def usage():
  print("Usage: logger.py -c <CommandName> -a <CommandArguments>")

def main():
    try:
        #Takes arguments inputed when running the script
        #Currently -h -a -s are only supported
        #Adding new argument e.g. -z would require to change "ha:s:"
        #to "ha:s:z:" in order to pick up new argument
        opts, args = getopt.getopt(sys.argv[1:], "ha:s:", ["argument=", "script="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    arguments = ""
    script = ""
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-a", "--argument"):
            arguments = "with arguments:" + a
        elif o in ("-s", "--script"):
            script = a
        else:
            assert False, "unhandled option"  
    FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
    logging.basicConfig(filename='commandHistory.txt', format=FORMAT)
    d = {'clientip': 'User: ' + getpass.getuser(), 'user': 'Script used: ' + script }
    logger = logging.getLogger(arguments)
    logger.warning('Command executed ' + arguments, extra=d)
    # ...

if __name__ == "__main__":
    main()
