import json
import re
import sys

d=dict()
clk=str(sys.argv[1])+"GHz"

cpu=str(sys.argv[2])

with open('m5out/stats.txt','r') as f:
    lines=f.readlines()
    
    for line in lines:
        if line:
            
            d["clk_freq"]=float(sys.argv[1])
            
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



out_file = open(f"{clk}+{cpu}.json", "w")
  
json.dump(d, out_file)
  
out_file.close()

print(f"Results dumped at json file-{clk}+{cpu}")