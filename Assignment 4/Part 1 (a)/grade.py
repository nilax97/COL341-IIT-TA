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

valid_inp = sys.argv[1]
valid_gold = sys.argv[2]
test_inp = sys.argv[3]
test_gold = sys.argv[4]
#moodleID = sys.argv[5]
#ID = np.genfromtxt(moodleID,dtype='str')

if os.path.exists(valid_inp) == False:
    comment("Prediction file not created for validation set");
    exit();
    
if os.path.exists(test_inp) == False:
    comment("Prediction file not created for test set");
    exit();

pred = np.loadtxt(valid_inp);
pred_gold = np.loadtxt(valid_gold);

if(pred.shape[0] != pred_gold.shape[0]):
    comment("Prediction file of wrong dimensions for validation set");
    exit();

valid_acc = float(np.sum(pred == pred_gold))/pred.shape[0];
#comment("Prediction accuracy on validation set(current submission): " + str(np.round(valid_acc,decimals=5)))

pred = np.loadtxt(test_inp);
pred_gold = np.loadtxt(test_gold);

if(pred.shape[0] != pred_gold.shape[0]):
    comment("Prediction file of wrong dimensions for test set");
    exit();

test_acc = float(np.sum(pred == pred_gold))/pred.shape[0];
#comment("Prediction accuracy on test set(current submission): " + str(np.round(test_acc,decimals=5)))

score = 0.2*test_acc + 0.8*valid_acc
#score = test_acc 
#comment("Weighted Score(current submission): " + str(np.round(score,decimals=5)))
comment(str(np.round(score,decimals=5)))
'''
call = "nohup bash proxy.sh &"
call_str = "sshpass -p 'umbrella' ssh -o StrictHostKeyChecking=no pranshu@10.237.20.124 '" + call +"'"
subprocess.getoutput(call_str)

if(score > 0.75):
    call = "python3 subgf_a41.py " + str(ID) + " " + str(score)
    call_str = "sshpass -p 'umbrella' ssh -o StrictHostKeyChecking=no pranshu@10.237.20.124 '" + call +"'"
    subprocess.getoutput(call_str)
    
call = "python3 grank_a41.py " + str(ID)
call_str = "sshpass -p 'umbrella' ssh -o StrictHostKeyChecking=no pranshu@10.237.20.124 '" + call +"'"
res_str = subprocess.getoutput(call_str)
split_res = res_str.split(' ')
#print(split_res)
split_res = split_res[-2:]

rank, total = [int(x) for x in split_res]
if(rank != 0):
    pred_val = 0.34 + 0.66 * (total - rank + 1)/ total;
    comment("Rank (tentative and based on best submission till now) = " + str(rank) + " / " + str(total)); 
else:
    pred_val = 0
    comment("Rank (tentative and based on best submission till now) = NA"); 
   
comment("Grade for Decision Tree (tentative and based on best submission till now) = " + str(pred_val * 50));
'''
