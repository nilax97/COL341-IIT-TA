import numpy as np
import pandas as pd
import subprocess 
import math
import os
import sys
from sklearn.metrics import f1_score

def comment(s):
    '''formats strings to create VPL comments'''
    print('Comment :=>> ' + s)

def grade(num):
    '''formats a number to create a VPL grade'''
    print('Grade :=>> ' + str(num))

out_inp = sys.argv[1]
out_gold = sys.argv[2]
#moodleID = sys.argv[3]
#ID = np.genfromtxt(moodleID,dtype='str')

if os.path.exists(out_inp) == False:
    comment("Prediction file not created for part ");
    exit();

pred = np.loadtxt(out_inp);
pred_gold = np.loadtxt(out_gold);

if(pred.shape[0] != pred_gold.shape[0]):
    comment("Prediction file of wrong dimensions for part a");
    exit();

comment("Part (c):");

pred_acc = float(np.sum(pred == pred_gold))/pred.shape[0];
comment("Prediction accuracy on public test set(current submission): " + str(np.round(pred_acc,decimals=5)))
'''
call = "nohup bash proxy.sh &"
call_str = "sshpass -p 'umbrella' ssh -o StrictHostKeyChecking=no pranshu@10.237.20.124 '" + call +"'"
subprocess.getoutput(call_str)

if(pred_acc > 0.20):
    call = "python3 subgf_a2c.py " + str(ID) + " " + str(pred_acc)
    call_str = "sshpass -p 'umbrella' ssh -o StrictHostKeyChecking=no pranshu@10.237.20.124 '" + call +"'"
    subprocess.getoutput(call_str)
    
call = "python3 grank_a2c.py " + str(ID)
call_str = "sshpass -p 'umbrella' ssh -o StrictHostKeyChecking=no pranshu@10.237.20.124 '" + call +"'"
res_str = subprocess.getoutput(call_str)
split_res = res_str.split(' ')
print(split_res)
split_res = split_res[-2:]

rank, total = [int(x) for x in split_res]
if(rank != 0):
    pred_val = 0.34 + 0.66 * (total - rank + 1)/ total;
    comment("Rank (tentative and based on best submission till now) = " + str(rank) + " / " + str(total)); 
else:
    pred_val = 0
    comment("Rank (tentative and based on best submission till now) = NA"); 
'''   
comment("Grade for part (c) (tentative and based on best submission till now) = " + str(pred_acc));

