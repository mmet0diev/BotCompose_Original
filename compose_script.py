#!/usr/bin/python3
import sys
import os
# A python script for composing an output text file with specific content in specific format.
# Write your code under this line:






# Write your code above this line:

user_path = os.path.expanduser("~username")

def WriteToFile(textToWrite):
    output_path = sys.argv[1]
    try:
        with open(output_path, 'w') as output:
            output.write(textToWrite)
    except Exception as e:
        print('Please provide a valid output file path.')
        print(e)


def check_args_num(args: list):
    if (len(args) == 2):
        # do sth
        return True
    else:
        print('Arguments have to be 2:\nScript name,\nresult file output path.\n')
        return False

def run_script():
    if check_args_num(sys.argv):
        pass
    else:
        print('Arguments have to be 2:\nScript name,\nresult file output path.\n')

run_script()