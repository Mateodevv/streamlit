import streamlit as st
import concatLayer
import altair as alt
from datetime import date

# Init data from Data Pipelines
jobtitles_bar_chart_df = concatLayer.get_concated_clustered_jobtitles()
jobamount_line_chart_df = concatLayer.get_concated_jobamount_over_time()
jobtitles_overtime_df = concatLayer.get_concated_jobtitles_over_time()

# Using whole widthness of the screen with wide mode.
st.set_page_config(layout="wide", page_title="TrendanalyseFiducia")
# Splitting the page layout in two columns
col1, col2 = st.beta_columns(2)

bar_chart = alt.Chart(jobtitles_bar_chart_df).mark_bar().encode(
    x='Jobbezeichnung',
    y='offene Stellen',
    color=alt.Color('Jobbezeichnung', legend=alt.Legend(title="Bars by title"))
).configure_axis(
    labelFontSize=15,
    titleFontSize=15
).configure_legend(
    labelFontSize=15
)

base = alt.Chart(jobtitles_overtime_df).mark_line().encode(
    x='date',
    y='amount',
    color='job_title'
).configure_axis(
    labelFontSize=15,
    titleFontSize=15,
).configure_legend(
    labelFontSize=15
)

line_chart = alt.Chart(jobamount_line_chart_df).mark_line().encode(
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

expander = st.sidebar.beta_expander("Date from last changes")
expander.write("8.3.2021")

# Filling one column of the splitted layout
with col1:
    st.subheader("Offene Stellen in Kategorien sortiert")
    st.altair_chart(bar_chart, use_container_width=True)
    stellen_exp = st.beta_expander("Interpretationshilfe")
    stellen_exp.write("Der Graph zeigt, wie viele Stellen pro Beruf offen sind. Eine Korrelation \nmit der Zeit wird "
                      "nicht betrachtet.")

    st.subheader("Anzahl neu veröffentlichter Stellen über Zeit")
    st.altair_chart(line_chart, use_container_width=True)


with col2:
    st.subheader("Offene Stellen gruppiert nach Kategorien über Zeit")
    st.altair_chart(base, use_container_width=True)
    stellenzeit_exp = st.beta_expander("Interpretationshilfe")
    stellenzeit_exp.write("Der Graph zeigt, wie viele Stellen pro Beruf über Zeit offen sind. Hier kann man plötzliche"
                          "Nachfragespikes für Berufsgruppen beobachten.")
