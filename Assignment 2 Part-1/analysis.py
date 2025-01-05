import json
import re
import sys

d=dict()
clk=str(sys.argv[1])+"GHz"

cpu=str(sys.argv[2])

l1i=str(sys.argv[3])

l1d=str(sys.argv[4])

l2=str(sys.argv[5])

bp=str(sys.argv[6])

with open('m5out/stats.txt','r') as f:
    lines=f.readlines()
    
    for line in lines:
        if line:
            
            d["clk_freq"]=float(sys.argv[1])

            d["l1i"]=l1i

            d["l1d"]=l1d

            d["l2"]=l2

            d["bp"]=bp
            
            if "simSeconds" in line:
                x=re.findall(r"[-+]?(?:\d*\.*\d+)",line)
                val=float(x[0])
                d["simSeconds"]=val
            
            elif "simInsts" in line:
                x=re.findall(r"[-+]?(?:\d*\.*\d+)",line)
                val=float(x[0])
                d["simInsts"]=val

            elif "board.processor.cores.core.numCycles" in line:
                x=re.findall(r"[-+]?(?:\d*\.*\d+)",line)
                val=float(x[0])
                d["board.processor.cores.core.numCycles"]=val
            
            elif "board.processor.cores.core.ipc" in line:
                x=re.findall(r"[-+]?(?:\d*\.*\d+)",line)
                val=float(x[0])
                d["board.processor.cores.core.ipc"]=val
            
            elif "board.processor.cores.core.cpi" in line:
                x=re.findall(r"[-+]?(?:\d*\.*\d+)",line)
                val=float(x[0])
                d["board.processor.cores.core.cpi"]=val

            elif "system.cpu.cpi" in line:
                x=re.findall(r"[-+]?(?:\d*\.*\d+)",line)
                val=float(x[0])
                d["board.processor.cores.core.cpi"]=val

            elif "hostInstRate" in line:
                x=re.findall(r"[-+]?(?:\d*\.*\d+)",line)
                val=float(x[0])
                d["hostInstRate "]=val

            elif "system.cache.hitRatio" in line:
                x=re.findall(r"[-+]?(?:\d*\.*\d+)",line)
                val=float(x[0])
                d["hitRatio"]=val

            elif "system.cpu.iew.predictedTakenIncorrect" in line:
            
             # Number of branches that were predicted taken incorrectly (Count)

                x=re.findall(r"[-+]?(?:\d*\.*\d+)",line)
                val=float(x[0])
                d["predictedTakenIncorrect"]=val
            
            elif "system.cpu.iew.branchMispredicts" in line: 
           
            # Number of branch mispredicts detected at execute (Count)

                x=re.findall(r"[-+]?(?:\d*\.*\d+)",line)
                val=float(x[0])
                d["branchMispredicts"]=val

            elif "system.cpu.branchPred.BTBHitRatio" in line: 
           
            # Number of branch mispredicts detected at execute (Count)

                x=re.findall(r"[-+]?(?:\d*\.*\d+)",line)
                val=float(x[0])
                d["BTBHitRatio"]=val

out_file = open(f"{clk}+{cpu}+{l1i}+{l1d}+{l2}+{bp}.json", "w")
  
json.dump(d, out_file)
  
out_file.close()

print(f"Results dumped at json file-{clk}+{cpu}+{l1i}+{l1d}+{l2}+{bp}")