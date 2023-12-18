import sys
import os
import argparse

# ARGUMENT PARSING
try:
    ap = argparse.ArgumentParser()
    ap.add_argument("-type", "--type", type=str, required='True', help="Define the type of ram")
    ap.add_argument("-n_words", "--n_words", type=str, required='True', help="Define the number of words for the ram")
    ap.add_argument("-n_bits", "--n_bits", type=str, required='True', help="Define the number of bits for the ram")
    ap.add_argument("-o", "--output", type=str, required='False', help="Output Folder")
    args = vars(ap.parse_args())
    ram_type = args.get("type")
    n_words = int(args.get("n_words"))
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
    if not n_bits < 8:
        with open(path+'ram'+str(n_words)+'x'+str(n_bits)+'.sv', 'w+') as f:
            if ram_type == 'std':
                mystr = 'module ram'+str(n_words)+'x'+str(n_bits)+' #(parameter WORDS = '+str(n_words)+', WIDTH = '+str(n_bits)+')(\n'
                mystr += '  input logic clk,\n'
                mystr += '  input logic rstn,\n'
                mystr += '  input logic csn,\n'
                mystr += '  input logic wen,\n'
                mystr += '  input logic [$clog2(WORDS)-1:0] add,\n'
                mystr += '  input logic [WIDTH-1:0] din,\n'
                mystr += '  output logic [WIDTH-1:0] dout\n'
                mystr += ');\n'
                mystr += '// Define memory array\n'
                mystr += 'logic [WIDTH-1:0] mem [0:WORDS-1];\n'
                mystr += '\n'
                mystr += '// Write operation\n'
                mystr += 'always_ff @(posedge clk or negedge rstn) begin\n'
                mystr += '  if (~rstn)\n'
                mystr += '    for (int i=0; i<WORDS; i++)\n'
                mystr += "      mem[i] <= '0;\n"
                mystr += '  else\n'
                mystr += '    if (~csn)\n'
                mystr += '      if (~wen)\n'
                mystr += '        mem[add] <= din;\n'
                mystr += 'end\n'
                mystr += '\n'
                mystr += '// Read operation\n'
                mystr += 'assign dout = mem[add];\n'
                mystr += '\nendmodule\n'
            f.write(mystr)
    else:
        raise('\033[38;5;RAM should not have less then 8 bit\033[0;0m')
except Exception as err:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('\033[38;5;208mError during CORE CODE:\nError Type: '+str(exc_type)+'\nLine number: '+str(exc_traceback.tb_lineno)+'\033[0;0m')
    print(err)
    sys.exit()




