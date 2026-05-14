import streamlit as st

# KONFIGURASI HALAMAN
st.set_page_config(
    page_title="SmartActuary",
    page_icon="🧮",
    layout="wide"
)

# SIDEBAR
st.sidebar.title("🧮 SMARTACTUARY")
st.sidebar.write("Portal Simulasi Premi")

menu = st.sidebar.radio(
    "Navigasi",
    ["Dashboard", "Simulasi Premi", "Tentang"]
)

# DASHBOARD
if menu == "Dashboard":

    st.title("SMARTACTUARY PORTAL")

    st.subheader("Dashboard Simulasi Premi Asuransi")

    col1, col2, col3 = st.columns(3)

    col1.metric("Metode", "Anuitas")
    col2.metric("Status", "Aktif")
    col3.metric("Versi", "1.0")

    st.markdown("---")

    st.info("""
    SmartActuary merupakan portal simulasi premi
    asuransi berbasis Python dan Streamlit.

    Sistem ini dibuat untuk membantu pengguna umum
    memahami simulasi premi dengan lebih mudah.
    """)

    st.markdown("---")

    st.write("### Fitur Sistem")
    st.write("""
    ✅ Simulasi Premi  
    ✅ Perhitungan Cepat  
    ✅ User Friendly  
    ✅ Berbasis Aktuaria  
    """)

# SIMULASI PREMI
elif menu == "Simulasi Premi":

    st.title("Simulasi Premi")

    col1, col2 = st.columns(2)

    with col1:

        usia = st.number_input(
            "Masukkan usia",
            min_value=1,
            max_value=100,
            value=25
        )

        bunga = st.number_input(
            "Masukkan bunga (%)",
            min_value=0.0,
            max_value=100.0,
            value=6.0
        )

    with col2:

        santunan = st.number_input(
            "Masukkan santunan (Rp)",
            min_value=0,
            value=100000000
        )

        jangka = st.number_input(
            "Jangka waktu (tahun)",
            min_value=1,
            max_value=100,
            value=20
        )

    st.markdown("---")

    if st.button("Hitung Premi"):

        premi = (santunan * (bunga / 100)) / jangka

        st.success(
            f"Premi Tahunan: Rp {premi:,.0f}"
        )

        st.markdown("---")

        c1, c2, c3 = st.columns(3)

        c1.metric("Usia", f"{usia} Tahun")
        c2.metric("Bunga", f"{bunga}%")
        c3.metric("Jangka", f"{jangka} Tahun")

# TENTANG
elif menu == "Tentang":

    st.title("Tentang Sistem")

    st.write("""
    SMARTACTUARY merupakan aplikasi simulasi premi
    asuransi berbasis web menggunakan Python dan Streamlit.

    Sistem ini dibuat sebagai implementasi konsep
    matematika aktuaria ke dalam teknologi interaktif
    yang dapat digunakan masyarakat umum.
    """)

    st.markdown("---")

    st.write("### Teknologi")
    st.write("""
    - Python
    - Streamlit
    - Matematika Aktuaria
    """)