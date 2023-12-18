import sys
import os
import argparse

# ARGUMENT PARSING
try:
    ap = argparse.ArgumentParser()
    ap.add_argument("-type", "--type", type=str, required='True', help="Define the type of adder")
    ap.add_argument("-n_bits", "--n_bits", type=str, required='True', help="Define the number of bits for the adder")
    ap.add_argument("-o", "--output", type=str, required='False', help="Output Folder")
    args = vars(ap.parse_args())
    a_type = args.get("type")
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
    if not n_bits == 1:
        with open(path+'adder'+str(n_bits)+'bits.sv', 'w+') as f:
            if a_type == 'rca':
                mystr = 'module adder'+str(n_bits)+'bits (\n'
                mystr += '	input ['+str(n_bits-1)+':0] a,\n'
                mystr += '	input ['+str(n_bits-1)+':0] b,\n'
                mystr += '	input cin,\n'
                mystr += '	output logic ['+str(n_bits-1)+':0] s,\n'
                mystr += '	output logic cout\n'
                mystr += ');\n'
                mystr += '\n'
                mystr += 'logic ['+str(n_bits)+':1] carry;\n\n'
                mystr += "fa fa_0 (.a(a[0]), .b(b[0]), .cin(cin), .s(s[0]), .cout(carry[1]));\n"
                for i in range(1, n_bits-1):
                    mystr += 'fa fa_'+str(i)+' (.a(a['+str(i)+']), .b(b['+str(i)+']), .cin(carry['+str(i)+']), .s(s['+str(i)+']), .cout(carry['+str(i+1)+']));\n'
                mystr += 'fa fa_'+str(n_bits-1)+' (.a(a['+str(n_bits-1)+']), .b(b['+str(n_bits-1)+']), .cin(carry['+str(n_bits-1)+']), .s(s['+str(n_bits-1)+']), .cout(cout));\n'
                mystr += '\nendmodule\n'
            f.write(mystr)
    else:
        raise('\033[38;5;Adder should have more then 1 bit\033[0;0m')
except Exception as err:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('\033[38;5;208mError during CORE CODE:\nError Type: '+str(exc_type)+'\nLine number: '+str(exc_traceback.tb_lineno)+'\033[0;0m')
    print(err)
    sys.exit()



