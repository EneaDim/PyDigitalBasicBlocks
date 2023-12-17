import sys
import os
import argparse

# ARGUMENT PARSING
try:
    ap = argparse.ArgumentParser()
    ap.add_argument("-type", "--type", type=str, required='True', help="Define the type of Flip Flop")
    ap.add_argument("-o", "--output", type=str, required='False', help="Output Folder")
    args = vars(ap.parse_args())
    ff_type = args.get("type")
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
    with open(path+'ff.sv', 'w+') as f:
        if ff_type == 'std':
            mystr = 'module ff (\n'
            mystr += '	input clk,\n'
            mystr += '	input rstn,\n'
            mystr += '	input d,\n'
            mystr += '	output logic q\n'
            mystr += ');\n'
            mystr += '\n'
            mystr += 'always_ff @(posedge clk or negedge rstn)\n'
            mystr += '	if (~rstn)\n'
            mystr += '		q <= 0;\n'
            mystr += '	else\n'
            mystr += '		q <= d;\n'
            mystr += 'endmodule\n'
        elif type=='rstn1':
            mystr = 'module ff_n (\n'
            mystr += '	input clk,\n'
            mystr += '	input rstn,\n'
            mystr += '	input d,\n'
            mystr += '	output logic q\n'
            mystr += ');\n'
            mystr += '\n'
            mystr += 'always_ff @(posedge clk or negedge rstn)\n'
            mystr += '	if (~rstn)\n'
            mystr += '		q <= 1;\n'
            mystr += '	else\n'
            mystr += '		q <= d;\n'
            mystr += 'endmodule\n'
        elif type=='with_en':
            mystr = 'module ff_e (\n'
            mystr += '	input clk,\n'
            mystr += '	input rstn,\n'
            mystr += '	input e,\n'
            mystr += '	input d,\n'
            mystr += '	output logic q\n'
            mystr += ');\n'
            mystr += '\n'
            mystr += 'always_ff @(posedge clk or negedge rstn)\n'
            mystr += '	if (~rstn)\n'
            mystr += '		q <= 0;\n'
            mystr += '	else\n'
            mystr += '	    if (e)\n'
            mystr += '		    q <= d;\n'
            mystr += 'endmodule\n'
        elif type=='with_synch_rstn':
            mystr = 'module ff_rstns (\n'
            mystr += '	input clk,\n'
            mystr += '	input rstn,\n'
            mystr += '	input rstns,\n'
            mystr += '	input d,\n'
            mystr += '	output logic q\n'
            mystr += ');\n'
            mystr += '\n'
            mystr += 'always_ff @(posedge clk or negedge rstn)\n'
            mystr += '	if (~rstn)\n'
            mystr += '		q <= 0;\n'
            mystr += '	else\n'
            mystr += '	    if (~rstns)\n'
            mystr += '		    q <= 0;\n'
            mystr += '	    else\n'
            mystr += '		    q <= d;\n'
            mystr += 'endmodule\n'
        elif type=='with_en_and_synch_rstn':
            mystr = 'module ff_rstns (\n'
            mystr += '	input clk,\n'
            mystr += '	input rstn,\n'
            mystr += '	input e,\n'
            mystr += '	input rstns,\n'
            mystr += '	input d,\n'
            mystr += '	output logic q\n'
            mystr += ');\n'
            mystr += '\n'
            mystr += 'always_ff @(posedge clk or negedge rstn)\n'
            mystr += '	if (~rstn)\n'
            mystr += '		q <= 0;\n'
            mystr += '	else\n'
            mystr += '	    if (~rstns)\n'
            mystr += '		    q <= 0;\n'
            mystr += '	    else\n'
            mystr += '	        if (e)\n'
            mystr += '		        q <= d;\n'
            mystr += 'endmodule\n'
        elif type=='sr':
            mystr = 'module sr_ff (\n'
            mystr += '	input clk,\n'
            mystr += '	input set,\n'
            mystr += '	input reset,\n'
            mystr += '	output logic q\n'
            mystr += ');\n'
            mystr += '\n'
            mystr += 'always_ff @(posedge clk or negedge rstn)\n'
            mystr += '	if (~rstn)\n'
            mystr += '		q <= 0;\n'
            mystr += '	else\n'
            mystr += '	    if (set)\n'
            mystr += '	        if (reset)\n'
            mystr += '		        q <= 0;\n'
            mystr += '	        else\n'
            mystr += '		        q <= set;\n'
            mystr += '	    else\n'
            mystr += '	        if (reset)\n'
            mystr += '		        q <= 0;\n'
            mystr += 'endmodule\n'
        elif type=='t':
            mystr = 'module t_ff (\n'
            mystr += '	input clk,\n'
            mystr += '	input rstn,\n'
            mystr += '	input d,\n'
            mystr += '	output logic q\n'
            mystr += ');\n'
            mystr += '\n'
            mystr += 'always_ff @(posedge clk or negedge rstn)\n'
            mystr += '	if (~rstn)\n'
            mystr += '		q <= 0;\n'
            mystr += '	else\n'
            mystr += '		q <= d ^ q;\n'
            mystr += 'endmodule\n'
        else:
            raise Exception('\033[38;5;208mFF type not allowed\033[0;0m')
        f.write(mystr)
except Exception as err:
    print('\033[38;5;208mError during CORE CODE:\n\033[0;0m')
    print(err)
    sys.exit()

