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
# Outputs
OUTPUT_FOLDER?='outputs'
SIM_FOLDER?='sim'

# SETUP
setup:
	mkdir -p $(SIM_FOLDER) $(OUTPUT_FOLDER)
# DESING
ff:
	python3 ./scripts/ff.py -type $(FF_TYPE) -o $(OUTPUT_FOLDER)
register:
	python3 ./scripts/register.py -type $(REG_TYPE) -nbit $(REG_NBIT) -o $(OUTPUT_FOLDER)
counter:
	python3 ./scripts/counter.py -type $(CNT_TYPE) -period $(CNT_PERIOD) -fclk $(CNT_FCLK) -o $(OUTPUT_FOLDER)

# HELP
help_ff:
	python3 ./scripts/ff.py -h
help_register:
	python3 ./scripts/register.py -h
help_counter:
	python3 ./scripts/counter.py -h

# CLEAN
clean:
	rm -rf outputs/*
