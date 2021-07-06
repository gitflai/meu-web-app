import streamlit as st
import pandas as pd

st.image('bannerflai.jpg', use_column_width = 'always')
st.sidebar.image('bannerflai.jpg', use_column_width = 'always')

paginas = ['Home', 'Rascunhos', 'Gráfico']
pagina = st.sidebar.selectbox('Selecione a página que você deseja', paginas)

dados = pd.read_csv('prof-dados-resumido.csv')

if pagina == 'Home':
	st.markdown('# Meu Web App')

	

	st.write(dados)


if pagina == 'Rascunhos':

	st.latex('\int_a^bf(x)dx = F(b) - F(a)')

	st.code('''
		def Função(x)
			return x**2
		''')

	var = st.sidebar.selectbox('Selecione uma variável', ['Idade', 'Profissão'])
	ms = dados['Salário'].groupby(dados[var]).mean()
	st.table(ms)


if pagina == 'Gráfico':

	variaveis = dados.columns.tolist()

	var1 = st.selectbox('Selecione uma variável', variaveis)

	plot = dados['Salário'].groupby(dados[var1]).mean().plot(kind = 'barh')

	st.pyplot(plot.figure)









