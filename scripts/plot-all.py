import re
import glob
import numpy as np
import sys

import os
import time 

import subprocess

file_path = "../scripts/plotting.py"

number = "6"

names = ["FillMean", "FillZero", "FillPhiRandom", "RemoveJets", "RemovePhi", "Jets0", "Jets1", "Jets2"]


models = []

for name in names:
    models += glob.glob("../plots/raw/" + name + number + "*.npz")

for model in models:
    timestamp = model.split("_")[-1].split('.')[0]
    print(timestamp)
    start = time.time()
    command = f"python3 {file_path} " + timestamp + " 0 "
    subprocess.run(command, shell=True)        
    end = time.time()
    print(f"Finished in {end-start} seconds")
    print("")


