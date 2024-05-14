import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

 # Importamos los datos.
df = pd.read_csv('medical_examination.csv')

# Agregamos la columna [overweight].
df['overweight'] = (df['weight'] / ((df['height'] / 100 ) ** 2) > 25).astype(int)

# Normalizamos los datos para [cholesterol] y [gluc] glucosa. 
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

def draw_cat_plot():
   
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat = df_cat.rename(columns={0: 'total'})

    # Mod 
    graph = sns.catplot(data=df_cat, kind="bar", x="variable", y="total", hue="value", col="cardio")
    fig = graph.fig

    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    
    df_clean = df[(df['ap_lo'] <= df['ap_hi']) &
              (df['height'] >= df['height'].quantile(0.025)) &
              (df['height'] <= df['height'].quantile(0.975)) &
              (df['weight'] >= df['weight'].quantile(0.025)) &
              (df['weight'] <= df['weight'].quantile(0.975))]

    correlation = df_clean.corr()
    mask = np.triu(np.ones_like(correlation, dtype=bool))
    fig, ax = plt.subplots(figsize=(16,9))
    # Mod
    sns.heatmap(correlation, mask=mask, square=True, annot=True, fmt=".1f", linewidths=0.5)

    fig.savefig('heatmap.png')
    return fig
