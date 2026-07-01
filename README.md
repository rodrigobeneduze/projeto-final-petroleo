# 🛢️ Previsão do Preço do Petróleo Brent (FOB)

Projeto para Pós-Graduação em Data Analytics - FIAP.

---

# Objetivo

Desenvolver um modelo de Machine Learning capaz de prever o próximo preço diário do petróleo Brent (FOB), utilizando dados históricos disponibilizados pelo IPEA Data.

O projeto demonstra todas as etapas de um pipeline de Data Science, desde a preparação dos dados até a avaliação do modelo e disponibilização em uma aplicação web utilizando Streamlit.

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

# Autor

Rodrigo Beneduze

Pós-Graduação em Data Analytics

2026
