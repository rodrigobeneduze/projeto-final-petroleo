import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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

pred=modelo.predict(X_test)

mae=mean_absolute_error(y_test,pred)
rmse=np.sqrt(mean_squared_error(y_test,pred))
r2=r2_score(y_test,pred)

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

st.markdown('### 🗂️ Últimos registros')
st.dataframe(df[['Data','Preco']].tail(10),use_container_width=True)

graf=df.copy()
graf['MM30']=graf['Preco'].rolling(30).mean()

st.markdown('### 📉 Histórico do preço')
fig,ax=plt.subplots(figsize=(12,5))
ax.plot(graf['Data'],graf['Preco'],label='Preço')
ax.plot(graf['Data'],graf['MM30'],label='Média móvel 30 dias')
ax.grid(True)
ax.legend()
st.pyplot(fig)

st.markdown('### 🤖 Desempenho do Modelo')
m1,m2,m3=st.columns(3)
m1.metric('MAE',f'{mae:.2f}')
m2.metric('RMSE',f'{rmse:.2f}')
m3.metric('R²',f'{r2:.3f}')

csv=df.to_csv(index=False).encode('utf-8')
st.download_button('📥 Baixar base em CSV',csv,'base_petroleo.csv','text/csv')

st.divider()
st.caption('Projeto desenvolvido para a Pós-Graduação em Data Analytics | Python • Pandas • Scikit-Learn • Streamlit')
