import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

st.set_page_config(
    page_title="Previsão do Petróleo Brent",
    page_icon="🛢️",
    layout="wide"
)

st.title("🛢️ Previsão do Preço do Petróleo Brent (FOB)")

st.markdown("""
Aplicação desenvolvida como projeto final da Pós-Graduação em Data Analytics.

O modelo utiliza **Random Forest Regressor** para estimar o próximo preço do petróleo Brent com base nos cinco últimos preços observados.
""")



df = pd.read_excel("BASE.xlsx")
df.columns = ["Data", "Preco"]
df = df.sort_values("Data")

# Criando as variáveis de atraso (lags)

df["Lag_1"] = df["Preco"].shift(1)
df["Lag_2"] = df["Preco"].shift(2)
df["Lag_3"] = df["Preco"].shift(3)
df["Lag_4"] = df["Preco"].shift(4)
df["Lag_5"] = df["Preco"].shift(5)

df = df.dropna()

# Treinando o modelo

from sklearn.ensemble import RandomForestRegressor

X = df[["Lag_1","Lag_2","Lag_3","Lag_4","Lag_5"]]
y = df["Preco"]

modelo = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

modelo.fit(X, y)

st.subheader("Últimos registros")

st.dataframe(df.tail())

ultimo_preco = df["Preco"].iloc[-1]

st.metric(
    label="Último preço registrado",
    value=f"US$ {ultimo_preco:.2f}"
)

ultimos = df["Preco"].tail(5).tolist()

entrada = pd.DataFrame([{
    "Lag_1": ultimos[4],
    "Lag_2": ultimos[3],
    "Lag_3": ultimos[2],
    "Lag_4": ultimos[1],
    "Lag_5": ultimos[0]
}])

previsao = modelo.predict(entrada)[0]

st.metric(
    label="Próxima previsão",
    value=f"US$ {previsao:.2f}"
)

st.subheader("Histórico do preço")

fig, ax = plt.subplots(figsize=(12,5))

ax.plot(df["Data"], df["Preco"], color="blue")

ax.set_xlabel("Ano")
ax.set_ylabel("Preço (US$)")
ax.grid(True)

st.pyplot(fig)