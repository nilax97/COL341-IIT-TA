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

test_inp = sys.argv[1]
test_gold = sys.argv[2]

if os.path.exists(test_inp) == False:
    comment("Prediction file not created for test set");
    exit();

pred = np.loadtxt(test_inp);
pred_gold = np.loadtxt(test_gold);

if(pred.shape[0] != pred_gold.shape[0]):
    comment("Prediction file of wrong dimensions for test set");
    exit();

test_acc = float(np.sum(pred == pred_gold))/pred.shape[0];
#comment("Prediction accuracy on test set(current submission): " + str(np.round(test_acc,decimals=5)))

if test_acc >= 0.88:
    weight_val = 1;
elif test_acc >= 0.80:
    weight_val = 0.5;
else:
    weight_val = 0;

comment(str(np.round(test_acc,decimals=5)))
#comment("Prediction Accuracy on Public Test: " + str(np.round(test_acc,decimals=5)));
#comment("Grade for SVM (tentative) = " + str(weight_val * 50));   

