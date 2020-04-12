#! /bin/bash
echo "#! /bin/bash" >> vpl_execution
echo "export OMP_NUM_THREADS=1" >> vpl_execution
echo "export PATH=\"/bin/anaconda3/bin:\$PATH\"" >> vpl_execution
echo "python3 -W ignore neural_d.py /bin/data/A2/CIFAR10/train.csv /bin/data/A2/CIFAR10/public.csv pred_d.txt">> vpl_execution
echo "python3 -W ignore grade_d.py pred_d.txt /bin/data/A2/CIFAR10/public_labels.txt moodleID" >> vpl_execution
chmod +x vpl_execution