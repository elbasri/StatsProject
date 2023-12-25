import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from bs4 import BeautifulSoup
from scipy.integrate import quad
import seaborn as sns

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

def etendue_colonne(dataframe, nom_colonne):
    # Vérifier si la colonne existe dans la DataFrame
    if nom_colonne in dataframe.columns:
        # Extraire la colonne spécifiée
        colonne = dataframe[nom_colonne]
        
        # Vérifier si la colonne est numérique
        if colonne.dtype.kind in 'iufc':
            # Calculer l'étendue de la colonne
            etendue = colonne.max() - colonne.min()
            return etendue
        else:
            return f"La colonne '{nom_colonne}' n'est pas de type numérique."
    else:
        return f"La colonne '{nom_colonne}' n'existe pas dans la DataFrame."

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

# Fonction pour supprimer une colonne spécifique
def supprimer_colonne(df, nom_colonne):
    # Utilisation de la méthode drop pour supprimer la colonne
    dataframe_sans_colonne = df.drop(columns=[nom_colonne], axis=1)
    return dataframe_sans_colonne

# Fonction pour renvoyer une ligne spécifique
def obtenir_ligne(df, index_ligne):
    # Utilisation de iloc pour sélectionner une ligne par son index
    ligne_selectionnee = df.iloc[index_ligne]
    return ligne_selectionnee

# Fonction pour sélectionner des lignes en fonction d'une condition
def selection_lignes(df, condition):
    # Utilisation de la méthode loc pour filtrer les lignes
    resultats = df.loc[condition]
    return resultats

# Fonction pour accéder à une valeur via le nom de la colonne
def valeur_par_colonne(df, nom_colonne, index_ligne):
    valeur = df.at[index_ligne, nom_colonne]
    return valeur

# Fonction pour filtrer une DataFrame en utilisant la méthode query
def filtrer_par_condition(df, condition):
    resultat_filtrage = df.query(condition)
    return resultat_filtrage

# Fonction pour calculer les moyennes des colonnes spécifiques par groupe
def moyenne_par_groupe(df, colonne_groupe, colonnes_moyenne):
    moyennes_groupes = df.groupby(colonne_groupe)[colonnes_moyenne].mean()
    return moyennes_groupes


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

def line_plot(df, x_col, y_col, title='Graphique', x_label='X', y_label='Y'):
    sns.set()  # Set the style (optional)
    
    # Create a figure and axes object
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot the line graph using the specified columns on the axes object
    sns.lineplot(x=x_col, y=y_col, data=df, marker='o', color='b', label=y_col, ax=ax)
    
    # Add labels and title to the axes object
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    
    # Display the legend
    ax.legend()
    
    # Return the figure object
    return fig


# Fonction pour créer un graphique de dispersion à partir d'une DataFrame
def scatter_dataframe(df, x_col, y_col, title="Graphique de Dispersion", x_label="Axe X", y_label="Axe Y"):
    fig, ax = plt.subplots(figsize=(8, 6))  # Taille de la figure
    
    # Création du scatter plot avec Seaborn
    sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
    
    # Ajout des titres et des étiquettes
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    
    # Retourne la figure
    return fig

# Fonction pour créer et afficher un graphique de dispersion avec une variable catégorique pour différencier les points sur le graphique
def graphique_dispersion_categories(df, x_col, y_col, categorie_col, titre="Graphique de Dispersion", etiquette_x="Axe X", etiquette_y="Axe Y", ordre_categorie=None):
    fig, ax = plt.subplots(figsize=(8, 6))  # Taille de la figure
    
    # Création du scatter plot avec Seaborn en utilisant une variable catégorique
    sns.scatterplot(x=x_col, y=y_col, hue=categorie_col, data=df, hue_order=ordre_categorie, ax=ax)
    
    # Ajout des titres et des étiquettes
    ax.set_title(titre)
    ax.set_xlabel(etiquette_x)
    ax.set_ylabel(etiquette_y)
    
    # Retourne la figure
    return fig

# Fonction pour créer et afficher un diagramme en boîte
def boite_a_moustaches(df, x_col, y_col, hue_col, titre="Diagramme en Boîte", etiquette_x="Axe X", etiquette_y="Axe Y"):
    fig, ax = plt.subplots(figsize=(8, 6))  # Taille de la figure
    
    # Création du diagramme en boîte avec Seaborn
    sns.boxplot(x=x_col, y=y_col, hue=hue_col, data=df, ax=ax)
    
    # Ajout des titres et des étiquettes
    ax.set_title(titre)
    ax.set_xlabel(etiquette_x)
    ax.set_ylabel(etiquette_y)
    
    # Retourne la figure
    return fig

# Fonction pour créer et afficher un histogramme à partir d'une colonne d'une DataFrame
def histogramme_dataframe(df, colonne, titre="Histogramme", xlabel="Valeurs", ylabel="Fréquence", hue=None):
    # Create a figure and axes object
    fig, ax = plt.subplots(figsize=(8, 6))

    # Create the histogram with Seaborn on the axes object
    sns.histplot(data=df, x=colonne, kde=False, hue=hue, ax=ax)  # kde=False disables the density estimate

    # Add titles and labels to the axes object
    ax.set_title(titre)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Return the figure object
    return fig

# Fonction pour créer et afficher un histogramme horizontal à partir d'une colonne d'une DataFrame
def histogramme_horizontal_dataframe(df, colonne, titre="Histogramme Horizontal", xlabel="Fréquence", ylabel="Valeurs"):
    plt.figure(figsize=(8, 6))  # Taille de la figure
    
    # Création de l'histogramme horizontal avec Seaborn
    sns.histplot(data=df, y=colonne, kde=False)
    
    # Ajout des titres et des étiquettes
    plt.title(titre)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # Retourne la figure
    return plt.gcf()

# Fonction pour créer et afficher une estimation de densité par noyau (KDE) à partir d'une colonne d'une DataFrame
def kde_dataframe(df, colonne, titre="Estimation de Densité par Noyau (KDE)", xlabel="Valeurs", ylabel="Densité"):
    # Create a figure and axes object
    fig, ax = plt.subplots(figsize=(8, 6))

    # Create the Kernel Density Estimate (KDE) plot with Seaborn on the axes object
    sns.kdeplot(data=df[colonne], ax=ax)

    # Add titles and labels to the axes object
    ax.set_title(titre)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Return the figure object
    return fig

# Fonction pour créer et afficher une estimation de densité par noyau (KDE) univariée à partir d'une colonne d'une DataFrame
def kde_univarie_dataframe(df, colonne, titre="Estimation de Densité par Noyau (KDE)", xlabel="Valeurs", ylabel="Densité"):
    plt.figure(figsize=(8, 6))  # Taille de la figure
    
    # Création de l'estimation de densité par noyau (KDE) univariée avec Seaborn
    sns.kdeplot(data=df[colonne], fill=True)
    
    # Ajout des titres et des étiquettes
    plt.title(titre)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # Retourne la figure
    return plt.gcf()

# Fonction pour tracer un KDE (Estimation de densité par noyau) et un nuage de points (scatterplot)
def kde_et_scatterplot(df, x_colonne, y_colonne, titre="KDE et Scatterplot", xlabel="X", ylabel="Y"):
    plt.figure(figsize=(8, 6))  # Taille de la figure
    
    # Estimation de densité par noyau (KDE)
    sns.kdeplot(x=x_colonne, y=y_colonne, data=df)
    
    # Nuage de points (scatterplot)
    sns.scatterplot(x=x_colonne, y=y_colonne, data=df, color='black', alpha=0.6)
    
    # Ajout des titres et des étiquettes
    plt.title(titre)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # Retourne la figure
    return plt.gcf()

# Fonction pour tracer deux estimations de densité par noyau (KDE) pour deux catégories spécifiques d'une DataFrame en fonction de deux colonnes
def kde_deux_categories(df, x_colonne, y_colonne, categorie_colonne, categorie1, categorie2, titre="KDE pour Deux Catégories", xlabel="X", ylabel="Y"):

    # Filtrage des données par catégories spécifiques
    categorie1_data = df[df[categorie_colonne] == categorie1]
    categorie2_data = df[df[categorie_colonne] == categorie2]

    # Configuration du style seaborn
    sns.set_style('whitegrid')

    # Création de la figure
    plt.figure(figsize=(8, 6))

    # Estimation de densité par noyau (KDE) pour la première catégorie
    sns.kdeplot(x=x_colonne, y=y_colonne, data=categorie1_data, cmap="Blues", fill=True)

    # Estimation de densité par noyau (KDE) pour la deuxième catégorie
    sns.kdeplot(x=x_colonne, y=y_colonne, data=categorie2_data, cmap="Reds", fill=True)

    # Ajout des étiquettes pour les axes x et y avec une taille de police spécifiée
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)

    # Annotations pour indiquer les catégories
    plt.annotate(f"{categorie1}", (105, 32), color='blue', fontsize=16, fontweight='bold')
    plt.annotate(f"{categorie2}", (190, 18), color='red', fontsize=16, fontweight='bold')

    # Titre du graphique
    plt.title(titre)

    # Retourne la figure
    return plt.gcf()


# Fonction pour créer un graphique en violon (violinplot) pour une colonne spécifique après filtrage des données d'une DataFrame.
def graphique_violon(df, colonne_filtre, valeurs_filtre, colonne_graphique, titre="Graphique en Violon", xlabel="Valeurs"):

    # Filtrage des données
    filtered_data = df[df[colonne_filtre].isin(valeurs_filtre)]

    # Création du graphique en violon
    plt.figure(figsize=(8, 6))
    sns.violinplot(x=filtered_data[colonne_graphique])

    # Ajout du titre et de l'étiquette de l'axe x
    plt.title(titre)
    plt.xlabel(xlabel)

    # Retourne la figure
    return plt.gcf()


# Fonction pour créer un graphique en violon (violinplot) pour deux colonnes spécifiques d'une DataFrame en distinguant une troisième colonne (comme une variable catégorique)
def graphique_violon_multi(df, x_colonne, y_colonne, hue_colonne, titre="Graphique en Violon", xlabel="X", ylabel="Y"):

    plt.figure(figsize=(8, 6))  # Taille de la figure

    # Création du graphique en violon en distinguant les catégories avec la colonne 'hue'
    sns.violinplot(x=x_colonne, y=y_colonne, hue=hue_colonne, data=df)

    # Ajout du titre et des étiquettes pour les axes x et y
    plt.title(titre)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Retourne la figure
    return plt.gcf()

# Fonction pour créer un graphique à barres (barplot) pour deux colonnes spécifiques d'une DataFrame
def graphique_barres(df, x_colonne, y_colonne, titre="Graphique à Barres", xlabel="X", ylabel="Y"):
    # Create a figure and axes object
    fig, ax = plt.subplots(figsize=(8, 6))

    # Create the bar plot using the specified columns on the axes object
    sns.barplot(x=x_colonne, y=y_colonne, data=df, ax=ax)

    # Add title and labels to the axes object
    ax.set_title(titre)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Return the figure object
    return fig

# Fonction pour créer une carte de chaleur (heatmap) à partir d'une DataFrame
def carte_chaleur(df, annot=True, cmap='YlGnBu', cbar=True, titre="Carte de Chaleur", xlabel="Axe X", ylabel="Axe Y"):
   
    plt.figure(figsize=(8, 6))  # Taille de la figure

    # Création de la carte de chaleur avec Seaborn
    sns.heatmap(df, annot=annot, cmap=cmap, cbar=cbar)

    # Ajout du titre et des étiquettes pour les axes x et y
    plt.title(titre)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Retourne la figure
    return plt.gcf()

def pairplot_custom(df, column):
    graph = sns.pairplot(data=df, hue=column)
    return graph