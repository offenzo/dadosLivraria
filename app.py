import streamlit as st
import pandas as pd
import plotly.express as px
import os

#configura a pagina
st.set_page_config(page_title="DashBoard Interativo", layout="wide")

st.title("DashBoard de Livros de Ficção Científica")

#dados
df = pd.read_csv("dados_extraidos.csv")

@st.cache_data
def importarDados():
    if os.path.exists("dados_extraidos.csv"):
        return pd.read_csv("dados_extraidos.csv")
    else:
        return pd.DataFrame(columns=["Título", "Preço", "Disponibilidade"])

df = importarDados()

# ADICIONADO: Função para traduzir disponibilidade para português
def traduzir_disponibilidade(disponibilidade):
    traducoes = {
        "In stock": "Em Estoque",
        "Out of stock": "Fora de Estoque"
    }
    return traducoes.get(disponibilidade, disponibilidade)

if st.sidebar.button("Atualizar Dados"):
    st.cache_data.clear()

if df.empty:
    st.warning("Nenhum dado encontrado.")
else:
    opcoesUnicas = df["Disponibilidade"].dropna().unique() 
    categoriaSelecionada = st.sidebar.multiselect(
        "Selecione a disponibilidade para filtrar",
        options = opcoesUnicas,
        default = opcoesUnicas
    )

    dfFiltrado = df[df["Disponibilidade"].astype(str).isin(categoriaSelecionada)].copy()
    dfFiltrado["Preço_Numérico"] = dfFiltrado["Preço"].str.replace("£", "").astype(float)
    
    st.subheader("Estatísticas Gerais")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total de Livros", len(dfFiltrado))
    with col2:
        st.metric("Preço Médio", f"£{dfFiltrado['Preço_Numérico'].mean():.2f}")
    with col3:
        st.metric("Preço Mínimo", f"£{dfFiltrado['Preço_Numérico'].min():.2f}")
    with col4:
        st.metric("Preço Máximo", f"£{dfFiltrado['Preço_Numérico'].max():.2f}")
    
    st.subheader("Preços médios dos livros disponiveis")
    dfGrafico = dfFiltrado.groupby("Disponibilidade")["Preço_Numérico"].agg(["mean", "count"]).reset_index()
    dfGrafico.columns = ["Disponibilidade", "Preço_Médio", "Quantidade"]
    dfGrafico["Disponibilidade"] = dfGrafico["Disponibilidade"].apply(traduzir_disponibilidade)
    
    fig = px.bar(dfGrafico, x="Disponibilidade", y="Preço_Médio", 
                 color="Disponibilidade",
                 labels={"Preço_Médio": "Preço Médio (£)"})
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Catálogo de Livros")
    dfExibicao = dfFiltrado[["Título", "Preço", "Disponibilidade"]].copy()
    dfExibicao["Disponibilidade"] = dfExibicao["Disponibilidade"].apply(traduzir_disponibilidade)
    dfExibicao = dfExibicao.sort_values("Preço", key=lambda x: x.str.replace("£", "").astype(float), ascending=False)
    
    st.dataframe(dfExibicao, use_container_width=True, hide_index=True)
