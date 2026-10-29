import streamlit as st
col1, col2 = st.columns(([1,1]))
with col1: 
    st.image("Logo.png",  width=250)

st.header("Cálculo de Nota Necessária")
st.write("Informe as notas dos dois primeiros trimestres para calcular a nota necessária no terceiro trimestre.")

col3, col4 = st.columns(([1,1]))
with col3:
    nota1 = st.number_input(
        "Nota do 1º trimestre (peso 0,30)",
        min_value=0.0,
        max_value=10.0,
        value=0.0,
        step=0.1,
        format="%.1f"
    )
with col4:
    nota2 = st.number_input(
        "Nota do 2º trimestre (peso 0,35)",
        min_value=0.0,
        max_value=10.0,
        value=0.0,
        step=0.1,
        format="%.1f"
    )

# Cálculo da nota necessária no 3º trimestre
if st.button("Calcular nota necessária"):
    media_desejada = 6.0

    nota3 = (media_desejada - nota1 * 0.30 - nota2 * 0.35) / 0.35

    st.subheader("Nota necessária no 3º trimestre:")

    if nota3 <= 0:
        st.success("O aluno já alcançou a média 6,0, porém o terceiro trimestre é importante para ampliar conhecimentos e melhorar a nota.")
    elif nota3 <= 10:
        st.info(f"O aluno precisa tirar **{nota3:.2f}** no 3º trimestre.")
    else:
        st.error("O aluno não alcançará média 6,0, Mesmo tirando 10,0 no 3º trimestre.")

    # Simulação da média com nota 10 no terceiro trimestre
    media_maxima = nota1 * 0.30 + nota2 * 0.35 + 10 * 0.35
    st.write(f"Média final máxima possível: {media_maxima:.2f}")
    media_parcial= nota1*0.3 + nota2* 0.35
    st.write(f"Média parcial com dois trimestres: {media_parcial:.2f}")