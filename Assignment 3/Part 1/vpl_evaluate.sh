#! /bin/bash
echo "#! /bin/bash" >> vpl_execution
echo "export OMP_NUM_THREADS=1" >> vpl_execution
echo "export PATH=\"/bin/anaconda3/bin:\$PATH\"" >> vpl_execution
echo "python3 -W ignore grade_compete.py cnn_predictions /bin/data/A3/a3_test_labels.csv moodleID" >> vpl_execution
chmod +x vpl_execution