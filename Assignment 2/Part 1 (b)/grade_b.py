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

weight_inp = sys.argv[1]
weight_gold = sys.argv[2]

if os.path.exists(weight_inp) == False:
    comment("Weight file not created for part a");
    exit();

weights = np.loadtxt(weight_inp, delimiter="\n");
weight_gold = np.loadtxt(weight_gold, delimiter="\n");

if(weights.shape != weight_gold.shape):
    comment("Weight file of wrong shape");
    comment(str(weights.shape[0]) + " - your file" );
    comment(str(weight_gold.shape[0]) + " - gold file" );
    exit();

weight_val = 0;

weight_error = np.sum(np.square(weights - weight_gold))/np.sum(np.square(weight_gold))

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

comment("Part (b):");

comment("Weight normalized L2 Error for part (b): " + str(np.round(weight_error,decimals=5)));
comment("Grade for part (b) (tentative) = " + str(weight_val * 12.5));
grades = weight_val * 12.5;
grade(grades);
