#! /bin/bash
echo "#! /bin/bash" >> vpl_execution
echo "export OMP_NUM_THREADS=1" >> vpl_execution
echo "export PATH=\"/bin/anaconda3/bin:\$PATH\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/train.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/test_X.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/test_pred.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/preds_21.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/weights_21.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/param21.txt\"" >> vpl_execution
echo "python3 -W ignore logistic_b.py train.csv test_X.csv param21.txt pred.csv weight.csv">> vpl_execution
echo "python3 -W ignore grade_b.py pred.csv weight.csv preds_21.csv weights_21.csv" >> vpl_execution
chmod +x vpl_execution