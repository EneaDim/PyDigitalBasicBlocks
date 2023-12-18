import sys
import os
import argparse
import math

# ARGUMENT PARSING
try:
    ap = argparse.ArgumentParser()
    ap.add_argument("-type", "--type", type=str, required='True', help="Define the counter type")
    ap.add_argument("-period", "--period", type=str, required='True', help="Define the period in [us] for the counter to count")
    ap.add_argument("-fclk", "--fclk", type=str, required='True', help="Define the frequency in [MHz] at which the counter will run")
    ap.add_argument("-o", "--output", type=str, required='False', help="Output Folder")
    args = vars(ap.parse_args())
    cnt_type = args.get("type")
    period = args.get("period")
    fclk = args.get("fclk")
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
    # Calculate number of counts and nbits
    count = math.floor(float(period)*float(fclk)) - 1
    nbit = math.ceil(math.log2(count))
    # Open the file
    with open(path+'counter'+period+'us.sv', 'w+') as f:
        if cnt_type == 'std':
            mystr = 'module counter'+period+'us (\n'
            mystr += '	input clk,\n'
            mystr += '	input rstn,\n'
            mystr += '	input enable,\n'
            mystr += '	output ['+str(nbit-1)+':0] value,\n'
            mystr += '	output tc\n'
            mystr += ');\n'
            mystr += '\n'
            mystr += 'logic ['+str(nbit-1)+':0] count;\n'
            mystr += 'logic ['+str(nbit-1)+':0] count_nxt;\n'
            mystr += 'logic tc_s;\n'
            mystr += '\n'
            mystr += '// SEQUENTIAL PROCESS\n'
            mystr += 'always_ff @(posedge clk or negedge rstn) begin\n'
            mystr += '	if (~rstn)\n'
            mystr += '		count <= 0;\n'
            mystr += '	else\n'
            mystr += '		count <= count_nxt;\n'
            mystr += 'end\n'
            mystr += '\n'
            mystr += '// COMBO PROCESS\n'
            mystr += 'always_comb begin\n'
            mystr += '	count_nxt = count;\n'
            mystr += '	if (enable & ~tc_s)\n'
            mystr += '		count_nxt = count + 1;\n'
            mystr += '	else\n'
            mystr += '	    if (tc_s)\n'
            mystr += '		    count_nxt = 0;\n'
            mystr += 'end\n'
            mystr += '\n'
            mystr += '// TERMINAL COUNT DEFINITION\n'
            mystr += 'always_comb begin\n'
            mystr += "	if (count == "+str(nbit)+"'d"+str(count)+")\n"
            mystr += '		count_nxt = count + 1;\n'
            mystr += '	else\n'
            mystr += '		count_nxt = 0;\n'
            mystr += 'end\n'
            mystr += '\n'
            mystr += '// OUTPUT ASSIGNMENT\n'
            mystr += 'assign value = count;\n'
            mystr += 'assign tc = tc_s;\n'
            mystr += '\n'
            mystr += 'endmodule\n'
        elif cnt_type == 'with_synch_rstn':
            mystr = 'module counter_'+period+'us (\n'
            mystr += '	input clk,\n'
            mystr += '	input rstn,\n'
            mystr += '	input rstns,\n'
            mystr += '	output ['+str(nbit-1)+':0] value,\n'
            mystr += '	output tc\n'
            mystr += ');\n'
            mystr += '\n'
            mystr += 'logic ['+str(nbit-1)+':0] count;\n'
            mystr += 'logic ['+str(nbit-1)+':0] count_nxt;\n'
            mystr += 'logic tc_s;\n'
            mystr += '\n'
            mystr += '// SEQUENTIAL PROCESS\n'
            mystr += 'always_ff @(posedge clk or negedge rstn) begin\n'
            mystr += '	if (~rstn)\n'
            mystr += '		count <= 0;\n'
            mystr += '	else\n'
            mystr += '		count <= count_nxt;\n'
            mystr += 'end\n'
            mystr += '\n'
            mystr += '// COMBO PROCESS\n'
            mystr += 'always_comb begin\n'
            mystr += '	count_nxt = count;\n'
            mystr += '	if (rstns & ~tc_s)\n'
            mystr += '		count_nxt = count + 1;\n'
            mystr += '	else\n'
            mystr += '		count_nxt = 0;\n'
            mystr += 'end\n'
            mystr += '\n'
            mystr += '// TERMINAL COUNT DEFINITION\n'
            mystr += 'always_comb begin\n'
            mystr += "	if (count == "+str(nbit)+"'d"+str(count)+")\n"
            mystr += '		count_nxt = count + 1;\n'
            mystr += '	else\n'
            mystr += '		count_nxt = 0;\n'
            mystr += 'end\n'
            mystr += '\n'
            mystr += '// OUTPUT ASSIGNMENT\n'
            mystr += 'assign value = count;\n'
            mystr += 'assign tc = tc_s;\n'
            mystr += '\n'
            mystr += 'endmodule\n'
        elif cnt_type == 'with_en_and_synch_reset':
            mystr = 'module counter_'+period+'us (\n'
            mystr += '	input clk,\n'
            mystr += '	input rstn,\n'
            mystr += '	input rstns,\n'
            mystr += '	input enable,\n'
            mystr += '	output ['+str(nbit-1)+':0] value,\n'
            mystr += '	output tc\n'
            mystr += ');\n'
            mystr += '\n'
            mystr += 'logic ['+str(nbit-1)+':0] count;\n'
            mystr += 'logic ['+str(nbit-1)+':0] count_nxt;\n'
            mystr += 'logic tc_s;\n'
            mystr += '\n'
            mystr += '// SEQUENTIAL PROCESS\n'
            mystr += 'always_ff @(posedge clk or negedge rstn) begin\n'
            mystr += '	if (~rstn)\n'
            mystr += '		count <= 0;\n'
            mystr += '	else\n'
            mystr += '		count <= count_nxt;\n'
            mystr += 'end\n'
            mystr += '\n'
            mystr += '// COMBO PROCESS\n'
            mystr += 'always_comb begin\n'
            mystr += '	count_nxt = count;\n'
            mystr += '	if (rstns & ~tc_s)\n'
            mystr += '	    if (enable)\n'
            mystr += '	        count_nxt = count + 1;\n'
            mystr += '	else\n'
            mystr += '	    count_nxt = 0;\n'
            mystr += 'end\n'
            mystr += '\n'
            mystr += '// TERMINAL COUNT DEFINITION\n'
            mystr += 'always_comb begin\n'
            mystr += "	if (count == "+str(nbit)+"'d"+str(count)+")\n"
            mystr += '		count_nxt = count + 1;\n'
            mystr += '	else\n'
            mystr += '		count_nxt = 0;\n'
            mystr += 'end\n'
            mystr += '\n'
            mystr += '// OUTPUT ASSIGNMENT\n'
            mystr += 'assign value = count;\n'
            mystr += 'assign tc = tc_s;\n'
            mystr += '\n'
            mystr += 'endmodule\n'
        else:
            raise Exception('\033[38;5;208mCOUNTER type not allowed\033[0;0m')
        f.write(mystr)
except Exception as err:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('\033[38;5;208mError during CORE CODE:\nError Type: '+str(exc_type)+'\nLine number: '+str(exc_traceback.tb_lineno)+'\033[0;0m')
    print(err)
    sys.exit()


