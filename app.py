import streamlit as st
import pandas as pd

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="SmartActuary",
    page_icon="🧮",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
}

h1, h2, h3 {
    color: #0f172a;
}

.stButton>button {
    background: linear-gradient(to right, #2563eb, #1d4ed8);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 12px 25px;
    font-size: 16px;
    font-weight: bold;
}

.stButton>button:hover {
    background: linear-gradient(to right, #1d4ed8, #1e40af);
}

.card {
    background-color: blue;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    color: black;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("SmartActuary")
st.sidebar.write("Portal Simulasi Premi")

menu = st.sidebar.radio(
    "Navigasi",
    ["Dashboard", "Simulasi Premi", "Tentang"]
)

# =========================
# DASHBOARD
# =========================
if menu == "Dashboard":

    st.title("SMARTACTUARY PORTAL")
    st.subheader("Simulasi Premi Asuransi Modern")

    st.markdown("""
    <div class="card">
    <h3>📌 Tentang Sistem</h3>
    <p>
    SmartActuary merupakan aplikasi simulasi premi asuransi
    berbasis Python dan Streamlit yang dirancang agar mudah
    digunakan masyarakat umum.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("### ✨ Fitur Utama")

    fitur1, fitur2, fitur3 = st.columns(3)

    fitur1.success("📊 Simulasi Premi")
    fitur2.success("📈 Grafik Interaktif")
    fitur3.success("🧑 User Friendly")

# =========================
# SIMULASI PREMI
# =========================
elif menu == "Simulasi Premi":

    st.title("📊 Simulasi Premi Asuransi")

    st.markdown("""
    <div class="card">
    Masukkan data berikut untuk menghitung estimasi premi tahunan.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        usia = st.number_input(
            "👤 Usia",
            min_value=1,
            max_value=100,
            value=25
        )

        bunga = st.number_input(
            "💰 Tingkat Bunga (%)",
            min_value=0.0,
            max_value=100.0,
            value=6.0
        )

    with col2:

        santunan = st.number_input(
            "🏦 Santunan (Rp)",
            min_value=0,
            value=100000000
        )

        jangka = st.number_input(
            "📅 Jangka Waktu (Tahun)",
            min_value=1,
            max_value=100,
            value=20
        )

    st.markdown("---")

    if st.button("🚀 Hitung Premi"):

        premi = (santunan * (bunga / 100)) / jangka

        st.success(
            f"✅ Estimasi Premi Tahunan: Rp {premi:,.0f}"
        )

        st.markdown("---")

        # METRIC
        c1, c2, c3 = st.columns(3)

        c1.metric("Usia", f"{usia} Tahun")
        c2.metric("Bunga", f"{bunga}%")
        c3.metric("Jangka", f"{jangka} Tahun")

        st.markdown("---")

        # PENJELASAN USER AWAM
        st.info(f"""
        Semakin panjang jangka waktu pembayaran,
        maka cicilan premi biasanya menjadi lebih kecil.
        
        Namun total pembayaran dapat menjadi lebih besar
        karena adanya pengaruh bunga.
        """)

        # =========================
        # GRAFIK
        # =========================

        tenor_list = [5, 10, 15, 20, 25]

        premi_list = []

        for t in tenor_list:
            hasil = (santunan * (bunga / 100)) / t
            premi_list.append(hasil)

        data = pd.DataFrame({
            "Jangka Waktu": tenor_list,
            "Premi": premi_list
        })

        st.write("### 📈 Grafik Perbandingan Premi")

        st.line_chart(
            data.set_index("Jangka Waktu")
        )

        st.write("### 📋 Tabel Simulasi")

        st.dataframe(data)

# =========================
# TENTANG
# =========================
elif menu == "Tentang":

    st.title("ℹ️ Tentang SmartActuary")

    st.markdown("""
    <div class="card">
    <h3>SMARTACTUARY</h3>

    <p>
    SmartActuary merupakan aplikasi simulasi premi
    asuransi berbasis web yang dibuat menggunakan
    Python dan Streamlit.
    </p>

    <p>
    Sistem ini bertujuan membantu masyarakat umum
    memahami simulasi premi asuransi secara lebih mudah,
    cepat, dan interaktif.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.write("### 🛠️ Teknologi")

    tech1, tech2, tech3 = st.columns(3)

    tech1.info("🐍 Python")
    tech2.info("🎨 Streamlit")
    tech3.info("📊 Matematika Aktuaria")