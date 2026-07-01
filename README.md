<p align="center">
  <img src="banner.png" width="100%">
</p>

# 🛢️ Previsão do Preço do Petróleo Brent (FOB)

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-RandomForest-orange?logo=scikitlearn)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-blue?logo=plotly)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?logo=streamlit)
![License](https://img.shields.io/badge/Projeto-Acadêmico-success)

Projeto desenvolvido para a Pós-Graduação em Data Analytics - FIAP.

---

## 📊 Sobre o Projeto

Este projeto aplica técnicas de Machine Learning para prever o próximo preço diário do petróleo Brent (FOB) utilizando dados históricos disponibilizados pelo IPEA Data.

Foi desenvolvido como projeto final da Pós-Graduação em Data Analytics (FIAP), contemplando todas as etapas de um pipeline de Ciência de Dados:

- Coleta dos dados
- Tratamento
- Engenharia de atributos
- Treinamento do modelo
- Avaliação
- Deploy utilizando Streamlit

---

# Objetivo

Desenvolver um modelo de Machine Learning capaz de prever o próximo preço diário do petróleo Brent (FOB), utilizando dados históricos disponibilizados pelo IPEA Data.

O projeto demonstra todas as etapas de um pipeline de Data Science, desde a preparação dos dados até a avaliação do modelo e disponibilização em uma aplicação web utilizando Streamlit.

---

## 🚀 Demonstração

### Aplicação Online

👉 https://projeto-final-petroleo-etefgwugyj9u7zcapzeipe.streamlit.app/

O dashboard permite:

- visualizar o histórico completo do petróleo Brent;
- prever automaticamente o próximo preço;
- analisar indicadores do modelo;
- explorar gráficos interativos;
- verificar a importância das variáveis;
- baixar a base utilizada.

---

# Fonte dos dados

IPEA Data

Histórico diário do preço do petróleo Brent (FOB).

Período analisado:

**1987 a 2026**

---

# Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Scikit-Learn
- Random Forest Regressor
- Plotly
- Matplotlib
- Streamlit
- GitHub

---

# Pipeline do Projeto

1. Coleta dos dados
2. Tratamento
3. Engenharia de atributos (Lag_1 até Lag_5)
4. Treinamento do modelo
5. Avaliação
6. Previsão do próximo preço

---

# Indicadores obtidos

| Indicador | Resultado |
|-----------|-----------|
| MAE | 1.46 |
| RMSE | 2.17 |
| R² | 0.986 |

---

# Principais funcionalidades

✅ Dashboard interativo

✅ KPIs executivos

✅ Previsão automática

✅ Comparação entre valores reais e previstos

✅ Histórico completo do petróleo

✅ Média móvel de 30 dias

✅ Importância das variáveis

✅ Interpretação automática do modelo

✅ Download da base em CSV

---

# Estrutura do projeto

```
Projeto_Final_Petroleo.ipynb

app.py

BASE.xlsx

requirements.txt

README.md
```

---

# Como executar localmente

Clone o repositório

```
git clone https://github.com/rodrigobeneduze/projeto-final-petroleo.git
```

Instale as dependências

```
pip install -r requirements.txt
```

Execute

```
streamlit run app.py
```

---

# Aplicação Online

Disponível em:

https://projeto-final-petroleo-etefgwugyj9u7zcapzeipe.streamlit.app/

---

# 📌 Considerações Finais
Os resultados demonstram que o modelo Random Forest apresentou elevada capacidade preditiva (R² = 0,986), explicando aproximadamente 98,6% da variabilidade dos preços históricos do petróleo Brent. O baixo MAE e RMSE evidenciam a precisão das previsões, tornando o modelo adequado como ferramenta de apoio à tomada de decisão. Entretanto, fatores externos, como eventos geopolíticos, decisões da OPEP e oscilações econômicas globais, não são considerados pelo algoritmo e podem influenciar significativamente o comportamento futuro dos preços.

---

# Autor

Rodrigo Beneduze

Pós-Graduação em Data Analytics

2026
