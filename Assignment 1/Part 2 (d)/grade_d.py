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
out_gold = sys.argv[2]

if os.path.exists(out_inp) == False:
    comment("Prediction file not created for part d");
    exit();


pred_str = np.loadtxt(out_inp , delimiter = ",", dtype='<U10')
pred_gold_str = np.loadtxt(out_gold, delimiter = ",", dtype='<U10')

if(pred_str.shape[0] != pred_gold_str.shape[0]):
    comment("Prediction file of wrong shape");
    comment(str(pred_str.shape[0]) + " - your file" );
    comment(str(pred_gold_str.shape[0]) + " - gold file" );
    exit();

preds = np.zeros((pred_str.shape[0],5))
labels = ['not_recom', 'recommend', 'very_recom', 'priority', 'spec_prior']
for i in range(pred_str.shape[0]):
    for j in range(len(labels)):
        if(pred_str[i] == labels[j]):
            preds[i,j] = 1

preds_gold = np.zeros((pred_gold_str.shape[0],5))
labels = ['not_recom', 'recommend', 'very_recom', 'priority', 'spec_prior']
for i in range(pred_gold_str.shape[0]):
    for j in range(len(labels)):
        if(pred_gold_str[i] == labels[j]):
            preds_gold[i,j] = 1

preds = np.argmax(preds,axis=1)
preds_gold = np.argmax(preds_gold, axis=1)

correct = 0
wrong = 0
for x in range(preds_gold.shape[0]):
    if(preds[x] == preds_gold[x]):
        correct = correct + 1
    elif(wrong < 5):
        comment(str(pred_str[x]) + " - your prediction" );
        comment(str(pred_gold_str[x]) + " - gold prediction" );
        comment("______");
        wrong = wrong + 1

marks = f1_score(preds,preds_gold, average='weighted')*100;
marks = np.round(marks, decimals=2)
comment("Part (d):");
comment("Weighted F1 score for Part (d): " + str(np.round(marks,decimals=2)))
data = pd.read_csv("grades.csv")
df = data["Virtual programming lab: Assignment 1 - Part 2 (d) (Real)"].replace('-',-1)
df = pd.to_numeric(df)
rank = df[df > marks].count() + 1;
total = df[df > -1].count() + 1;
if(marks > 0.7):
    marks1 = 34 + 66 * (total - rank + 1)/ total;
marks1 = np.round(marks1, decimals=2)
grade(marks);
comment("Rank (tentative) = " + str(rank) + " / " + str(total) + "  (based on evaluations until 20th August)");
comment("Tentative score : " + str(marks1) + "; Final score will be calculated based on your code's performance on the final evaluation dataset")
comment("Please ignore the Proposed Grade on the top right, it is there only for technical reasons. The expected grades are reflected in the comments section")



