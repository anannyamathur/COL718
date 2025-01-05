#!/bin/bash

export PATH=$PATH:/opt/riscv/bin

source ~/.bashrc

/opt/riscv/bin/riscv64-unknown-elf-gcc comb_form.c -o m1.o

/opt/riscv/bin/riscv64-unknown-elf-objdump -D m1.o > comb_form.dump

gem5/build/RISCV/gem5.opt simple.py

python analysis.py Custom-Inst