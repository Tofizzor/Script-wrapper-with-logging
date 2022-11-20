# Script-wrapper-with-logging
A menu that executes other scripts, this script also logs commands executed

Required scripts: main.py logger.py

To run this, simply execute main.py script:
python main.py

Logging function:

Log file: commandHistory.txt

logger.py is a separate script that handles logging of commands executed on main script. 
Main.py has a loggerFn function that got 2 inputs - script and arguments.
loggerFn function needs to be added to every command in order to log the activity.

Example: loggerFn("inputYourName.py", ans1 + ans2)

First option: Input name of the script as string

Second option: Add all the arguments that script requires
