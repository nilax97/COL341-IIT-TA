#! /bin/bash
echo "#! /bin/bash" >> vpl_execution
echo "export OMP_NUM_THREADS=1" >> vpl_execution
echo "export PATH=\"/bin/anaconda3/bin:\$PATH\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~pranshu/DT/train.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~pranshu/DT/test_private.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~pranshu/DT/private_labels.txt\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~pranshu/DT/valid.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~pranshu/DT/valid_labels.txt\"" >> vpl_execution
echo "python3 -W ignore dt.py train.csv valid.csv test_private.csv validpred.txt testpred.txt">> vpl_execution
echo "python3 -W ignore grade.py validpred.txt valid_labels.txt testpred.txt private_labels.txt" >> vpl_execution
#echo "python3 -W ignore dt.py train.csv valid.csv valid.csv validpred.txt testpred.txt">> vpl_execution
#echo "python3 -W ignore grade.py validpred.txt valid_labels.txt testpred.txt valid_labels.txt" >> vpl_execution


chmod +x vpl_execution