#! /bin/bash
echo "#! /bin/bash" >> vpl_execution
echo "export OMP_NUM_THREADS=1" >> vpl_execution
echo "export PATH=\"/bin/anaconda3/bin:\$PATH\"" >> vpl_execution
echo "python3 -W ignore neural_a.py /bin/data/A2/Toy/train.csv /bin/data/A2/Toy/param.txt weight_a.txt">> vpl_execution
echo "python3 -W ignore grade_a.py weight_a.txt /bin/data/A2/Toy/weight_gold.txt" >> vpl_execution
chmod +x vpl_execution