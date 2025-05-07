import streamlit as st

st.set_page_config(page_title="Abgezinste Amortisationszeit-Rechner", page_icon="C:/Users/see/Documents/Lehrprojekt Cobot/favicon/mdz-ico.ico")

# Titel und Einführung
st.title("Abgezinste Amortisationszeit (DPP) Rechner für KMU")
st.markdown("""
Dieses Tool hilft kleinen und mittleren Unternehmen (KMU), die abgezinste Amortisationszeit (Discounted Payback Period, DPP) für Investitionen wie Cobots zu berechnen.
Gib einfach deine Schätzwerte ein.
""")

# Eingabefelder
investition = st.number_input("Investitionskosten (€)", min_value=0.0, value=8000.0, step=100.0)
jaehrlicher_cashflow = st.number_input("Jährlicher Rückfluss / Einsparung (€)", min_value=0.0, value=2500.0, step=100.0)
zinssatz = st.slider("Diskontierungszinssatz (%)", min_value=0.0, max_value=20.0, value=8.0, step=0.5)
max_jahre = st.slider("Maximale Betrachtungsdauer (Jahre)", 1, 20, 10)

# Berechnung
zinssatz = zinssatz / 100  # Umwandlung in Dezimalform
kumulierte_barwerte = 0.0
jahr = 0
ergebnisse = []

while kumulierte_barwerte < investition and jahr < max_jahre:
    jahr += 1
    abgezinster_cf = jaehrlicher_cashflow / ((1 + zinssatz) ** jahr)
    kumulierte_barwerte += abgezinster_cf
    ergebnisse.append((jahr, jaehrlicher_cashflow, abgezinster_cf, kumulierte_barwerte))

# Ergebnisanzeige
st.subheader("Berechnete Rückflüsse pro Jahr:")
st.table(
    { "Jahr": [r[0] for r in ergebnisse],
      "Rückfluss (€)": [f"{r[1]:,.2f}" for r in ergebnisse],
      "Abgezinst (€)": [f"{r[2]:,.2f}" for r in ergebnisse],
      "Kumuliert (€)": [f"{r[3]:,.2f}" for r in ergebnisse] }
)

# Ergebnistext
if kumulierte_barwerte >= investition:
    st.success(f"Die Investition amortisiert sich nach ca. {jahr} Jahren (abgezinst).")
else:
    st.warning("Die Investition hat sich innerhalb der betrachteten Jahre nicht amortisiert.")

# Fußnote
st.markdown("---")
st.caption("Hinweis: Dies ist eine vereinfachte Berechnung. Für detailliertere Analysen kann ein Finanzberater hinzugezogen werden.")
