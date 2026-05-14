import streamlit as st

st.title("Kalkulator Premi Asuransi")

st.write("Simulasi sederhana premi asuransi")

usia = st.number_input("Masukkan usia", 1, 100)

bunga = st.number_input("Masukkan bunga (%)", 0.0, 100.0)

santunan = st.number_input("Masukkan santunan (Rp)", 0)

jangka = st.number_input("Jangka waktu (tahun)", 1, 100)

if st.button("Hitung Premi"):

    premi = (santunan * (bunga / 100)) / jangka

    st.success(f"Premi Tahunan: Rp {premi:,.0f}")