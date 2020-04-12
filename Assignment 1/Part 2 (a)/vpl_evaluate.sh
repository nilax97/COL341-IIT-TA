#! /bin/bash
echo "#! /bin/bash" >> vpl_execution
echo "export OMP_NUM_THREADS=1" >> vpl_execution
echo "export PATH=\"/bin/anaconda3/bin:\$PATH\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/train.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/test_X.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/test_pred.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/preds_11.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/weights_11.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/preds_12.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/weights_12.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/preds_13.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/weights_13.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/param11.txt\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/param12.txt\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/param13.txt\"" >> vpl_execution
echo "echo \"FIXED LEARNING RATE:\"" >> vpl_execution
echo "python3 -W ignore logistic_a.py train.csv test_X.csv param11.txt pred.csv weight.csv">> vpl_execution
echo "python3 -W ignore grade_a.py pred.csv weight.csv preds_11.csv weights_11.csv" >> vpl_execution
echo "echo \"ADAPTIVE LEARNING RATE:\"" >> vpl_execution
echo "python3 -W ignore logistic_a.py train.csv test_X.csv param12.txt pred.csv weight.csv">> vpl_execution
echo "python3 -W ignore grade_a.py pred.csv weight.csv preds_12.csv weights_12.csv" >> vpl_execution
echo "echo \"ALPHA-BETA BACKTRACKING:\"" >> vpl_execution
echo "python3 -W ignore logistic_a.py train.csv test_X.csv param13.txt pred.csv weight.csv">> vpl_execution
echo "python3 -W ignore grade_a.py pred.csv weight.csv preds_13.csv weights_13.csv" >> vpl_execution
echo "python3 -W ignore grade_final.py" >> vpl_execution
chmod +x vpl_execution