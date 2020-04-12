#! /bin/bash
echo "#! /bin/bash" >> vpl_execution
echo "export OMP_NUM_THREADS=1" >> vpl_execution
echo "export PATH=\"/bin/anaconda3/bin:\$PATH\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~pranshu/SVM/train.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~pranshu/SVM/test_public.csv\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~pranshu/SVM/test_labels.txt\"" >> vpl_execution
echo "python3 -W ignore svm.py train.csv test_public.csv testpred.txt">> vpl_execution
echo "python3 -W ignore grade.py testpred.txt test_labels.txt" >> vpl_execution
chmod +x vpl_execution