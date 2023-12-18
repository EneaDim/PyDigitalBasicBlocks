import sys
import os
import argparse
import math

# ARGUMENT PARSING
try:
    ap = argparse.ArgumentParser()
    ap.add_argument("-n_inputs", "--n_inputs", type=str, required='True', help="Define the number of inputs for the mux")
    ap.add_argument("-n_bits", "--n_bits", type=str, required='True', help="Define the number of bits for each input")
    ap.add_argument("-o", "--output", type=str, required='False', help="Output Folder")
    args = vars(ap.parse_args())
    n_inputs = int(args.get("n_inputs"))
    n_bits = int(args.get("n_bits"))
    output_folder = args.get("output")
except Exception as err:
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
    sel = math.ceil(math.log2(n_inputs))
    # Open the file
    with open(path+'mux'+str(n_inputs)+'to1.sv', 'w+') as f:
        mystr = 'module mux'+str(n_inputs)+'to1 (\n'
        mystr += '	input ['+str(sel-1)+':0] sel,\n'
        for i in range(n_inputs):
            sig_ascii = ord('a') + i
            if n_bits > 1:
                mystr += '	input ['+str(n_bits-1)+':0] '+str(chr(sig_ascii))+',\n'
            else:
                mystr += '	input '+str(chr(sig_ascii))+',\n'
        if n_bits > 1:
            mystr += '	output logic ['+str(n_bits-1)+':0] out\n'
        else:
            mystr += '	output logic out\n'
        mystr += ');\n'
        mystr += '\n'
        mystr += 'always_comb\n'
        mystr += '  case (sel)\n'
        for i in range(n_inputs):
            sig_ascii = ord('a') + i
            binary = bin(i)[2:].zfill(sel)
            mystr += "	    "+str(sel)+"'b"+str(binary)+": out = "+str(chr(sig_ascii))+";\n"
        mystr += '	    default: out = a;\n'
        mystr += '  endcase\n'
        mystr += 'endmodule\n'
        f.write(mystr)
except Exception as err:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('\033[38;5;208mError during CORE CODE:\nError Type: '+str(exc_type)+'\nLine number: '+str(exc_traceback.tb_lineno)+'\033[0;0m')
    print(err)
    sys.exit()

