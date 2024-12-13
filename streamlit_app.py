import streamlit as st

# Titel van de applicatie
st.title("FPIES Diagnostisch Algoritme")

# Inleiding
st.markdown(
    """
    Welkom bij de FPIES diagnostische tool. Beantwoord de volgende vragen stap voor stap 
    om te bepalen of een patiënt mogelijk aan FPIES (Food Protein-Induced Enterocolitis Syndrome) lijdt.
    """
)

# Vraag 1: Leeftijd van de patiënt
age = st.selectbox("Wat is de leeftijd van de patiënt?", ["<16 jaar", "≥16 jaar"])

if age == "<16 jaar":
    st.write("Patiënt valt onder de kindcategorie.")

    # Vraag 2: Heeft de patiënt acute symptomen?
    acute_symptoms = st.radio("Heeft de patiënt acute symptomen?", ["Ja", "Nee"])

    if acute_symptoms == "Ja":
        # Vraag 3: Zijn er ≥3 minor criteria aanwezig?
        minor_criteria = [
            st.checkbox("Repetitief braken na eten van hetzelfde voedsel"),
            st.checkbox("Braken 1-4 uur na eten van verdacht voedsel"),
            st.checkbox("Significant lethargie met reactie"),
            st.checkbox("Bleekheid met reactie"),
            st.checkbox("Intravenus vocht of ziekenhuisopname vereist")
        ]

        # Tellen van criteria
        criteria_count = sum(minor_criteria)

        if criteria_count >= 3:
            st.success("Patiënt voldoet aan criteria voor acute FPIES. Overweeg een gecontroleerde voedselprovocatie.")
        else:
            st.warning("Patiënt voldoet mogelijk niet aan de criteria. Overweeg andere oorzaken.")

    else:
        st.info("Geen acute symptomen. Overweeg chronische FPIES.")
        chronic_symptoms = st.radio(
            "Zijn er terugkerende symptomen zoals waterige diarree of braken met regelmatige consumptie?", ["Ja", "Nee"]
        )
        if chronic_symptoms == "Ja":
            st.success("Patiënt voldoet aan criteria voor chronische FPIES.")
        else:
            st.warning("Overweeg andere oorzaken dan FPIES.")

elif age == "≥16 jaar":
    st.write("Patiënt valt onder de volwassen categorie.")

    # Vraag 4: Zijn er ≥2 episoden van koliekachtige buikpijn na hetzelfde voedsel?
    abdominal_pain = st.radio(
        "Heeft de patiënt ≥2 episoden van koliekachtige buikpijn of braken na eten van hetzelfde voedsel?", ["Ja", "Nee"]
    )

    if abdominal_pain == "Ja":
        # Minor criteria voor volwassenen
        minor_criteria_adult = [
            st.checkbox("Significant lethargie"),
            st.checkbox("Bleekheid"),
            st.checkbox("Diarree binnen 24 uur"),
            st.checkbox("Hypotensie of hypothermie"),
            st.checkbox("Intravenus vocht nodig")
        ]
        criteria_count_adult = sum(minor_criteria_adult)

        if criteria_count_adult >= 3:
            st.success("Patiënt voldoet aan criteria voor acute FPIES bij volwassenen.")
        else:
            st.warning("Mogelijke FPIES-symptomen. Overweeg verdere evaluatie.")
    else:
        st.info("Zijn er andere symptomen zoals significant lethargie, bleekheid, of diarree na voedselinname?")
        other_symptoms = st.radio("Andere symptomen aanwezig?", ["Ja", "Nee"])
        if other_symptoms == "Ja":
            st.success("Overweeg FPIES met aanvullende diagnostiek.")
        else:
            st.warning("Geen duidelijke symptomen van FPIES. Overweeg andere oorzaken.")

# Slot
st.markdown(
    """
    **Disclaimer:** Deze tool is bedoeld ter ondersteuning en niet als vervanging voor medische diagnose of behandeling.
    Neem bij twijfel contact op met een specialist.
    """
)
