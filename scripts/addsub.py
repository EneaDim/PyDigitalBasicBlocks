import sys
import os
import argparse

# ARGUMENT PARSING
try:
    ap = argparse.ArgumentParser()
    ap.add_argument("-n_bits", "--n_bits", type=str, required='True', help="Define the number of bits for the adder")
    ap.add_argument("-o", "--output", type=str, required='False', help="Output Folder")
    args = vars(ap.parse_args())
    n_bits = int(args.get("n_bits"))
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
    if n_bits > 1:
        with open(path+'addsub'+str(n_bits)+'bits.sv', 'w+') as f:
            mystr = 'module addsub'+str(n_bits)+'bits (\n'
            mystr += '	input ['+str(n_bits-1)+':0] a,\n'
            mystr += '	input ['+str(n_bits-1)+':0] b,\n'
            mystr += '	input addn_sub,\n'
            mystr += '	output logic ['+str(n_bits-1)+':0] s,\n'
            mystr += '	output logic cout\n'
            mystr += ');\n'
            mystr += '\n'
            mystr += 'logic ['+str(n_bits-1)+':0] b_xor;\n\n'
            for i in range(n_bits):
                mystr += 'assign b_xor['+str(i)+'] = b['+str(i)+'] ^ addn_sub;\n'
            mystr += '\nadder'+str(n_bits)+'bits adder'+str(n_bits)+'bits_u (.a(a), .b(b), .cin(addn_sub), .s(s), .cout(cout));\n'
            mystr += '\nendmodule\n'
            f.write(mystr)
    else:
        raise('\033[38;5;208mSubtractor should have more then 1 bit\033[0;0m')
except Exception as err:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('\033[38;5;208mError during CORE CODE:\nError Type: '+str(exc_type)+'\nLine number: '+str(exc_traceback.tb_lineno)+'\033[0;0m')
    print(err)
    sys.exit()




