#Check disk usage of system

import os
import shutil

print(os.getcwd())

total, free, usage = shutil.disk_usage("/")
print(f"total disk usage is {total // (2**30)} GB")
print(f"usage disk usage is {usage // (2**30)} GB")
print(f"free disk usage is {free // (2**30)} GB")
      
      