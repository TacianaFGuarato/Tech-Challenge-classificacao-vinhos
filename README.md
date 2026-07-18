# Classificação da Qualidade de Vinhos

## Descrição

Este projeto tem como objetivo desenvolver e comparar modelos de aprendizado de máquina para a classificação da qualidade de vinhos. Foram avaliados três algoritmos de classificação (**KNN**, **Regressão Logística** e **Random Forest**) utilizando diferentes conjuntos de variáveis, com o objetivo de identificar a abordagem que apresenta o melhor desempenho na distinção entre vinhos de alta e baixa qualidade.

O projeto contempla todas as etapas de um fluxo de Machine Learning, desde o pré-processamento dos dados até a avaliação dos modelos por meio de métricas de desempenho e curvas ROC.

---

## Base de Dados

O conjunto de dados utilizado foi o **WineQT**, composto por características físico-químicas dos vinhos e sua respectiva classificação de qualidade.

### Variáveis utilizadas

* Fixed Acidity
* Volatile Acidity
* Citric Acid
* Residual Sugar
* Chlorides
* Free Sulfur Dioxide
* Total Sulfur Dioxide
* Density
* pH
* Sulphates
* Alcohol

A variável alvo foi transformada em uma classificação binária:

* **0** → Vinhos com qualidade inferior a 7.
* **1** → Vinhos com qualidade maior ou igual a 7.

---

## Estrutura do Projeto

```text
├── data/
│   └── WineQT.csv
│
├── notebooks/
│   └── Classificacao_Vinhos.ipynb
│
├── src/
│   ├── preprocessamento.py
│   └── modelagem.py
│
├── results/
│
├── requirements.txt
└── README.md
```

---

## Pré-processamento

As seguintes etapas foram realizadas:

* Leitura da base de dados;
* Remoção da coluna **Id**;
* Criação da variável alvo **quality_bin**;
* Separação entre variáveis preditoras e variável alvo;
* Divisão dos dados em treino e teste;
* Balanceamento da classe minoritária utilizando **SMOTE**;
* Padronização das variáveis utilizando **StandardScaler**.

---

## Modelos Avaliados

Foram treinados e comparados três algoritmos de classificação:

* K-Nearest Neighbors (KNN)
* Regressão Logística
* Random Forest

Cada algoritmo foi avaliado em quatro conjuntos de variáveis:

* **All** – Todas as variáveis.
* **Top 4** – Quatro variáveis mais relevantes.
* **Top 7** – Sete variáveis mais relevantes.
* **Alcohol** – Variáveis relacionadas ao álcool.

---

## Métricas de Avaliação

O desempenho dos modelos foi avaliado utilizando:

* Accuracy
* Precision
* Recall
* F1-score
* Matriz de Confusão
* Curva ROC
* Área sob a Curva (AUC)

---

## Principais Resultados

* O **Random Forest** apresentou o melhor desempenho entre os modelos avaliados.
* O conjunto **Top 4** obteve os melhores resultados gerais.
* Melhor Accuracy: **84,55%**.
* Melhor F1-score: **0,5138**.
* Melhor AUC: **0,835** (conjunto Top 4).

Os resultados demonstram que um conjunto reduzido das variáveis mais relevantes foi suficiente para obter um desempenho semelhante — e, em alguns casos, superior — ao modelo treinado com todas as variáveis.

---

## Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Imbalanced-learn (SMOTE)

---

## Autora

**Taciana**

Projeto desenvolvido para estudo e comparação de modelos de Machine Learning aplicados à classificação da qualidade de vinhos, abrangendo as etapas de pré-processamento, treinamento, avaliação e interpretação dos resultados.
