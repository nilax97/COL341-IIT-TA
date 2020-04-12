import numpy as np
import pandas as pd
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
weight_inp = sys.argv[2]
out_gold = sys.argv[3]
weight_gold = sys.argv[4]

if os.path.exists(out_inp) == False:
    comment("Prediction file not created for part a");
    exit();
if os.path.exists(weight_inp) == False:
    comment("Weight file not created for part a");
    exit();


pred = np.loadtxt(out_inp , delimiter = ",", dtype='<U10')
pred_gold = np.loadtxt(out_gold, delimiter = ",", dtype='<U10')
weights = np.loadtxt(weight_inp, delimiter=",");
weight_gold = np.loadtxt(weight_gold, delimiter=",");

if(pred.shape[0] != pred_gold.shape[0]):
    comment("Prediction file of wrong shape");
    comment(str(pred.shape[0]) + " - your file" );
    comment(str(pred_gold.shape[0]) + " - gold file" );
    exit();
if(weights.shape != weight_gold.shape):
    comment("Weight file of wrong shape");
    comment(str(weights.shape) + " - your file" );
    comment(str(weight_gold.shape) + " - gold file" );
    exit();

pred_val = 0;
weight_val = 0;

correct = 0
wrong = 0;
for x in range(pred_gold.shape[0]):
    if(pred[x] == pred_gold[x]):
        correct = correct + 1
    elif(wrong < 5):
        comment(str(pred[x]) + " - your prediction" );
        comment(str(pred_gold[x]) + " - gold prediction" );
        comment("______");
        wrong = wrong + 1
        
pred_error = correct/pred_gold.shape[0]
weight_error = np.sum(np.square(weights - weight_gold))/np.sum(np.square(weight_gold))
if(weight_error > 1e-3):
    x = np.argmax(abs(weights - weight_gold))
    comment("Max weight error at : " + str(int(x/weights.shape[1])) + "," + str(x%weights.shape[1]))

if pred_error == 1.0:
    pred_val = 1;
elif pred_error > 0.95:
    pred_val = 0.75;
elif pred_error > 0.9:
    pred_val = 0.5;
elif pred_error > 0.85:
    pred_val = 0.25;
else:
    pred_val = 0;

if weight_error < 1e-3:
    weight_val = 1;
elif weight_error < 1e-2:
    weight_val = 0.75;
elif weight_error < 1e-1:
    weight_val = 0.5;
elif weight_error < 2.5e-1:
    weight_val = 0.25;
else:
    weight_val = 0;

comment("Part (a):");
comment("Prediction accuracy score (a): " + str(np.round(pred_error,decimals=5)))
comment("Weight normalized L2 Error for part (a): " + str(np.round(weight_error,decimals=5)));
comment("Grade for part (a) (tentative) = " + str(pred_val * 5 + weight_val * 5));
grades = pred_val * 5 + weight_val * 5;

f = open("counter.txt", "a+");
f.write(str(grades) + "\n");



