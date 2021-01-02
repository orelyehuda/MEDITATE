from tqdm import tqdm
import time 

switch = True

for j in range(8):
    for i in (t := tqdm(range(9))):
        if(switch):
            t.set_description("Breath in...")
        else:
            t.set_description("Breath out...")

        time.sleep(1)
        
        
    switch = not switch 

