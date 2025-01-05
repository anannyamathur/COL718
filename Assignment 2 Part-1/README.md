## Files Present-

- Configuration Files: branch_pred.py
- Matrix Multiplication: mm.cpp, mm.1 (Input size is kept at 100)
- Code files for analysis and dumping simulation results: analysis.py, plots.ipynb

## To Run the Code Files-

```
$ gcc mm.cpp -o mm.1 -static -static-libgcc

$ gem5/build/X86/gem5.opt branch_pred.py --l1i_size=[] --l1d_size=[] --cpu_type=[] --bp_type=[] --l2_size=[]

$ python3 analysis.py [clk-frequency in GHz] [cpu type] [l1i size] [l1d size] [l2 size] [bp scheme]

```

## Output Files-

- json files, where the simulation results are dumped, will be generated corresponding to the parameters fed into the configuration files.
- The .cpp code compilation will generate three files, corresponding to the two input matrices and the final product.