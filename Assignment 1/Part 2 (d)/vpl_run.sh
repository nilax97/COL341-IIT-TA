#! /bin/bash
echo "#! /bin/bash" >> vpl_execution
echo "export OMP_NUM_THREADS=1" >> vpl_execution
echo "export PATH=\"/bin/anaconda3/bin:\$PATH\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/train.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/test_X.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/test_pred.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/grades.csv\"" >> vpl_execution
echo "timeout 10m python3 -W ignore logistic_d.py train.csv test_X.csv pred.csv weight.csv">> vpl_execution
echo "python3 -W ignore grade_d.py pred.csv test_pred.csv" >> vpl_execution
echo "echo \"Please click the evaluate button for your scores to be counted. You need to do this for your final submission before the assignment deadline. \"">> vpl_execution
chmod +x vpl_execution