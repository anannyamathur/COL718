## Files Present-

- Configuration Files: simple.py, hello-world.py
- Matrix Multiplication: mm.cpp, mm.1 (Input size is kept at 100)
- Code files for analysis and dumping simulation results: analysis.py, plots.ipynb

## To Run the Code Files-

```
$ gcc mm.cpp -o mm.1 -static -static-libgcc

$ gem5/build/X86/gem5.opt simple.py --cmd=mm.1 --cpu-type=AtomicSimpleCPU --mem-type=DDR4_1600_8x8

$ gem5/build/X86/gem5.opt simple.py --cmd=mm.1 --cpu-type=TimingSimpleCPU --l1d_size=64kB --l1i_size=16kB --caches

$ gem5/build/X86/gem5.opt hello-world.py [clk-frequency]

$ python3 analysis.py [clk-frequency] [configuration]

```

## Output Files-

- json files, where the simulation results are dumped, will be generated corresponding to the parameters fed into the configuration files.
- The .cpp code compilation will generate three files, corresponding to the two input matrices and the final product.