SHELL:=/bin/bash
# Flip Flops
FF_TYPE?='std'
# Registers
REG_TYPE?='with_en'
REG_NBIT?='8'
# Counter
CNT_TYPE?='with_synch_rstn'
CNT_PERIOD?='15'
CNT_FCLK?='8'
# Mux
MUX_N_INPUTS?='4'
MUX_N_BITS?='8'
#Decoder
DEC_N_INPUTS?='3'
# Adder
ADD_TYPE?='rca'
ADD_NBITS?='8'
# Subtractor
SUB_NBITS?='8'
# RAM
RAM_TYPE?='std'
RAM_NWORDS?='8'
RAM_NBITS?='8'
# Outputs
OUTPUT_FOLDER?='outputs'
SIM_FOLDER?='sim'

all: clean setup ff register counter mux decoder ha addsub ram compile
# SETUP
setup:
	mkdir -p $(SIM_FOLDER) $(OUTPUT_FOLDER)
# DESING
ha:
	python3 ./scripts/ha.py -o $(OUTPUT_FOLDER)
fa:
	python3 ./scripts/fa.py -o $(OUTPUT_FOLDER)
ff:
	python3 ./scripts/ff.py -type $(FF_TYPE) -o $(OUTPUT_FOLDER)
register:
	python3 ./scripts/register.py -type $(REG_TYPE) -nbit $(REG_NBIT) -o $(OUTPUT_FOLDER)
counter:
	python3 ./scripts/counter.py -type $(CNT_TYPE) -period $(CNT_PERIOD) -fclk $(CNT_FCLK) -o $(OUTPUT_FOLDER)
mux:
	python3 ./scripts/mux.py -n_inputs $(MUX_N_INPUTS) -n_bits $(MUX_N_BITS) -o $(OUTPUT_FOLDER)
decoder:
	python3 ./scripts/decoder.py -n_inputs $(DEC_N_INPUTS) -o $(OUTPUT_FOLDER)
adder: fa
	python3 ./scripts/adder.py -type $(ADD_TYPE) -n_bits $(ADD_NBITS) -o $(OUTPUT_FOLDER)
addsub: adder
	python3 ./scripts/addsub.py -n_bits $(SUB_NBITS) -o $(OUTPUT_FOLDER)
ram: 
	python3 ./scripts/ram.py -type $(RAM_TYPE) -n_words $(RAM_NWORDS) -n_bits $(RAM_NBITS) -o $(OUTPUT_FOLDER)

# COMPILE
compile:
	iverilog -g2012 $(OUTPUT_FOLDER)/*

# HELP
help_ff:
	python3 ./scripts/ff.py -h
help_register:
	python3 ./scripts/register.py -h
help_counter:
	python3 ./scripts/counter.py -h
help_mux:
	python3 ./scripts/mux.py -h
help_decoder:
	python3 ./scripts/decoder.py -h
help_fa:
	python3 ./scripts/fa.py -h
help_ha:
	python3 ./scripts/ha.py -h
help_adder:
	python3 ./scripts/adder.py -h
help_addsub:
	python3 ./scripts/addsub.py -h

# CLEAN
clean:
	rm -rf $(SIM_FOLDER) $(OUTPUT_FOLDER)
