import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

#gradient 0
def dJ0(df, m,t0,t1, x0_col, x1_col, y_col):
    s = 0
    for i in range(m):
        s += ((t0 * df[x0_col][i] + t1 * df[x1_col][i]) - df[y_col][i]) * df[x0_col][i]
    return s/m 

#gradient 1
def dJ1(df, m,t0,t1, x0_col, x1_col, y_col):
    s = 0
    for i in range(m):
        s += ((t0*df[x0_col][i] +t1*df[x1_col][i])-df[y_col][i])*df[x1_col][i]
    return s/m 

def MSE(df, t0,t1,m, x1_col, y_col):
    mse = 0
    for i in range(m):
        mse += (t0+ t1*df[x1_col][i]- df[y_col][i])**2
    return mse/m

def gradientD(df, alpha, t0, t1, nbrIteration, m, x0_col, x1_col, y_col):
    mse_list=[]
    for i in range(nbrIteration):
        t0 = t0 - alpha*dJ0(df,m,t0,t1, x0_col, x1_col, y_col)
        t1 = t1 - alpha*dJ1(df,m,t0,t1, x0_col, x1_col, y_col)
        mse_list.append(MSE(df,t0,t1,m, x1_col, y_col))
    #(t0,t1)
    return mse_list

def minmax(x1):
    return (x1 - x1.min()) / (x1.max() - x1.min())

def normalize(df):
    return df.apply(minmax)
