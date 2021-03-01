import streamlit as st
import finanzInformatikDataPipe as fI
import cluster
import altair as alt

links, junk = fI.find_job_offers()

df = cluster.cluster_job_titles(junk)
st.set_page_config(layout="wide")

col1, col2 = st.beta_columns(2)
chart = alt.Chart(df).mark_bar().encode(
    x='Jobbezeichnung',
    y='offene Stellen',
    color=alt.Color('Jobbezeichnung', legend=alt.Legend(title="Bars by title"))
)

st.sidebar.text(
    "DISCLAIMER: Das ist ein Prototyp zum Thema 'Trendsanalyse durch \nWeb crawling'. Es ist gibt keine Garantie auf"
    "Richtigkeit der\nDaten. Das Design der Seite kann  sich ebenfalls jederzeit ändern")

with col1:
    st.subheader("Offene Stellen in Kategorien sortiert")
    st.altair_chart(chart, use_container_width=True)
    st.subheader("Offene Stellen in Kategorien sortiert")
    st.altair_chart(chart, use_container_width=True)

with col2:
    st.subheader("Offene Stellen in Kategorien sortiert")
    st.altair_chart(chart, use_container_width=True)

