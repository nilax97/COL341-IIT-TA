import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
import sys

path_train = sys.argv[1]
path_test = sys.argv[2]
path_reg = sys.argv[3]
path_out = sys.argv[4]
path_weight = sys.argv[5]

train = np.loadtxt("/bin/data/BlogFeedback/" + path_train, delimiter=",");
test = np.loadtxt("/bin/data/BlogFeedback/" + path_test, delimiter=",");
reg = np.loadtxt("/bin/data/BlogFeedback/" + path_reg, delimiter=",");

X1_train = train[:,:-1].astype('float64')
Y_train = train[:,-1].astype('float64')
Y_train = Y_train.reshape((Y_train.shape[0],1))
ones_train = np.ones(Y_train.shape)
X_train = np.c_[ones_train,X1_train]

X1_test = test.astype('float64')
ones_test = np.ones((X1_test.shape[0],1))
X_test = np.c_[ones_test,X1_test]

loss = np.zeros(reg.shape[0]);

kf = KFold(n_splits=10)

for train_index, test_index in kf.split(X_train):
    X_1, X_2 = X_train[train_index], X_train[test_index]
    Y_1, Y_2 = Y_train[train_index], Y_train[test_index]
    
    for i in range(reg.shape[0]):
        theta = (np.linalg.pinv(X_1.T @ X_1 - reg[i] * np.ones((X_1.shape[1],X_1.shape[1]))) @ (X_1.T @ Y_1))
        Y_pred = X_2 @ theta
        loss[i] = loss[i] + np.sum(np.square(Y_pred, Y_2)) / np.sum(np.square(Y_2))

t = np.argmin(loss);
theta = (np.linalg.pinv(X_train.T @ X_train - reg[t] * np.ones((X_train.shape[1],X_train.shape[1]))) @ (X_train.T @ Y_train))
Y_pred = X_test @ theta

np.savetxt(path_out, Y_pred);
np.savetxt(path_weight, theta);
print("Gold regularization hyperparameter = ",reg[t]);