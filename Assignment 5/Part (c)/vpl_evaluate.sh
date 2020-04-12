#! /bin/bash
echo "#! /bin/bash" >> vpl_execution
echo "export OMP_NUM_THREADS=1" >> vpl_execution
echo "export PATH=\"/bin/anaconda3/bin:\$PATH\"" >> vpl_execution
echo "python3 -W ignore naive_bayes_c.py /bin/data/A5/traindata.csv /bin/data/A5/testdata.csv weight_c.txt">> vpl_execution
echo "python3 -W ignore grade_c.py weight_c.txt /bin/data/A5/weight_gold.txt" >> vpl_execution
chmod +x vpl_execution