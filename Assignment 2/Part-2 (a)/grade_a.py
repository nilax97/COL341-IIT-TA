import numpy as np
from sklearn.metrics import accuracy_score
import sys

pred_file = sys.argv[1]
gold_file = sys.argv[2]

y_pred = np.loadtxt(pred_file)
# y_pred = y_pred[:100]
y_act = np.loadtxt(gold_file)
if(len(y_act) != len(y_pred)):
	print("Error in Prediction Lengths")
else:
	score = accuracy_score(y_act, y_pred)
	print("Your accuracy for this part in % is: ", score*100)

print("The expected accuracy is at least 65%")