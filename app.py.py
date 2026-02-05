import streamlit as st
import os

# Sayfa Ayarları
st.set_page_config(page_title="Lise Çalışma Portalı", layout="wide", page_icon="📓")

# CSS ile Görünümü Güzelleştirme
st.markdown("""
    <style>
    .ozet-kutusu {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #2ecc71;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    .gunluk-alani {
        background-color: #fef9e7;
        padding: 20px;
        border-radius: 15px;
        border: 1px dashed #f39c12;
    }
    </style>
    """, unsafe_allow_html=True)

# Yan Menü: Sınıf Seçimi
sinif = st.sidebar.selectbox("Sınıf Seçiniz", ["9. Sınıf", "10. Sınıf", "11. Sınıf", "12. Sınıf"])
st.sidebar.markdown("---")
st.sidebar.write("🎯 **Hedefine Odaklan!**")

# PDF İndirme Fonksiyonu
def pdf_indir(dosya_adi, etiket):
    yol = f"belgeler/{dosya_adi}"
    if os.path.exists(yol):
        with open(yol, "rb") as f:
            st.download_button(label=f"📥 {etiket} PDF", data=f, file_name=dosya_adi)
    else:
        st.warning(f"⚠️ {dosya_adi} henüz 'belgeler' klasörüne atılmamış.")

# ANA BAŞLIK
st.title(f"🎓 {sinif} Çalışma Alanı")

# İÇERİK SEKMELERİ
tab_ders, tab_gunluk = st.tabs(["📖 Ders Özetleri & PDF", "✍️ Kişisel Not Defterim"])

with tab_ders:
    if sinif == "9. Sınıf":
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📐 Matematik")
            st.markdown("<div class='ozet-kutusu'><b>Hızlı Özet:</b><br>Mantık konusunda 'p ⇒ q' önermesi sadece 1 ⇒ 0 iken yanlıştır. Diğer tüm durumlarda doğrudur.</div>", unsafe_allow_html=True)
            pdf_indir("mat9.pdf", "9. Sınıf Matematik")
            
        with col2:
            st.subheader("🧪 Fizik")
            st.markdown("<div class='ozet-kutusu'><b>Hızlı Özet:</b><br>Fiziğin alt dalları: Kamyonet (Katıhal, Atom, Mekanik, Yüksek Enerji, Optik, Nükleer, Elektromanyetizma, Termodinamik).</div>", unsafe_allow_html=True)
            pdf_indir("fiz9.pdf", "9. Sınıf Fizik")

    # Diğer sınıflar buraya elif ile eklenebilir...
    else:
        st.info("Bu sınıfın özetleri yakında eklenecek.")

with tab_gunluk:
    st.markdown("<div class='gunluk-alani'>", unsafe_allow_html=True)
    st.subheader("📝 Bugün Neler Öğrendim?")
    kisisel_not = st.text_area("Günlük çalışma notlarını buraya bırak:", height=150, placeholder="Bugün 50 paragraf çözdüm, biyolojide hücreyi bitirdim...")
    
    if st.button("Notu Onayla"):
        st.success("Harika! Notun kaydedildi (Sayfa yenilenene kadar burada duracak).")
        st.balloons()
    st.markdown("</div>", unsafe_allow_html=True)