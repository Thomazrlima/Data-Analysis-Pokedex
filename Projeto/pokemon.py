# -*- coding: utf-8 -*-
"""Pokemon.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yf4zHngk9usPhGI4vgbX1ZDEK_SLDNfa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from google.colab import files
scaler = StandardScaler()

uploaded = files.upload()

leitura = pd.read_csv('pokemon_combined.csv')
leitura.head(3)

leitura[['Type1', 'Type2']] = leitura['Type'].str.split(' ', n=1, expand=True)
leitura[['Male', 'Female']] = leitura['Gender'].str.split(',', n=1, expand=True)
leitura[['Male', "Male_Drop"]] = leitura ['Male'].str.split("m", n=0, expand=True)
leitura[['Female', "Female_Drop"]] = leitura ['Female'].str.split("f", n=0, expand=True)
leitura.drop(columns=['Gender', 'Male_Drop', 'Female_Drop'], inplace=True)

col = leitura.pop('Type1')
leitura.insert(2, 'Type1', col)

col = leitura.pop('Type2')
leitura.insert(3, 'Type2', col)

col = leitura.pop('Male')
leitura.insert(5, 'Male', col)

col = leitura.pop('Female')
leitura.insert(6, 'Female', col)

encoder = LabelEncoder()
leitura['Type_Encoder'] = encoder.fit_transform(leitura['Type'])

leitura['Female'].fillna("Genderless", inplace=True)
leitura.head(3)

scaler = StandardScaler()
scaler.fit(leitura[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']])
normal = scaler.transform(leitura[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']])
normalpadrao = pd.DataFrame(normal, columns=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
print(normalpadrao.head())

#Box plot

def plot_boxplot_attack_by_type(df):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='Type1', y='Attack', palette='pastel')
    plt.title('Distribuição do Ataque por Tipo de Pokémon', fontsize=16, weight='bold')
    plt.xlabel('Tipo', fontsize=14)
    plt.ylabel('Ataque', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

plot_boxplot_attack_by_type(leitura)

def plot_boxplot_defense_by_type(df):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='Type1', y='Defense', palette='pastel')
    plt.title('Distribuição da Defesa por Tipo de Pokémon', fontsize=16, weight='bold')
    plt.xlabel('Tipo', fontsize=14)
    plt.ylabel('Defesa', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

plot_boxplot_defense_by_type(leitura)

def plot_boxplot_defense_by_type(df):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='Type1', y='Speed', palette='pastel')
    plt.title('Distribuição da Velocidade por Tipo de Pokémon', fontsize=16, weight='bold')
    plt.xlabel('Tipo', fontsize=14)
    plt.ylabel('Velocidade', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

plot_boxplot_defense_by_type(leitura)

def plot_boxplot_defense_by_type(df):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='Type1', y='Sp. Atk', palette='pastel')
    plt.title('Distribuição do Ataque Especial por Tipo de Pokémon', fontsize=16, weight='bold')
    plt.xlabel('Tipo', fontsize=14)
    plt.ylabel('Ataque Especial', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

plot_boxplot_defense_by_type(leitura)

def plot_boxplot_defense_by_type(df):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='Type1', y='Sp. Def', palette='pastel')
    plt.title('Distribuição da Defesa Especial por Tipo de Pokémon', fontsize=16, weight='bold')
    plt.xlabel('Tipo', fontsize=14)
    plt.ylabel('Defesa Especial', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

plot_boxplot_defense_by_type(leitura)

from scipy.interpolate import make_interp_spline
import numpy as np

def plot_histogram_with_trend(df):
    type_counts = df['Type1'].value_counts().add(df['Type2'].value_counts(), fill_value=0)
    type_counts = type_counts.sort_index()

    x = np.arange(len(type_counts))
    y = type_counts.values

    x_smooth = np.linspace(x.min(), x.max(), 500)
    y_smooth = make_interp_spline(x, y)(x_smooth)

    plt.figure(figsize=(12, 6))
    colors = plt.cm.get_cmap('Pastel1', len(type_counts))
    bars = plt.bar(type_counts.index, y, color=[colors(i) for i in range(len(type_counts))], edgecolor='black', alpha=0.8)

    plt.plot(x_smooth, y_smooth, color='red', linestyle='--', linewidth=2, label='Curva de Tendência')

    plt.title('Distribuição dos Tipos de Pokémon com Tendência', fontsize=16, weight='bold')
    plt.xlabel('Tipo', fontsize=14)
    plt.ylabel('Frequência', fontsize=14)
    plt.xticks(rotation=45, ticks=x, labels=type_counts.index)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

plot_histogram_with_trend(leitura)

from scipy.interpolate import interp1d
import numpy as np

male_value = []
female_value = []
genderless_value = []

for index, row in leitura.iterrows():
    if row['Male'] != 'Genderless':
        male_value.append(float(row['Male'].split('%')[0]))
        female_value.append(float(row['Female'].split('%')[0]))
    else:
        genderless_value.append(100)

male_value = sum(male_value) / 101400
female_value = sum(female_value) / 101400
genderless_value = sum(genderless_value) / 101400

grafico = [100 * male_value, 100 * female_value, 100 * genderless_value]
labels = ['Macho', 'Fêmea', 'Sem Gênero']

plt.figure(figsize=(8, 6))

bars = plt.bar(labels, grafico, color=['#1f77b4', '#ff7f0e', '#2ca02c'])

x = np.arange(len(grafico))
x_smooth = np.linspace(x.min(), x.max(), 500)

linear_interp = interp1d(x, grafico, kind='linear')
y_smooth = linear_interp(x_smooth)

plt.plot(x_smooth, y_smooth, color='red', linestyle='--', linewidth=2, label='Curva de Tendência')

plt.title('Distribuição Percentual de Gênero com Tendência', fontsize=16, weight='bold')
plt.xlabel('Gênero', fontsize=14)
plt.ylabel('Valor Médio (%)', fontsize=14)
plt.legend()
plt.tight_layout()

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:.2f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.show()

leitura['Male'] = leitura['Male'].replace('Genderless', np.nan)

leitura['Male'] = leitura['Male'].apply(lambda x: float(str(x).replace('%', '')) / 100 if isinstance(x, str) else x)

leitura['Female'] = leitura['Female'].replace('Genderless', np.nan)
leitura['Female'] = leitura['Female'].apply(lambda x: float(str(x).replace('%', '')) / 100 if isinstance(x, str) else x)

type_gender_distribution = leitura.groupby('Type1')[['Male', 'Female']].mean()

type_gender_distribution = type_gender_distribution.sort_values(by='Male', ascending=False)

plt.figure(figsize=(14, 8))

plt.barh(type_gender_distribution.index, -type_gender_distribution['Male'], color='skyblue', edgecolor='black', label='Masculino')

plt.barh(type_gender_distribution.index, type_gender_distribution['Female'], color='salmon', edgecolor='black', label='Feminino')

for index, value in enumerate(type_gender_distribution['Male']):
    plt.text(-value, index, f'{value*100:.1f}%', va='center', ha='right', color='black', fontsize=12, fontweight='bold')

for index, value in enumerate(type_gender_distribution['Female']):
    plt.text(value, index, f'{value*100:.1f}%', va='center', ha='left', color='black', fontsize=12, fontweight='bold')

plt.title('Distribuição Masculina e Feminina de Pokémon por Tipo', fontsize=18, weight='bold')
plt.xlabel('Proporção de Pokémon (%)', fontsize=14)
plt.ylabel('Tipo de Pokémon', fontsize=14)

plt.legend(title='Sexo', loc='upper left', fontsize=12, title_fontsize=14, borderpad=1.5, labelspacing=1.5, bbox_to_anchor=(1, 1))
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()

plt.show()

def plot_histogram_attack(df, bins=20):
    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.hist(df['Attack'], bins=bins, color='#F7F744', edgecolor='black', alpha=0.7)
    ax1.set_title('Distribuição da Ataque dos Pokémon', fontsize=16, weight='bold')
    ax1.set_xlabel('Ataque', fontsize=14)
    ax1.set_ylabel('Frequência', fontsize=14)
    ax1.grid(axis='y', linestyle='--', alpha=0.7)

    ax2 = ax1.twinx()
    sns.kdeplot(df['Attack'], color='blue', linestyle='--', linewidth=2, ax=ax2)
    ax2.grid(False)

    plt.tight_layout()
    plt.show()

plot_histogram_attack(leitura)

def plot_histogram_sp_attack(df, bins=20):
    plt.figure(figsize=(12, 6))
    plt.hist(df['Sp. Atk'], bins=bins, color='#8B0000', edgecolor='black', alpha=0.7)
    plt.title('Distribuição do ataque especial dos Pokémon', fontsize=16, weight='bold')
    plt.xlabel('Ataque especial', fontsize=14)
    plt.ylabel('Frequência', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

plot_histogram_sp_attack(leitura)

def plot_histogram_defense(df, bins=20):
    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.hist(df['Defense'], bins=bins, color='#8B0000', edgecolor='black', alpha=0.7)
    ax1.set_title('Distribuição da Defesa dos Pokémon', fontsize=16, weight='bold')
    ax1.set_xlabel('Defesa', fontsize=14)
    ax1.set_ylabel('Frequência', fontsize=14)
    ax1.grid(axis='y', linestyle='--', alpha=0.7)

    ax2 = ax1.twinx()
    sns.kdeplot(df['Defense'], color='red', linestyle='--', linewidth=2, ax=ax2)
    ax2.grid(False)

    plt.tight_layout()
    plt.show()

plot_histogram_defense(leitura)

def plot_histogram_speed(df, bins=20):
    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.hist(df['Speed'], bins=bins, color='#F7C4CC', edgecolor='black', alpha=0.7)
    ax1.set_title('Distribuição da Velocidade dos Pokémon', fontsize=16, weight='bold')
    ax1.set_xlabel('Velocidade', fontsize=14)
    ax1.set_ylabel('Frequência', fontsize=14)
    ax1.grid(axis='y', linestyle='--', alpha=0.7)

    ax2 = ax1.twinx()
    sns.kdeplot(df['Speed'], color='red', linestyle='--', linewidth=2, ax=ax2)
    ax2.grid(False)

    plt.tight_layout()
    plt.show()

plot_histogram_speed(leitura)

#Scatter plot
import matplotlib.pyplot as plt

def plot_scatter_attack_defense(df):
    plt.figure(figsize=(12, 6))

    plt.scatter(df['Attack'], df['Defense'], color='skyblue', alpha=0.7, edgecolor='black')

    plt.title('Relação entre Ataque e Defesa dos Pokémon', fontsize=16, weight='bold')
    plt.xlabel('Ataque', fontsize=14)
    plt.ylabel('Defesa', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)

    z = np.polyfit(df['Attack'], df['Defense'], 1)
    p = np.poly1d(z)
    plt.plot(df['Attack'], p(df['Attack']), color='red', linestyle='--', linewidth=2, label='Linha de Tendência')

    plt.legend()
    plt.tight_layout()
    plt.show()

plot_scatter_attack_defense(leitura)

import matplotlib.pyplot as plt

def plot_scatter_defense_spdef(df):
    plt.figure(figsize=(12, 6))

    plt.scatter(df['Defense'], df['Sp. Def'], color='lightcoral', alpha=0.7, edgecolor='black')

    plt.title('Relação entre Defesa e Defesa Especial dos Pokémon', fontsize=16, weight='bold')
    plt.xlabel('Defesa', fontsize=14)
    plt.ylabel('Defesa Especial', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)

    z = np.polyfit(df['Defense'], df['Sp. Def'], 1)
    p = np.poly1d(z)
    plt.plot(df['Defense'], p(df['Defense']), color='red', linestyle='--', linewidth=2, label='Linha de Tendência')

    plt.legend()
    plt.tight_layout()
    plt.show()

plot_scatter_defense_spdef(leitura)

def plot_scatter_height_weight(df):
    df_filtered = df[(df['Height'] != df['Height'].max()) &
                     (df['Height'] != df['Height'].min()) &
                     (df['Weight'] != df['Weight'].max()) &
                     (df['Weight'] != df['Weight'].min())]

    plt.figure(figsize=(12, 6))

    plt.scatter(df_filtered['Height'], df_filtered['Weight'], color='lightgreen', alpha=0.7, edgecolor='black')

    plt.title('Relação entre Altura e Peso dos Pokémon', fontsize=16, weight='bold')
    plt.xlabel('Altura (m)', fontsize=14)
    plt.ylabel('Peso (kg)', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)

    z = np.polyfit(df_filtered['Height'], df_filtered['Weight'], 1)
    p = np.poly1d(z)
    plt.plot(df_filtered['Height'], p(df_filtered['Height']), color='red', linestyle='--', linewidth=2, label='Linha de Tendência')

    plt.legend()
    plt.tight_layout()
    plt.show()

plot_scatter_height_weight(leitura)

def plot_scatter_height_weight(df):
    plt.figure(figsize=(12, 6))

    plt.scatter(df['Sp. Atk'], df['Sp. Def'], color='yellow', alpha=0.7, edgecolor='black')

    plt.title('Relação entre Ataque Especial e Defesa Especial', fontsize=16, weight='bold')
    plt.xlabel('Ataque Especial', fontsize=14)
    plt.ylabel('Defesa Especial', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)

    z = np.polyfit(df['Sp. Atk'], df['Sp. Def'], 1)
    p = np.poly1d(z)
    plt.plot(df['Sp. Atk'], p(df['Sp. Atk']), color='red', linestyle='--', linewidth=2, label='Linha de Tendência')

    plt.legend()
    plt.tight_layout()
    plt.show()

plot_scatter_height_weight(leitura)

def plot_scatter_height_weight(df):
    plt.figure(figsize=(12, 6))

    plt.scatter(df['Speed'], df['Weight'], color='lightpink', alpha=0.7, edgecolor='black')

    plt.title('Relação entre Velocidade e Peso', fontsize=16, weight='bold')
    plt.xlabel('Velocidade', fontsize=14)
    plt.ylabel('Peso (kg)', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)

    z = np.polyfit(df['Speed'], df['Weight'], 1)
    p = np.poly1d(z)
    plt.plot(df['Speed'], p(df['Speed']), color='red', linestyle='--', linewidth=2, label='Linha de Tendência')

    plt.legend()
    plt.tight_layout()
    plt.show()

plot_scatter_height_weight(leitura)

#Mapa de calor

cmap = sns.light_palette("#A3C1DA", as_cmap=True)
cmap_r = sns.light_palette("#E39D9D", as_cmap=True)

plt.rcParams.update({
    'axes.facecolor': '#F0F0F0',
    'axes.edgecolor': '#E0E0E0',
    'grid.color': '#D0D0D0',
    'grid.linestyle': '--',
})

def plot_box_plots(df, cols):
    fig, axes = plt.subplots(1, len(cols), figsize=(14, 6), sharex=False)
    fig.suptitle("Box Plots das Variáveis Selecionadas", fontsize=16, weight='bold', color='#333333')

    for ax, col in zip(axes, cols):
        sns.boxplot(data=df, y=col, ax=ax, color="#A3C1DA")
        ax.set_title(col, fontsize=12, weight='semibold', color='#333333')
        ax.set_ylabel('')
        ax.tick_params(axis='y', labelsize=10)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

def plot_histograms(df, cols, bins=10):
    fig, axes = plt.subplots(2, len(cols) // 2, figsize=(14, 8))
    fig.suptitle("Histogramas das Variáveis Selecionadas", fontsize=16, weight='bold', color='#333333')

    for ax, col in zip(axes.flat, cols):
        ax.hist(df[col].dropna(), bins=bins, color='#E39D9D', edgecolor='black', alpha=0.7)
        ax.set_title(col, fontsize=12, weight='semibold', color='#333333')
        ax.set_xlabel('Valor')
        ax.set_ylabel('Frequência')
        ax.grid(False)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

def plot_scatter_plots(df, target_col, cols):
    num_cols = len(cols)
    fig, axes = plt.subplots(1, num_cols, figsize=(5 * num_cols, 5))
    fig.suptitle(f'Scatter Plots em relação a {target_col}', fontsize=16, weight='bold', color='#333333')

    for ax, col in zip(axes, cols):
        sns.scatterplot(data=df, x=col, y=target_col, ax=ax, s=40, color='#A3C1DA', edgecolor='black', alpha=0.7)
        ax.set_title(f'{col} vs {target_col}', fontsize=12, weight='semibold', color='#333333')
        ax.set_xlabel(col)
        ax.set_ylabel(target_col)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

def plot_heatmap(df, categoria1, categoria2):
    corr = pd.crosstab(df[categoria1], df[categoria2])

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt="d", cmap=sns.diverging_palette(220, 20, as_cmap=True), linewidths=0.5, cbar_kws={'label': 'Frequência'})
    plt.title(f'Heatmap: {categoria1} vs {categoria2}', fontsize=16, weight='bold', color='#333333')
    plt.xlabel(categoria2)
    plt.ylabel(categoria1)

    plt.show()

plot_heatmap(leitura, 'Type1', 'Type2')

np.random.seed(42)
leitura = pd.DataFrame({
    'Height': np.random.normal(loc=170, scale=10, size=1000),
    'Weight': np.random.normal(loc=65, scale=15, size=1000)
})

leitura['Height_Normalized'] = (leitura['Height'] - leitura['Height'].mean()) / leitura['Height'].std()
leitura['Weight_Normalized'] = (leitura['Weight'] - leitura['Weight'].mean()) / leitura['Weight'].std()

print(leitura.head())

#Distribuições Amostrais

from scipy.stats import norm

def calcular_medias_amostrais(data, colunas, tamanho_amostra, num_amostras):
    medias_amostrais = {col: [] for col in colunas}

    for _ in range(num_amostras):
        amostra = data.sample(n=tamanho_amostra, replace=False)
        for col in colunas:
            medias_amostrais[col].append(np.mean(amostra[col]))

    return medias_amostrais

colunas = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
tamanhos_amostras = [5, 50, 200]
num_amostras = 1000

distribuicoes_amostrais = {}

for tamanho in tamanhos_amostras:
    medias_amostrais = calcular_medias_amostrais(normalpadrao, colunas, tamanho, num_amostras)
    distribuicoes_amostrais[tamanho] = medias_amostrais

plt.style.use('ggplot')
fig, axes = plt.subplots(len(colunas), len(tamanhos_amostras), figsize=(18, 12))
fig.suptitle('Distribuição das Médias Amostrais com Curva Normal', fontsize=16, weight='bold')

for i, col in enumerate(colunas):
    for j, tamanho in enumerate(tamanhos_amostras):
        dados = distribuicoes_amostrais[tamanho][col]
        media = np.mean(dados)
        desvio_padrao = np.std(dados)

        axes[i, j].hist(dados, bins=30, color='#4C72B0', edgecolor='black', alpha=0.7, density=True)

        xmin, xmax = axes[i, j].get_xlim()
        x = np.linspace(xmin, xmax, 100)
        y = norm.pdf(x, media, desvio_padrao)
        axes[i, j].plot(x, y, color='#E24A33', linewidth=2.5, linestyle='--')

        axes[i, j].set_title(f'{col} - Amostra: {tamanho}', fontsize=12, weight='semibold', color='#333333')
        axes[i, j].set_xlabel('Média da Amostra', fontsize=10)
        axes[i, j].set_ylabel('Densidade', fontsize=10)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

np.random.seed(42)
populacao = np.random.normal(loc=50, scale=10, size=1000)

def calcular_medias_amostrais(populacao, tamanho_amostra, num_amostras):
    medias_amostrais = []
    for _ in range(num_amostras):
        amostra = np.random.choice(populacao, size=tamanho_amostra, replace=False)
        medias_amostrais.append(np.mean(amostra))
    return medias_amostrais

tamanhos_amostras = [5, 30, 100]
num_amostras = 1000

leitura = pd.DataFrame({'Height': np.random.normal(loc=5, scale=1.5, size=1000)})

plt.figure(figsize=(22, 12))

mu, sigma = leitura['Height'].mean(), leitura['Height'].std()

for i, tamanho in enumerate(tamanhos_amostras):
    medias_amostrais = calcular_medias_amostrais(leitura['Height'], tamanho, num_amostras)
    plt.subplot(1, len(tamanhos_amostras), i + 1)

    plt.hist(medias_amostrais, bins=40, color='skyblue', edgecolor='black', alpha=0.7, density=True)

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, sigma / np.sqrt(tamanho))
    plt.plot(x, p, 'r--', linewidth=2, label='Distribuição Normal')

    plt.title(f'Distribuição Amostral da Média\n(Tamanho da Amostra = {tamanho})', fontsize=16, pad=20)
    plt.xlabel('Média da Amostra de Altura dos Pokémon (em metros)', fontsize=14)
    plt.ylabel('Densidade', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()

plt.tight_layout()
plt.show()

np.random.seed(42)
populacao_weight = np.random.normal(loc=60, scale=15, size=1000)

def calcular_medias_amostrais(populacao, tamanho_amostra, num_amostras):
    medias_amostrais = []
    for _ in range(num_amostras):
        amostra = np.random.choice(populacao, size=tamanho_amostra, replace=False)
        medias_amostrais.append(np.mean(amostra))
    return medias_amostrais

tamanhos_amostras = [5, 30, 100]
num_amostras = 1000

leitura = pd.DataFrame({
    'Weight': populacao_weight
})

def plot_distribuicoes_amostrais_peso(leitura, tamanhos_amostras, num_amostras):
    plt.figure(figsize=(18, 12))

    mu, sigma = populacao_weight.mean(), populacao_weight.std()

    for i, tamanho in enumerate(tamanhos_amostras):
        medias_amostrais = calcular_medias_amostrais(leitura['Weight'], tamanho, num_amostras)
        plt.subplot(1, len(tamanhos_amostras), i + 1)

        plt.hist(medias_amostrais, bins=30, color='skyblue', edgecolor='black', alpha=0.7, density=True)

        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, sigma / np.sqrt(tamanho))
        plt.plot(x, p, 'r--', linewidth=2, label='Distribuição Normal')

        plt.title(f'Distribuição Amostral da Média do Peso\n(Tamanho da Amostra = {tamanho})', fontsize=16, pad=20)
        plt.xlabel('Média da Amostra de Peso (kg)', fontsize=14)
        plt.ylabel('Densidade', fontsize=14)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend()

    plt.tight_layout()
    plt.show()

plot_distribuicoes_amostrais_peso(leitura, tamanhos_amostras, num_amostras)

np.random.seed(42)
populacao_hp = np.random.normal(loc=70, scale=20, size=1000)

leitura = pd.DataFrame({
    'HP': populacao_hp
})

def calcular_medias_amostrais(populacao, tamanho_amostra, num_amostras):
    medias_amostrais = []
    for _ in range(num_amostras):
        amostra = np.random.choice(populacao, size=tamanho_amostra, replace=False)
        medias_amostrais.append(np.mean(amostra))
    return medias_amostrais

tamanhos_amostras = [5, 30, 100]
num_amostras = 1000

def plot_distribuicoes_amostrais_hp(leitura, tamanhos_amostras, num_amostras):
    plt.figure(figsize=(18, 12))

    mu, sigma = populacao_hp.mean(), populacao_hp.std()

    for i, tamanho in enumerate(tamanhos_amostras):
        medias_amostrais = calcular_medias_amostrais(leitura['HP'], tamanho, num_amostras)

        plt.subplot(1, len(tamanhos_amostras), i + 1)
        plt.hist(medias_amostrais, bins=30, color='skyblue', edgecolor='black', alpha=0.7, density=True)

        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, sigma / np.sqrt(tamanho))
        plt.plot(x, p, 'r--', linewidth=2, label='Distribuição Normal')

        plt.title(f'Distribuição Amostral da Média de HP\n(Tamanho da Amostra = {tamanho})', fontsize=16, pad=20)
        plt.xlabel('Média da Amostra de HP', fontsize=14)
        plt.ylabel('Densidade', fontsize=14)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend()

    plt.tight_layout()
    plt.show()

plot_distribuicoes_amostrais_hp(leitura, tamanhos_amostras, num_amostras)

altura = leitura['Height'].astype(float).values

Q3 = np.percentile(altura, 75)
IQR = Q3 - Q1

limite_inferior = Q1 - 3.0 * IQR
limite_superior = Q3 + 3.0 * IQR

altura_filtrada = altura[(altura >= limite_inferior) & (altura <= limite_superior)]

media_amostra = np.mean(altura_filtrada)
desvio_padrao_amostra = np.std(altura_filtrada, ddof=1)
n = len(altura_filtrada)

confianca_90 = 0.90
confianca_95 = 0.95

z_90 = stats.norm.ppf(1 - (1 - confianca_90) / 2)
z_95 = stats.norm.ppf(1 - (1 - confianca_95) / 2)

erro_padrao = desvio_padrao_amostra / np.sqrt(n)

IC_90 = (media_amostra - z_90 * erro_padrao, media_amostra + z_90 * erro_padrao)
IC_95 = (media_amostra - z_95 * erro_padrao, media_amostra + z_95 * erro_padrao)

print(f"Média da amostra (altura filtrada): {media_amostra:.2f} m")
print(f"Desvio padrão da amostra: {desvio_padrao_amostra:.2f} m")
print(f"Intervalo de Confiança de 90%: {IC_90[0]:.2f} m a {IC_90[1]:.2f} m")
print(f"Intervalo de Confiança de 95%: {IC_95[0]:.2f} m a {IC_95[1]:.2f} m")