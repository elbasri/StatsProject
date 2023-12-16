import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from bs4 import BeautifulSoup
from scipy.integrate import quad

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
    description_table = df.describe().to_html()
    soup = BeautifulSoup(description_table, 'html.parser')
    return soup.prettify()

def longueur_dataframe(df):
    """
    Cette fonction prend un DataFrame en entrée et renvoie la longueur, c'est-à-dire le nombre de lignes du DataFrame.
    """
    return len(df)

def premieres_valeurs(df, nombre_lignes):
    """
    Cette fonction affiche les premières valeurs d'un DataFrame.
    """
    return df.head(nombre_lignes).to_html()

def valeurs_recentes(df, nombre_lignes):
    """
    Cette fonction affiche les valeurs les plus récentes ajoutées à un DataFrame.
    """
    return df.tail(nombre_lignes).to_html()

def mediane_colonne(df, nom_colonne):
    # Vérifier si la colonne existe dans la DataFrame
    if nom_colonne in df.columns:
        # Extraire la colonne spécifiée
        colonne = df[nom_colonne]
        
        # Vérifier si la colonne est numérique
        if pd.api.types.is_numeric_dtype(colonne):
            # Calculer la médiane de la colonne
            mediane = colonne.median()
            return mediane
        else:
            return f"La colonne '{nom_colonne}' n'est pas de type numérique."
    else:
        return f"La colonne '{nom_colonne}' n'existe pas dans la DataFrame."

def moyenne_colonne(df, nom_colonne):
    # Vérifier si la colonne existe dans la DataFrame
    if nom_colonne in df.columns:
        # Extraire la colonne spécifiée
        colonne = df[nom_colonne]
        
        # Vérifier si la colonne est numérique
        if pd.api.types.is_numeric_dtype(colonne):
            # Calculer la moyenne de la colonne
            moyenne = colonne.mean()
            return moyenne
        else:
            return f"La colonne '{nom_colonne}' n'est pas de type numérique."
    else:
        return f"La colonne '{nom_colonne}' n'existe pas dans la DataFrame."

def variance_colonne(df, nom_colonne):
    # Vérifier si la colonne existe dans la DataFrame
    if nom_colonne in df.columns:
        # Extraire la colonne spécifiée
        colonne = df[nom_colonne]
        
        # Vérifier si la colonne est numérique
        if pd.api.types.is_numeric_dtype(colonne):
            # Calculer la variance de la colonne
            variance = colonne.var()
            return variance
        else:
            return f"La colonne '{nom_colonne}' n'est pas de type numérique."
    else:
        return f"La colonne '{nom_colonne}' n'existe pas dans la DataFrame."

def ecart_type_colonne(df, nom_colonne):
    # Vérifier si la colonne existe dans la DataFrame
    if nom_colonne in df.columns:
        # Extraire la colonne spécifiée
        colonne = df[nom_colonne]
        
        # Vérifier si la colonne est numérique
        if pd.api.types.is_numeric_dtype(colonne):
            # Calculer l'écart type de la colonne
            ecart_type = colonne.std()
            return ecart_type
        else:
            return f"La colonne '{nom_colonne}' n'est pas de type numérique."
    else:
        return f"La colonne '{nom_colonne}' n'existe pas dans la DataFrame."
    
def mode(df, col): # Cette fonction prend une DataFrame et le nom d'une colonne, puis retourne le mode de la colonne spécifiée.

    mode = df[col].mode()
    # Si la colonne a plusieurs modes, mode renverra une Série.
    # Vous pouvez choisir le premier mode en utilisant .iloc[0].
    return mode.iloc[0] 

def valeur_max_colonne(df, nom_colonne):
    # Vérifie si la colonne existe dans la DataFrame
    if nom_colonne in df.columns:
        # Extraire la colonne spécifiée
        colonne = df[nom_colonne]
        
        # Vérifie si la colonne est numérique
        if pd.api.types.is_numeric_dtype(colonne):
            # Trouve la valeur maximale de la colonne spécifiée
            valeur_max = colonne.max()
            return valeur_max
        else:
            return f"La colonne '{nom_colonne}' n'est pas de type numérique."
    else:
        return f"La colonne '{nom_colonne}' n'existe pas dans la DataFrame."

def valeur_min_colonne(df, nom_colonne):
    # Vérifie si la colonne existe dans la DataFrame
    if nom_colonne in df.columns:
        # Extraire la colonne spécifiée
        colonne = df[nom_colonne]
        
        # Vérifie si la colonne est numérique
        if pd.api.types.is_numeric_dtype(colonne):
            # Trouve la valeur minimale de la colonne spécifiée
            valeur_min = colonne.min()
            return valeur_min
        else:
            return f"La colonne '{nom_colonne}' n'est pas de type numérique."
    else:
        return f"La colonne '{nom_colonne}' n'existe pas dans la DataFrame."
    
def permutations(elements):
    if len(elements) == 0:
        return [[]]

    result = []
    for i in range(len(elements)):
        reste = elements[:i] + elements[i+1:]
        for p in permutations(reste):
            result.append([elements[i]] + p)
    return result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def combinations(n, k):
    if n < k:
        return 0
    else:
        return factorial(n) // (factorial(k) * factorial(n - k))
    
def combinaisonsRecursiveM(elements, k):
    if k == 0:
        return [[]]
    if len(elements) == 0 or len(elements) < k:
        return []

    tete, queue = elements[0], elements[1:]

    avec_tete = [[tete] + c for c in combinaisonsRecursiveM(queue, k - 1)]
    sans_tete = combinaisonsRecursiveM(queue, k)

    return avec_tete + sans_tete

def esperance_variable_discrete(valeurs, probabilites):
    if len(valeurs) != len(probabilites):
        raise ValueError("Les listes de valeurs et de probabilités doivent avoir la même longueur.")
    
    esperance = 0
    for i in range(len(valeurs)):
        esperance += valeurs[i] * probabilites[i]
    
    return esperance

def esperance_variable_continue(fonction_densite_probabilite, borne_inf, borne_sup):
    def integrande(x):
        return x * fonction_densite_probabilite(x)
    
    resultat, _ = quad(integrande, borne_inf, borne_sup)
    return resultat