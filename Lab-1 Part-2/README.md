## Files Present-

- Configuration Files: splitL1cache.py, unifiedL1cache.py
- Matrix Multiplication: mm.cpp, mm.1 (Input size is kept at 100)
- Code files for analysis and dumping simulation results: analysis.py, plots.ipynb

## To Run the Code Files-

```
$ gcc mm.cpp -o mm.1 -static -static-libgcc

$ gem5/build/X86/gem5.opt splitL1cache.py --l1i_size=[] --l1d_size=[] --assoc=[] --latency=[] --l2_size=[]

$ gem5/build/X86/gem5.opt unifiedL1cache.py --l2_size=[] --l1unified_size=[]

$ python3 analysis.py [clk-frequency] [cpu type] [latency] [assoc] [l1 size] [l2 size]

```

## Output Files-

- json files, where the simulation results are dumped, will be generated corresponding to the parameters fed into the configuration files.
- The .cpp code compilation will generate three files, corresponding to the two input matrices and the final product.