#! /bin/bash
echo "#! /bin/bash" >> vpl_execution
echo "export OMP_NUM_THREADS=1" >> vpl_execution
echo "export PATH=\"/bin/anaconda3/bin:\$PATH\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~pranshu/weight_gold.txt\"" >> vpl_execution
echo "python3 -W ignore neural_b.py /bin/data/A2/CIFAR10/train.csv /bin/data/A2/CIFAR10/param.txt weight_b.txt">> vpl_execution
echo "python3 -W ignore grade_b.py weight_b.txt weight_gold.txt" >> vpl_execution
chmod +x vpl_execution