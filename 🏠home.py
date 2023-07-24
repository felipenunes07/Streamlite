import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.write("# FIFA23 OFFICIAL DATASET! ⚽")

btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data?resource=download")

st.markdown("""
O conjurto de dados 
de jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre
jogadores de futebol profissonais. O conjunto de dados contém uma gama de atribtos, incluindo
dados demográficos do jogador,caracteristicas fisicas, estátisticas de jogo, detalhes do contrato e
afiliações de clubes.

Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para analistas de
futebol, pesquisadores entusiatas interessados em explorar vários aspectos do mundo do futebol, pois
permite estudar atributos de jogadores, métrias de desempenho,avaliação de mercado, analise de
clubes, posicionamento de jogadore e  desenvolvimento do jogador ao longo do tempo.
            
"""
)