import streamlit as st
import numpy as np
import numpy_financial as npf



st.set_page_config(page_title="Cobot IZF-Rechner", page_icon="C:/Users/see/Documents/Lehrprojekt Cobot/favicon/mdz-ico.ico")

st.title("Cobot-Investitionsrechner")
st.markdown("Berechne den **internen Zinsfuß (IZF)**, Kapitalwert (NPV) und die Amortisationsdauer deiner Cobot-Investition.")

# Eingaben
investitionskosten = st.number_input("Investitionskosten (€)", min_value=1000, value=6000, step=100)
nutzungsdauer = st.number_input("Nutzungsdauer (Jahre)", min_value=1, value=5)
rueckfluss = st.number_input("Rückfluss pro Jahr (€)", min_value=0, value=2000, step=100)
restwert = st.number_input("Geschätzter Restwert nach Nutzungsdauer (€)", min_value=0, value=0)
kalk_zins = st.number_input("Kalkulationszins (%)", min_value=0.0, value=5.0, step=0.5) / 100

# Cashflows berechnen
cashflows = [-investitionskosten] + [rueckfluss] * int(nutzungsdauer)
cashflows[-1] += restwert  # Restwert am Ende berücksichtigen

# Berechnungen
izf = npf.irr(cashflows)
npv = npf.npv(kalk_zins, cashflows)

# Amortisation berechnen
kumulierter_cashflow = 0
amortisationsdauer = None
for i, cf in enumerate(cashflows[1:], start=1):
    kumulierter_cashflow += cf
    if kumulierter_cashflow >= investitionskosten:
        amortisationsdauer = i
        break

# Ergebnisse anzeigen
st.subheader("Ergebnisse")

st.write(f"**Interner Zinsfuß (IZF):** {izf*100:.2f} %")
st.write(f"**Kapitalwert (NPV) bei {kalk_zins*100:.1f}% Zins:** {npv:.2f} €")
if amortisationsdauer:
    st.write(f"**Amortisationsdauer:** {amortisationsdauer} Jahre")
else:
    st.warning("Amortisation nicht innerhalb der Nutzungsdauer erreicht.")

# Cashflow-Visualisierung (optional)
import matplotlib.pyplot as plt

st.subheader("Cashflow-Diagramm")
jahre = list(range(len(cashflows)))
plt.figure(figsize=(8, 3))
plt.bar(jahre, cashflows, color="skyblue")
plt.axhline(0, color="gray", linestyle="--")
plt.xlabel("Jahr")
plt.ylabel("Cashflow (€)")
plt.title("Jährliche Cashflows")
st.pyplot(plt)
