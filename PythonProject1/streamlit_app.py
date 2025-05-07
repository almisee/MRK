import streamlit as st

hom_page = st.Page("home.py", title="Home")
izf_page = st.Page("cobot_izf_app.py", title="Zinsfuß-Rechner")
dpp_page = st.Page("dpp_tool.py", title="Abgezinste Amortisationszeit")

pg = st.navigation([hom_page, izf_page, dpp_page])
pg.run()

st.title("Willkommen in der Übersicht für Cobots im MDZ")
st.write("Wähle das gewünschte Werkzeug über das Seitenmenü links aus.")

