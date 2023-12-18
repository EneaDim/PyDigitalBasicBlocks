import sys
import os
import argparse

# ARGUMENT PARSING
try:
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", type=str, required='False', help="Output Folder")
    args = vars(ap.parse_args())
    output_folder = args.get("output")
except Exception as err:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('\033[38;5;208mError during ARGUMENT PASSING:\nError Type: '+str(exc_type)+'\nLine number: '+str(exc_traceback.tb_lineno)+'\033[0;0m')
    print(err)
    sys.exit()

# CORE CODE
try:
    # Define the output folder
    if output_folder:
        path = './' + output_folder + '/'
    else:
        path = './'
    # Open the file
    with open(path+'fa.sv', 'w+') as f:
        mystr = 'module fa (\n'
        mystr += '	input a,\n'
        mystr += '	input b,\n'
        mystr += '	input cin,\n'
        mystr += '	output logic s,\n'
        mystr += '	output logic cout\n'
        mystr += ');\n'
        mystr += '\n'
        mystr += 'assign s = a ^ b ^ cin;\n'
        mystr += 'assign cout = (a & b) | (a & cin) | (b & cin);\n'
        mystr += '\nendmodule\n'
        f.write(mystr)
except Exception as err:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('\033[38;5;208mError during CORE CODE:\nError Type: '+str(exc_type)+'\nLine number: '+str(exc_traceback.tb_lineno)+'\033[0;0m')
    print(err)
    sys.exit()




