import streamlit as st
import finanzInformatikDataPipe as fI
import cluster
import altair as alt

# Init data from Data Pipelines
junk = fI.find_job_offers()
bar_chart_df = cluster.get_clustered_job_titles(junk)
line_chart_df = cluster.get_jobamount_over_time(junk)
test_df = cluster.get_jobtitles_over_time(junk)

# Using whole widthness of the screen with wide mode.
st.set_page_config(layout="wide", page_title="TrendanalyseFiducia")
# Splitting the page layout in two columns
col1, col2 = st.beta_columns(2)

bar_chart = alt.Chart(bar_chart_df).mark_bar().encode(
    x='Jobbezeichnung',
    y='offene Stellen',
    color=alt.Color('Jobbezeichnung', legend=alt.Legend(title="Bars by title"))
).configure_axis(
    labelFontSize=15,
    titleFontSize=15
).configure_legend(
    labelFontSize=15
)

base = alt.Chart(test_df).mark_line().encode(
    x='date',
    y='amount',
    color='job_title'
).configure_axis(
    labelFontSize=15,
    titleFontSize=15,
).configure_legend(
    labelFontSize=15
)

line_chart = alt.Chart(line_chart_df).mark_line().encode(
    x='Datum',
    y='Anzahl Ausschreibungen'
).configure_axis(
    labelFontSize=15,
    titleFontSize=15
)

# Elements filling the sidebar
st.sidebar.subheader("DISCLAIMER")
st.sidebar.text(
    "Das ist ein Prototyp zum Thema\n'Trendanalyse durch Web crawling'.\nEs gibt keine Garantie auf"
    " \nRichtigkeit der Daten.")

with col1:
    st.subheader("Offene Stellen in Kategorien sortiert")
    st.altair_chart(bar_chart, use_container_width=True)
    st.subheader("Offene Stellen über Zeit")
    st.altair_chart(line_chart, use_container_width=True)

with col2:
    st.subheader("Offene Stellen gruppiert nach Kategorien über Zeit")
    st.altair_chart(base, use_container_width=True)
