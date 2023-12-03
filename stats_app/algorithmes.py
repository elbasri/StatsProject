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

def mediane_colonne(dataframe, nom_colonne):
    # Vérifier si la colonne existe dans la DataFrame
    if nom_colonne in dataframe.columns:
        # Extraire la colonne spécifiée
        colonne = dataframe[nom_colonne]
        
        # Vérifier si la colonne est numérique
        if pd.api.types.is_numeric_dtype(colonne):
            # Calculer la médiane de la colonne
            mediane = colonne.median()
            return mediane
        else:
            return f"La colonne '{nom_colonne}' n'est pas de type numérique."
    else:
        return f"La colonne '{nom_colonne}' n'existe pas dans la DataFrame."

def moyenne_colonne(dataframe, nom_colonne):
    # Vérifier si la colonne existe dans la DataFrame
    if nom_colonne in dataframe.columns:
        # Extraire la colonne spécifiée
        colonne = dataframe[nom_colonne]
        
        # Vérifier si la colonne est numérique
        if pd.api.types.is_numeric_dtype(colonne):
            # Calculer la moyenne de la colonne
            moyenne = colonne.mean()
            return moyenne
        else:
            return f"La colonne '{nom_colonne}' n'est pas de type numérique."
    else:
        return f"La colonne '{nom_colonne}' n'existe pas dans la DataFrame."

def variance_colonne(dataframe, nom_colonne):
    # Vérifier si la colonne existe dans la DataFrame
    if nom_colonne in dataframe.columns:
        # Extraire la colonne spécifiée
        colonne = dataframe[nom_colonne]
        
        # Vérifier si la colonne est numérique
        if pd.api.types.is_numeric_dtype(colonne):
            # Calculer la variance de la colonne
            variance = colonne.var()
            return variance
        else:
            return f"La colonne '{nom_colonne}' n'est pas de type numérique."
    else:
        return f"La colonne '{nom_colonne}' n'existe pas dans la DataFrame."

def ecart_type_colonne(dataframe, nom_colonne):
    # Vérifier si la colonne existe dans la DataFrame
    if nom_colonne in dataframe.columns:
        # Extraire la colonne spécifiée
        colonne = dataframe[nom_colonne]
        
        # Vérifier si la colonne est numérique
        if pd.api.types.is_numeric_dtype(colonne):
            # Calculer l'écart type de la colonne
            ecart_type = colonne.std()
            return ecart_type
        else:
            return f"La colonne '{nom_colonne}' n'est pas de type numérique."
    else:
        return f"La colonne '{nom_colonne}' n'existe pas dans la DataFrame."
