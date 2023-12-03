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

def visualiserCol(df, col, typeGraph):
    fig, ax = plt.subplots()
    
    # Plot the column data
    # ax.plot(df[col], label=col)
    ax.hist(df[col], bins='auto', color='blue', alpha=0.7)

    # Set plot title and axis labels
    ax.set_title(f'{typeGraph} - {col}')
    ax.set_xlabel('X-axis Label')
    ax.set_ylabel('Y-axis Label')

    # Add legend if needed
    ax.legend()

    return fig

def description_dataframe(df):
    """
    Cette fonction affiche les statistiques descriptives pour un DataFrame donné.
    """
    description = df.describe()
    print("Statistiques descriptives du DataFrame :")
    print(description)

def longueur_dataframe(df):
    """
    Cette fonction prend un DataFrame en entrée et renvoie la longueur, c'est-à-dire le nombre de lignes du DataFrame.
    """
    return len(df)

def premieres_valeurs(df, nombre_lignes=5):
    """
    Cette fonction affiche les premières valeurs d'un DataFrame.
    """
    premieres_lignes = df.head(nombre_lignes)
    print("Les", nombre_lignes, "premières lignes du DataFrame :")
    print(premieres_lignes)

def valeurs_recentes(df, nombre_lignes=5):
    """
    Cette fonction affiche les valeurs les plus récentes ajoutées à un DataFrame.
    """
    dernieres_valeurs = df.tail(nombre_lignes)
    print("Les", nombre_lignes, "dernières lignes du DataFrame :")
    print(dernieres_valeurs)

