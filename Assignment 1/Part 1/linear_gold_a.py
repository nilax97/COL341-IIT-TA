import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
import sys

path_train = sys.argv[1]
path_test = sys.argv[2]
path_out = sys.argv[3]
path_weight = sys.argv[4]

train = np.loadtxt("/bin/data/BlogFeedback/" + path_train, delimiter=",");
test = np.loadtxt("/bin/data/BlogFeedback/" + path_test, delimiter=",")

X1_train = train[:,:-1].astype('float64')
Y_train = train[:,-1].astype('float64')
Y_train = Y_train.reshape((Y_train.shape[0],1))
ones_train = np.ones(Y_train.shape)
X_train = np.c_[ones_train,X1_train]

X1_test = test.astype('float64')
ones_test = np.ones((X1_test.shape[0],1))
X_test = np.c_[ones_test,X1_test]

theta = (np.linalg.pinv(X_train.T @ X_train) @ (X_train.T @ Y_train))
Y_pred = X_test @ theta

np.savetxt(path_out, Y_pred);
np.savetxt(path_weight, theta);