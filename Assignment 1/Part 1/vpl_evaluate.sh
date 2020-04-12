#! /bin/bash
echo "#! /bin/bash" >> vpl_execution
echo "export OMP_NUM_THREADS=1" >> vpl_execution
echo "export PATH=\"/bin/anaconda3/bin:\$PATH\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/pred_gold_a.txt\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/weight_gold_a.txt\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/pred_gold_b.txt\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/weight_gold_b.txt\"" >> vpl_execution
echo "wget -q \"http://www.cse.iitd.ac.in/~ph1150813/grades.csv\"" >> vpl_execution
echo "python3 -W ignore linear.py a /bin/data/BlogFeedback/A1_train.csv /bin/data/BlogFeedback/A1_test.csv pred_a.txt weight_a.txt">> vpl_execution
echo "python3 -W ignore grade_a.py pred_a.txt weight_a.txt pred_gold_a.txt weight_gold_a.txt" >> vpl_execution
echo "python3 -W ignore linear.py b /bin/data/BlogFeedback/A1_train.csv /bin/data/BlogFeedback/A1_test.csv /bin/data/BlogFeedback/regular.txt pred_b.txt weight_b.txt">> vpl_execution
echo "python3 -W ignore grade_b.py pred_b.txt weight_b.txt pred_gold_b.txt weight_gold_b.txt" >> vpl_execution
echo "python3 -W ignore linear.py c /bin/data/BlogFeedback/A1_train.csv /bin/data/BlogFeedback/A1_test.csv pred_c.txt">> vpl_execution
echo "python -W ignore grade_c.py pred_c.txt /bin/data/BlogFeedback/A1_test_out.csv">> vpl_execution
chmod +x vpl_execution