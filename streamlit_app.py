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
age = st.selectbox("Wat is de leeftijd van de patiënt?", ["<16 jaar", "\u226516 jaar"])

if age == "<16 jaar":
    st.write("Patiënt valt onder de kindcategorie.")

    # Vraag 2: Heeft de patiënt acute symptomen?
    acute_symptoms = st.radio("Heeft de patiënt acute symptomen?", ["Ja", "Nee"])

    if acute_symptoms == "Ja":
        # Vraag 3: Zijn er \u22653 minor criteria aanwezig?
        minor_criteria = st.checkbox("Repetitief braken na eten van hetzelfde voedsel")
        minor_criteria2 = st.checkbox("Braken 1-4 uur na eten van ander voedsel")
        minor_criteria3 = st.checkbox("Significant lethargisch bij verdacht voedsel")
        minor_criteria4 = st.checkbox("Bleekheid bij verdacht voedsel")
        minor_criteria5 = st.checkbox("Intravenus vocht nodig bij reactie")
        
        # Tellen van criteria
        criteria_count = sum([minor_criteria, minor_criteria2, minor_criteria3, minor_criteria4, minor_criteria5])
        
        if criteria_count >= 3:
            st.success("Patiënt voldoet aan criteria voor acute FPIES. Overweeg een gecontroleerde voedselprovocatie.")
        else:
            st.warning("Patiënt voldoet mogelijk niet aan de criteria. Overweeg andere oorzaken.")

    else:
        st.info("Geen acute symptomen. Overweeg chronische FPIES of andere oorzaken.")

elif age == "\u226516 jaar":
    st.write("Patiënt valt onder de volwassen categorie.")

    # Vraag 4: Zijn er \u22652 episoden van colicky abdominale pijn na hetzelfde voedsel?
    abdominal_pain = st.radio(
        "Heeft de patiënt \u22652 episoden van koliekachtige buikpijn na eten van hetzelfde voedsel?", ["Ja", "Nee"]
    )

    if abdominal_pain == "Ja":
        st.success("Patiënt voldoet aan criteria voor volwassen FPIES. Overweeg een gecontroleerde voedselprovocatie.")
    else:
        st.warning("Geen duidelijke symptomen van FPIES. Overweeg andere oorzaken.")

# Slot
st.markdown(
    """
    **Disclaimer:** Deze tool is bedoeld ter ondersteuning en niet als vervanging voor medische diagnose of behandeling.
    Neem bij twijfel contact op met een specialist.
    """
)
