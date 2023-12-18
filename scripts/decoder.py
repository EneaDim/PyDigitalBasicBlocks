import sys
import os
import argparse
import math

# ARGUMENT PARSING
try:
    ap = argparse.ArgumentParser()
    ap.add_argument("-n_inputs", "--n_inputs", type=str, required='True', help="Define the number of inputs for the decoder")
    ap.add_argument("-o", "--output", type=str, required='False', help="Output Folder")
    args = vars(ap.parse_args())
    n_inputs = int(args.get("n_inputs"))
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
    outs = pow(2, n_inputs)
    # Open the file
    with open(path+'decoder'+str(n_inputs)+'to'+str(outs)+'.sv', 'w+') as f:
        mystr = 'module decoder'+str(n_inputs)+'to'+str(outs)+' (\n'
        if n_inputs > 1:
            mystr += '	input ['+str(n_inputs-1)+':0] sel,\n'
        else:
            mystr += '	input sel,\n'
        mystr += '	output logic ['+str(outs-1)+':0] out\n'
        mystr += ');\n'
        mystr += '\n'
        mystr += 'always_comb\n'
        mystr += '  case (sel)\n'
        for i in range(outs):
            binary_sel = bin(i)[2:].zfill(n_inputs)
            binary_out = bin(pow(2, i))[2:].zfill(outs)
            mystr += "	    "+str(n_inputs)+"'b"+str(binary_sel)+": out = "+str(outs)+"'b"+str(binary_out)+";\n"
        mystr += "	    default: out = "+str(outs)+"'b"+str(bin(0)[2:].zfill(outs))+";\n"
        mystr += '  endcase\n'
        mystr += 'endmodule\n'
        f.write(mystr)
except Exception as err:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('\033[38;5;208mError during CORE CODE:\nError Type: '+str(exc_type)+'\nLine number: '+str(exc_traceback.tb_lineno)+'\033[0;0m')
    print(err)
    sys.exit()


