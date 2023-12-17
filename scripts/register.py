import sys
import os
import argparse

# ARGUMENT PARSING
try:
    ap = argparse.ArgumentParser()
    ap.add_argument("-type", "--type", type=str, required='True', help="Define the type of Register")
    ap.add_argument("-nbit", "--nbit", type=str, required='True', help="Define the number of bits for the register")
    ap.add_argument("-o", "--output", type=str, required='False', help="Output Folder")
    args = vars(ap.parse_args())
    reg_type = args.get("type")
    nbit = args.get("nbit")
    output_folder = args.get("output")
except Exception as err:
    print('\033[38;5;208mError during ARGUMENT PARSING:\n\033[0;0m')
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
    with open(path+'register.sv', 'w+') as f:
        if reg_type == 'std':
            mystr = 'module register #(\n'
            mystr += '	parameter NBIT = '+nbit+',\n'
            mystr += '	parameter UPPER = NBIT -1\n'
            mystr += ')(\n'
            mystr += '	input clk,\n'
            mystr += '	input rstn,\n'
            mystr += '	input  [UPPER:0] in,\n'
            mystr += '	output [UPPER:0] out\n'
            mystr += ');\n'
            mystr += '\n'
            mystr += 'logic [UPPER:0] out_w;\n'
            mystr += '\n'
            mystr += 'always_ff @(posedge clk or negedge rstn) begin\n'
            mystr += '	if (~rstn) begin\n'
            mystr += '		out_w <= 0;\n'
            mystr += '	else\n'
            mystr += '		out_w <= in;\n'
            mystr += 'end\n'
            mystr += '\n'
            mystr += 'assign out = out_s;\n'
            mystr += '\n'
            mystr += 'endmodule\n'
        elif reg_type =='with_en':
            mystr = 'module register #(\n'
            mystr += '	parameter NBIT = '+nbit+',\n'
            mystr += '	parameter UPPER = NBIT -1\n'
            mystr += ')(\n'
            mystr += '	input clk,\n'
            mystr += '	input rstn,\n'
            mystr += '	input enable,\n'
            mystr += '	input  [UPPER:0] in,\n'
            mystr += '	output [UPPER:0] out\n'
            mystr += ');\n'
            mystr += '\n'
            mystr += 'logic [UPPER:0] out_w;\n'
            mystr += '\n'
            mystr += 'always_ff @(posedge clk or negedge rstn) begin\n'
            mystr += '	if (~rstn) begin\n'
            mystr += '		out_w <= 0;\n'
            mystr += '	else\n'
            mystr += '		if (enable)\n'
            mystr += '			out_w <= in;\n'
            mystr += 'end\n'
            mystr += '\n'
            mystr += 'assign out = out_s;\n'
            mystr += '\n'
            mystr += 'endmodule\n'
        elif reg_type =='with_synch_rstn':
            mystr = 'module register #(\n'
            mystr += '	parameter NBIT = '+nbit+',\n'
            mystr += '	parameter UPPER = NBIT -1\n'
            mystr += ')(\n'
            mystr += '	input clk,\n'
            mystr += '	input rstn,\n'
            mystr += '	input rstns,\n'
            mystr += '	input  [UPPER:0] in,\n'
            mystr += '	output [UPPER:0] out\n'
            mystr += ');\n'
            mystr += '\n'
            mystr += 'logic [UPPER:0] out_w;\n'
            mystr += '\n'
            mystr += 'always_ff @(posedge clk or negedge rstn) begin\n'
            mystr += '	if (~rstn) begin\n'
            mystr += '		out_w <= 0;\n'
            mystr += '	else\n'
            mystr += '		if (~rstns)\n'
            mystr += "			out_w <= "+nbit+"'d0;\n"
            mystr += '		else\n'
            mystr += "			out_w <= in;\n"
            mystr += 'end\n'
            mystr += '\n'
            mystr += 'assign out = out_s;\n'
            mystr += '\n'
            mystr += 'endmodule\n'
        elif reg_type =='with_en_and_synch_rstn':
            mystr = 'module register #(\n'
            mystr += '	parameter NBIT = '+nbit+',\n'
            mystr += '	parameter UPPER = NBIT -1\n'
            mystr += ')(\n'
            mystr += '	input clk,\n'
            mystr += '	input rstn,\n'
            mystr += '	input enable,\n'
            mystr += '	input rstns,\n'
            mystr += '	input  [UPPER:0] in,\n'
            mystr += '	output [UPPER:0] out\n'
            mystr += ');\n'
            mystr += '\n'
            mystr += 'logic [UPPER:0] out_w;\n'
            mystr += '\n'
            mystr += 'always_ff @(posedge clk or negedge rstn) begin\n'
            mystr += '	if (~rstn) begin\n'
            mystr += '		out_w <= 0;\n'
            mystr += '	else\n'
            mystr += '		if (~rstns)\n'
            mystr += "			out_w <= "+nbit+"'d0;\n"
            mystr += '		else\n'
            mystr += '		    if (enable)\n'
            mystr += "			    out_w <= in;\n"
            mystr += 'end\n'
            mystr += '\n'
            mystr += 'assign out = out_s;\n'
            mystr += '\n'
            mystr += 'endmodule\n'
        else:
            raise Exception('\033[38;5;208mREGISTER type not allowed\033[0;0m')
        f.write(mystr)
except Exception as err:
    print('\033[38;5;208mError during CORE CODE:\n\033[0;0m')
    print(err)
    sys.exit()

