import numpy as np
from sklearn.metrics import accuracy_score
import sys, subprocess

pred_file = sys.argv[1]
gold_file = sys.argv[2]
moodleID = sys.argv[3]

ID = np.genfromtxt(moodleID,dtype='str')

y_pred = np.loadtxt(pred_file)
# y_pred = y_pred[:100]
y_act = np.loadtxt(gold_file)
if(len(y_act) != len(y_pred)):
	print("Error in Prediction Lengths")
	score = 0
else:
	score = accuracy_score(y_act, y_pred)
	print("Your accuracy for this part in % is: ", score*100)


call = "python3 -W ignore /opt/lampp/htdocs/dashboard/Table/upgrade.py "+str(ID)+" "+str(score)+" " 
call_str = "sshpass -p 'tintin@902' ssh -q -o StrictHostKeyChecking=no vinayak@10.237.23.117 '" + call +"'"
res_str = subprocess.getoutput(call_str)
print(res_str)


print("Please see the leaderboard at: ")
print("http://10.237.23.117/dashboard/Table/")
