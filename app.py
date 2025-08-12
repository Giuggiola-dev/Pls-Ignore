import streamlit as st

st.write("Hello world!")

st.write("Seleziona un Paese dell'Unione Europea dal menù a tendina")

options=["BE",  "BG",  "CZ",  "DK",  "DE",  "EE",  "IE",  "EL",  "ES",  "FR",  "HR",  "IT",  "CY",  "LV",  "LT",  "LU",  "HU",  "MT",  "NL",  "AT",  "PL",  "PT",  "RO",  "SI",  "SK",  "FI",  "SE",  "IS",  "NO"]
country_dict = {
  "BE": "Belgium",
  "BG": "Bulgaria",
  "CZ": "Czechia",
  "DK": "Denmark",
  "DE": "Germany",
  "EE": "Estonia",
  "IE": "Ireland",
  "EL": "Greece",
  "ES": "Spain",
  "FR": "France",
  "HR": "Croatia",
  "IT": "Italy",
  "CY": "Cyprus",
  "LV": "Latvia",
  "LT": "Lithuania",
  "LU": "Luxembourg",
  "HU": "Hungary",
  "MT": "Malta",
  "NL": "Netherlands",
  "AT": "Austria",
  "PL": "Poland",
  "PT": "Portugal",
  "RO": "Romania",
  "SI": "Slovenia",
  "SK": "Slovakia",
  "FI": "Finland",
  "SE": "Sweden",
  "IS": "Iceland",
  "NO": "Norway"
}

def label_function (key):
    return country_dict[key]

country = st.selectbox("Paese", options, index=None, format_func=lambda x: label_function(x), placeholder="Seleziona un Paese...")


if country is not None:
    st.write(f"Hai selezionato {label_function(country)}, che ha codice {country}!")