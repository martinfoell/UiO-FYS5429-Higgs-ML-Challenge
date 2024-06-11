import os
import sys
import time 

import subprocess

file_path = "../scripts/neural-network.py"

name = str(sys.argv[1])
model = str(sys.argv[2])

epochs = {"fillMean" : "500" , "fillZero" : "500" , "fillPhiRandom" : "500" , "removeJets" : "500" , "fillStandarize" : "500" , "removePhi" : "500" , "jets0" : "500" , "jets1" : "500" , "jets2" : "500" , "jets0removePhi" : "500" , "jets1removePhi" : "500" , "jets2removePhi" : "500"}

# Grid
eta = [0.01, 0.1, 1, 10]
lamda = [0.001, 0.0001, 0.00001, 0.000001]

for e in eta:
    for l in lamda:
        print(f"Running with eta={e} and lamda={l}")
        start = time.time()
        command = f"python {file_path} " + name + " " + model + " " + epochs[model] + " 1000 " + str(e) + " " + str(l)
        subprocess.run(command, shell=True)        
        end = time.time()
        print(f"Finished in {end-start} seconds")
        print("")
        time.sleep(300)

