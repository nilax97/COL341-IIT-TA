import numpy as np
from sklearn.metrics import accuracy_score
import sys, subprocess

pred_file = sys.argv[1]
gold_file = sys.argv[2]

y_pred = np.loadtxt(pred_file)
# y_pred = y_pred[:100]
y_act = np.loadtxt(gold_file)
if(len(y_act) != len(y_pred)):
	print("Error in Code Predictions")
	score = 0
else:
	score = accuracy_score(y_act, y_pred)
	print("Your accuracy is: ", score*100)

# if os.path.exists(weight_inp) == False:
#     comment("Weight file not created for part a");
#     exit();

# weights = np.loadtxt(weight_inp, delimiter="\n");
# weight_gold = np.loadtxt(weight_gold, delimiter="\n");

# if(weights.shape != weight_gold.shape):
#     comment("Weight file of wrong shape");
#     comment(str(weights.shape[0]) + " - your file" );
#     comment(str(weight_gold.shape[0]) + " - gold file" );
#     exit();

# weight_val = 0;

# weight_error = np.sum(np.square(weights - weight_gold))/np.sum(np.square(weight_gold))

# if weight_error < 1e-3:
#     weight_val = 1;
# elif weight_error < 1e-2:
#     weight_val = 0.75;
# elif weight_error < 1e-1:
#     weight_val = 0.5;
# elif weight_error < 2.5e-1:
#     weight_val = 0.25;
# else:
#     weight_val = 0;

# comment("Part (a):");

# comment("Weight normalized L2 Error for part (a): " + str(np.round(weight_error,decimals=5)));
# comment("Grade for part (a) (tentative) = " + str(weight_val * 50));
# grades = weight_val * 50;
# grade(grades);



