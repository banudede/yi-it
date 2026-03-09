import streamlit as st
import time

# Sayfa ayarları
st.set_page_config(page_title="Uyum Envanteri", page_icon="📊")

# İlerleme durumu yönetimi
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'show_results' not in st.session_state:
    st.session_state.show_results = False

st.title("📊 Yiğit İle Banu'nun Uyum Envanteri")
st.write("Merhaba Yiğit! Bu çalışma, Banu'nun eğitim projesi kapsamında geliştirilmiştir. Lütfen tüm soruları objektif ve içtenlikle yanıtlayınız.")

# Soruları tek tek gösterme mantığı
if st.session_state.step < 10:
    st.write(f"Soru {st.session_state.step + 1} / 10")
    
    # 10 Soru için seçimler
    if st.session_state.step == 0:
        ans = st.slider("İnsan ilişkilerinde 'güven' faktörünü 1'den 10'a kadar puanlayın:", 1, 10, 5)
    else:
        # Soruları ve şıkları burada listeliyoruz
        sorular = [
            "", # 0. soru slider olduğu için boş
            "Bir arkadaşlıkta en çok neye önem verirsiniz?",
            "Sosyal ortamlarda genellikle gözlemci mi yoksa yönlendirici mi olmayı tercih edersin?",
            "Banu ile ortak bir karar almanız gerekse, genelde kimin fikri daha baskın olur?",
            "Genel olarak arkadaşlıklarında 'sakinleştirici' bir güç müsün, yoksa 'hareketlendirici' mi?",
            "Planlı hareket etmeyi mi seversin, yoksa akışına bırakmayı mı?",
            "Küçük bir anlaşmazlıkta ilk adımı atmayı mı tercih edersin, yoksa karşı tarafın gelmesini mi?",
            "Banu ile ortak bir ilgi alanınız olsaydı bu ne olurdu?",
            "Banu ile vakit geçirirken sence hangimiz daha çok eğleniyoruz?",
            "Sence bu testin sonunda aramızdaki 'uyum' ne çıkacak?"
        ]
        
        secenekler = [
            [], # 0
            ["Dürüstlük", "Ortak hobiler", "İletişim sıklığı"],
            ["Gözlemci", "Yönlendirici", "Ortama göre dengeleyici"],
            ["Genelde benim fikirlerim", "Genelde Banu'nun fikirleri", "Ortak bir noktada buluşuruz"],
            ["Sakinleştirici", "Hareketlendirici", "Duruma göre değişir"],
            ["Planlı", "Akışına bırakırım"],
            ["İlk adımı atarım", "Karşı taraf gelsin"],
            ["Teknoloji", "Eğlence", "Sosyal Projeler"],
            ["Ben onu eğlendiriyorum", "O beni daha çok eğlendiriyor", "İkimiz de birbirimizi tamamlıyoruz"],
            ["Oldukça yüksek bir skor", "Gözlem aşamasında olduğumuz bir sonuç", "Henüz keşfedilmemiş bir potansiyel"]
        ]
        
        ans = st.radio(sorular[st.session_state.step], secenekler[st.session_state.step])

    if st.button("Sıradaki Soru"):
        st.session_state.step += 1
        st.rerun()

elif not st.session_state.show_results:
    # 20 saniyelik yükleme çubuğu
    st.write("Analiz verileri hesaplanıyor...")
    progress_bar = st.progress(0)
    progress_text = st.empty()
    
    for i in range(101):
        progress_bar.progress(i)
        progress_text.text(f"Yükleme Durumu: %{i}")
        time.sleep(0.198) # 100 adım x 0.198 = ~20 saniye
    
    st.session_state.show_results = True
    st.rerun()

else:
    # Final: Önce resim, sonra yazı gelecek şekilde düzenlendi
    st.image("intikam.png", use_container_width=True)
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>HEE ÇOK BEKLERSİN! 🤣 AL SANA ANALİZ! 🖕 </h1>", unsafe_allow_html=True)::