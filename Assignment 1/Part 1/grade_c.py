import sys
import numpy as np
import os
import pandas as pd
import math


def comment(s):
    '''formats strings to create VPL comments'''
    print('Comment :=>> ' + s)

def grade(num):
    '''formats a number to create a VPL grade'''
    print('Grade :=>> ' + str(num))

pred_file = sys.argv[1]
gold_file = sys.argv[2]

if os.path.exists(pred_file) == False:
    comment("Prediction file not created for part c");
    grade(0);
    exit();

Y_pred = np.loadtxt(pred_file);
Y_gold = np.loadtxt(gold_file);

if(Y_pred.shape[0] != Y_gold.shape[0]):
    comment("Prediction file of wrong dimensions for part c");
    grade(0);
    exit();

error = np.sum(np.square(Y_pred - Y_gold))/np.sum(np.square(Y_gold));
error = np.round(error, decimals = 5);
error = min(error, 1.0);
marks = (1.0 - error) * 100;
marks = np.round(marks, decimals = 2);
comment("Part (c): ");
comment("Normalized L2 Error for part (c)= " + str(np.round(error, decimals=5)));
data = pd.read_csv("grades.csv")
df = data["Virtual programming lab: Assignment 1 - Part 1 (Real)"].replace('-',-1)
df = pd.to_numeric(df)
rank = df[df > marks].count() + 1;
total = df[df > -1].count() + 1;
if(marks > 30):
    marks1 = 34 + 66 * (total - rank + 1)/ total;
else:
    marks1 = 0
marks1 = np.round(marks1, decimals = 2);
grade(marks);
comment("Rank (tentative) = " + str(rank) + " / " + str(total) + "  (based on evaluations until 12th August)");
comment("Tentative score : " + str(marks1) + "; Final score will be calculated based on your code's performance on the final evaluation dataset")
comment("Please ignore the Proposed Grade on the top right, it is there only for technical reasons. The expected grades are reflected in the comments section")
