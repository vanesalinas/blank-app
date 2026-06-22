import streamlit as st
from catalogo import catalogo

def recomendador(leche, notas, intensidad):

    mejor_cafe          = None
    mejor_puntaje       = 0          

    for cafe in catalogo:
        coincide_leche = cafe["Con leche"] == leche or cafe["Con leche"] == "ambos"
        coincide_notas = notas in cafe["Notas de sabor"]
        coincide_intesidad = cafe["Intensidad"] == intensidad

        puntaje = sum([coincide_leche, coincide_notas, coincide_intesidad]) #cuenta cuantos son TRRUE

        if puntaje == 3:
            return cafe, [leche, notas, intensidad]
        
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_cafe = cafe
            mejor_coincidencias = []
            if coincide_leche:
                mejor_coincidencias.append(leche)
            if coincide_notas:
                mejor_coincidencias.append(notas)
            if coincide_intesidad:
                mejor_coincidencias.append(intensidad)
    
    if mejor_cafe:
        return mejor_cafe, mejor_coincidencias
    
st.title("☕ Recomendador de Café Personalizado")
st.write(
    "Selecciona tus preferencias para obtener la recomendación ideal"
)

leche = st.selectbox(
    "¿Cómo tomás el café?",
    ["solo", "con leche"]
)

notas = st.selectbox(
    "¿Qué notas de sabor te gustan?",
    [
        "vainilla",
        "chocolate",
        "frutilla",
        "frutos secos",
        "pasas",
        "dulzor marcado"
    ]
)

intensidad = st.selectbox(
    "¿Qué intensidad preferís?",
    ["suave", "medio", "intenso"]
)

if st.button("Encontrar mi café"):

    cafe, coincidencias = recomendador(
        leche,
        notas,
        intensidad
    )

    if cafe:

        if len(coincidencias) == 3:

            st.success("¡Encontramos tu café ideal!")

            st.subheader(cafe["Nombre cafe"])

            st.write(f"**Tostadería:** {cafe['Tostaderia']}")
            st.write(f"**Origen:** {cafe['Origen']}")
            st.write(f"**Proceso:** {cafe['Proceso']}")
            st.write(f"**Intensidad:** {cafe['Intensidad']}")
            st.write(f"**Notas:** {cafe['Notas de sabor']}")
            st.write(f"**Puntaje SCA:** {cafe['SCA']}")

        else:

            st.warning("No encontramos una coincidencia exacta.")

            st.subheader(
                f"☕ Te recomendamos probar {cafe['Nombre cafe']}"
            )

            st.write(
                f"Coincide con: {', '.join(coincidencias)}"
            )

            st.write(
                f"Notas: {cafe['Notas de sabor']}"
            )

    else:
        st.error("No encontramos un café adecuado.")
