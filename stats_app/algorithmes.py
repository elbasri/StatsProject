import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

#gradient 0
def dJ0(df, m,t0,t1):
    s = 0
    for i in range(m):
        s += ((t0*df.x0[i] +t1*df.x1[i])-df.y[i])*df.x0[i]
    return s/m 

#gradient 1
def dJ1(df, m,t0,t1):
    s = 0
    for i in range(m):
        s += ((t0*df.x0[i] +t1*df.x1[i])-df.y[i])*df.x1[i]
    return s/m 

def MSE(df, t0,t1,m):
    mse = 0
    for i in range(m):
        mse += (t0+ t1*df.x1[i]- df.y[i])**2
    return mse/m

def gradientD(df):
    alpha, t0, t1 = 0.0002, 1, 2
    nbrIteration = 200
    m=50
    mse_list=[]
    for i in range(nbrIteration):
        t0 = t0 - alpha*dJ0(df,m,t0,t1)
        t1 = t1 - alpha*dJ1(df,m,t0,t1)
        mse_list.append(MSE(df,t0,t1,m))
    #(t0,t1)
    return mse_list