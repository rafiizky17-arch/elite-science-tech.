import streamlit as st

st.title("Aplikasi Edit Keren")
st.write("Selamat datang di aplikasi edit pertama kamu!")

# Contoh kotak input teks
teks = st.text_area("Masukkan tulisanmu di sini:", "Tulis sesuatu...")

if st.button("Tampilkan"):
    st.write("Tulisan kamu:")
    st.write(teks)
