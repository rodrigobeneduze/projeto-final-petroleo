import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

st.set_page_config(page_title='Previsão do Petróleo Brent', page_icon='🛢️', layout='wide')

st.title('🛢️ Previsão do Preço do Petróleo Brent (FOB)')
st.caption('Projeto Pós-Graduação em Data Analytics')

st.sidebar.header('📋 Sobre o Projeto')
st.sidebar.write('''Autor: Rodrigo Beneduze

Modelo: Random Forest Regressor

Fonte: IPEA Data

O modelo é treinado automaticamente a partir da base histórica.''')

@st.cache_data
def carregar():
    df = pd.read_excel('BASE.xlsx')
    df.columns=['Data','Preco']
    df['Data']=pd.to_datetime(df['Data'])
    return df.sort_values('Data')

df=carregar()

base=df.copy()
for i in range(1,6):
    base[f'Lag_{i}']=base['Preco'].shift(i)
base=base.dropna()

X=base[[f'Lag_{i}' for i in range(1,6)]]
y=base['Preco']

div=int(len(base)*0.8)
X_train,X_test=X.iloc[:div],X.iloc[div:]
y_train,y_test=y.iloc[:div],y.iloc[div:]

modelo=RandomForestRegressor(n_estimators=200,random_state=42)
modelo.fit(X_train,y_train)

pred = modelo.predict(X_test)

mae = mean_absolute_error(y_test,pred)
rmse = np.sqrt(mean_squared_error(y_test,pred))
r2 = r2_score(y_test,pred)

ultimos=base['Preco'].tail(5).tolist()
entrada=pd.DataFrame([{'Lag_1':ultimos[4],'Lag_2':ultimos[3],'Lag_3':ultimos[2],'Lag_4':ultimos[1],'Lag_5':ultimos[0]}])

previsao=float(modelo.predict(entrada)[0])
ultimo=float(base['Preco'].iloc[-1])
delta=previsao-ultimo

st.markdown('### 📊 Indicadores')
c1,c2,c3,c4=st.columns(4)
c1.metric('Último preço',f'US$ {ultimo:.2f}')
c2.metric('Previsão',f'US$ {previsao:.2f}',delta=f'{delta:.2f}')
c3.metric('MAE',f'{mae:.2f}')
c4.metric('R²',f'{r2:.3f}')

st.markdown('### 📈 Interpretação')
if delta>=0:
    st.success(f'O modelo estima alta de aproximadamente US$ {abs(delta):.2f}.')
else:
    st.warning(f'O modelo estima queda de aproximadamente US$ {abs(delta):.2f}.')

st.subheader("📊 Resumo Executivo")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Período",
        f"{df['Data'].min().year} - {df['Data'].max().year}"
    )

    st.metric(
        "Total de registros",
        f"{len(df):,}".replace(",", ".")
    )

with col2:
    st.metric(
        "Preço médio",
        f"US$ {df['Preco'].mean():.2f}"
    )

    st.metric(
        "Preço mínimo",
        f"US$ {df['Preco'].min():.2f}"
    )

with col3:
    st.metric(
        "Preço máximo",
        f"US$ {df['Preco'].max():.2f}"
    )

    st.metric(
        "Última atualização",
        df['Data'].max().strftime("%d/%m/%Y")
    )

st.markdown('### 🗂️ Últimos registros')
st.dataframe(df[['Data','Preco']].tail(10),use_container_width=True)

graf=df.copy()
graf['MM30']=graf['Preco'].rolling(30).mean()

st.subheader("📉 Histórico do preço")

fig = go.Figure()

# Série histórica
fig.add_trace(
    go.Scatter(
        x=df["Data"],
        y=df["Preco"],
        mode="lines",
        name="Preço",
        line=dict(width=2)
    )
)

# Média móvel
fig.add_trace(
    go.Scatter(
        x=df["Data"],
        y=df["Preco"].rolling(30).mean(),
        mode="lines",
        name="Média móvel (30 dias)",
        line=dict(dash="dash")
    )
)

# Último ponto
fig.add_trace(
    go.Scatter(
        x=[df["Data"].iloc[-1]],
        y=[df["Preco"].iloc[-1]],
        mode="markers",
        marker=dict(size=10),
        name="Último preço"
    )
)

fig.update_layout(
    title="Histórico do preço do Petróleo Brent",
    xaxis_title="Ano",
    yaxis_title="Preço (US$)",
    hovermode="x unified",
    template="plotly_white",
    height=550
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# Comparação entre valores reais e previstos
# ===============================

st.markdown("### 📊 Comparação: Valores Reais x Valores Previstos")

fig2, ax2 = plt.subplots(figsize=(12,5))

ax2.plot(
    y_test.values,
    label="Valor Real",
    linewidth=2
)

ax2.plot(
    pred,
    label="Previsão",
    linestyle="--",
    linewidth=2
)

ax2.set_xlabel("Observações")
ax2.set_ylabel("Preço (US$)")
ax2.grid(True)
ax2.legend()

st.pyplot(fig2)

st.subheader("🧠 Importância das Variáveis")

import plotly.express as px

importancia = pd.DataFrame({
    "Variável": X.columns,
    "Importância": modelo.feature_importances_
})

importancia = importancia.sort_values(
    "Importância",
    ascending=True
)

fig_importancia = px.bar(
    importancia,
    x="Importância",
    y="Variável",
    orientation="h",
    text="Importância",
    title="Contribuição de cada variável para a previsão"
)

fig_importancia.update_traces(
    texttemplate="%{text:.2%}",
    textposition="outside"
)

fig_importancia.update_layout(
    template="plotly_white",
    height=420
)

st.plotly_chart(fig_importancia, use_container_width=True)

variavel = importancia.iloc[-1]["Variável"]

st.info(
    f"""
A variável mais importante para o modelo foi **{variavel}**.

Isso indica que o preço observado mais recentemente exerce a maior influência
na previsão do próximo preço do petróleo Brent.
"""
)

st.markdown('### 🤖 Desempenho do Modelo')
m1,m2,m3=st.columns(3)
m1.metric('MAE',f'{mae:.2f}')
m2.metric('RMSE',f'{rmse:.2f}')
m3.metric('R²',f'{r2:.3f}')

csv=df.to_csv(index=False).encode('utf-8')
st.download_button('📥 Baixar base em CSV',csv,'base_petroleo.csv','text/csv')

st.divider()
st.caption('Projeto desenvolvido para a Pós-Graduação em Data Analytics | Python • Pandas • Scikit-Learn • Streamlit')
