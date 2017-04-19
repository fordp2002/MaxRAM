# SST39SF010 flash programmer
# by Phillip Pearson

# Copyright 2017 Google Inc
# Licensed under the GPL; see LICENSE.txt for details.


all: build wav

build:
	mkdir -p out
	ca65 --cpu 6502 -o out/program.o program.asm
	ld65 out/program.o -o out/program -C program.lkr
	da65 --comments 4 --start-addr 0x1100 out/program > out/program.list

wav:
	python file_to_wav.py out/program flash 1100
