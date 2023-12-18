import sys
import os
import argparse

# ARGUMENT PARSING
try:
    ap = argparse.ArgumentParser()
    ap.add_argument("-type", "--type", type=str, required='True', help="Define the type of fifo")
    ap.add_argument("-n_words", "--n_words", type=str, required='True', help="Define the number of words for the fifo")
    ap.add_argument("-n_bits", "--n_bits", type=str, required='True', help="Define the number of bits for the fifo")
    ap.add_argument("-o", "--output", type=str, required='False', help="Output Folder")
    args = vars(ap.parse_args())
    fifo_type = args.get("type")
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
        with open(path+'fifo'+str(n_words)+'x'+str(n_bits)+'.sv', 'w+') as f:
            if fifo_type == 'std':
                mystr = 'module fifo'+str(n_words)+'x'+str(n_bits)+' #(parameter DEPTH = '+str(n_words)+', WIDTH = '+str(n_bits)+')(\n'
                mystr += '    input logic clk,\n'
                mystr += '    input logic rst_n,\n'
                mystr += '    input logic [WIDTH-1:0] data_in,\n'
                mystr += '    input logic write_en,\n'
                mystr += '    output logic [WIDTH-1:0] data_out,\n'
                mystr += '    input logic read_en,\n'
                mystr += '    output logic empty,\n'
                mystr += '    output logic full\n'
                mystr += ');\n'
                mystr += '\n'
                mystr += '    // Internal memory to store data\n'
                mystr += '    logic [WIDTH-1:0] mem [0:DEPTH-1];\n'
                mystr += '    logic [DEPTH-1:0] wr_ptr, rd_ptr; // Renamed pointers\n'
                mystr += '\n'
                mystr += '    // Signals for empty and full conditions\n'
                mystr += '    logic [DEPTH:0] count;\n'
                mystr += '\n'
                mystr += '    // Full and empty flags\n'
                mystr += '    assign full = (count == DEPTH);\n'
                mystr += '    assign empty = (count == 0);\n'
                mystr += '\n'
                mystr += '    // Write process\n'
                mystr += '    always_ff @(posedge clk or negedge rst_n) begin\n'
                mystr += '        if (~rst_n) begin\n'
                mystr += '            wr_ptr <= 0;\n'
                mystr += '            rd_ptr <= 0;\n'
                mystr += '        end else if (write_en && ~full) begin\n'
                mystr += '            mem[wr_ptr] <= data_in;\n'
                mystr += '            wr_ptr <= (wr_ptr == DEPTH-1) ? 0 : wr_ptr + 1;\n'
                mystr += '            count <= count + 1;\n'
                mystr += '        end\n'
                mystr += '    end\n'
                mystr += '\n'
                mystr += '    // Read process\n'
                mystr += '    always_ff @(posedge clk or negedge rst_n) begin\n'
                mystr += '        if (~rst_n) begin\n'
                mystr += '            wr_ptr <= 0;\n'
                mystr += '            rd_ptr <= 0;\n'
                mystr += '        end else if (read_en && ~empty) begin\n'
                mystr += '            data_out <= mem[rd_ptr];\n'
                mystr += '            rd_ptr <= (rd_ptr == DEPTH-1) ? 0 : rd_ptr + 1;\n'
                mystr += '            count <= count - 1;\n'
                mystr += '        end\n'
                mystr += '    end\n'
                mystr += '\n'
                mystr += 'endmodule\n'

            f.write(mystr)
    else:
        raise('\033[38;5;RAM should not have less then 8 bit\033[0;0m')
except Exception as err:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('\033[38;5;208mError during CORE CODE:\nError Type: '+str(exc_type)+'\nLine number: '+str(exc_traceback.tb_lineno)+'\033[0;0m')
    print(err)
    sys.exit()





