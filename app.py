import streamlit as st
import time

# Sayfa ayarları
st.set_page_config(page_title="Uyum Envanteri", page_icon="📊")

# Soruları liste olarak tanımlayalım
questions = [
    "1. İnsan ilişkilerinde 'güven' faktörünü 1'den 10'a kadar puanlayın:",
    "2. Bir arkadaşlıkta en çok neye önem verirsiniz?",
    "3. Sosyal ortamlarda genellikle gözlemci mi yoksa yönlendirici mi olmayı tercih edersin?",
    "4. Banu ile ortak bir karar almanız gerekse, genelde kimin fikri daha baskın olur?",
    "5. Genel olarak arkadaşlıklarında 'sakinleştirici' bir güç müsün, yoksa 'hareketlendirici' mi?",
    "6. Planlı hareket etmeyi mi seversin, yoksa akışına bırakmayı mı?",
    "7. Küçük bir anlaşmazlıkta ilk adımı atmayı mı tercih edersin, yoksa karşı tarafın gelmesini mi?",
    "8. Banu ile ortak bir ilgi alanınız olsaydı bu ne olurdu?",
    "9. Banu ile vakit geçirirken sence hangimiz daha çok eğleniyoruz?",
    "10. Sence bu testin sonunda aramızdaki 'uyum' ne çıkacak?"
]

# İlerleme durumu
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'show_results' not in st.session_state:
    st.session_state.show_results = False

st.title("📊 Yiğit İle Banu'nun Uyum Envanteri")
st.write("Merhaba Yiğit! Bu çalışma, Banu'nun eğitim projesi kapsamında geliştirilmiştir. Lütfen tüm soruları objektif ve içtenlikle yanıtlayınız.")

# Soruları tek tek gösterme mantığı
if st.session_state.step < len(questions):
    st.write(f"Soru {st.session_state.step + 1} / 10")
    
    if st.session_state.step == 0:
        ans = st.slider(questions[st.session_state.step], 1, 10, 5)
    else:
        # Seçenekler
        options_map = {
            1: ["Dürüstlük", "Ortak hobiler", "İletişim sıklığı"],
            2: ["Gözlemci", "Yönlendirici", "Ortama göre dengeleyici"],
            3: ["Genelde benim fikirlerim", "Genelde Banu'nun fikirleri", "Ortak bir noktada buluşuruz"],
            4: ["Sakinleştirici", "Hareketlendirici", "Duruma göre değişir"],
            5: ["Planlı", "Akışına bırakırım"],
            6: ["İlk adımı atarım", "Karşı taraf gelsin"],
            7: ["Teknoloji", "Eğlence", "Sosyal Projeler"],
            8: ["Ben onu eğlendiriyorum", "O beni daha çok eğlendiriyor", "İkimiz de birbirimizi tamamlıyoruz"],
            9: ["Oldukça yüksek bir skor", "Gözlem aşamasında olduğumuz bir sonuç", "Henüz keşfedilmemiş bir potansiyel"]
        }
        ans = st.radio(questions[st.session_state.step], options_map.get(st.session_state.step, ["Seçenek A", "Seçenek B"]))

    if st.button("Sıradaki Soru"):
        st.session_state.step += 1
        st.rerun()

elif not st.session_state.show_results:
    # Yüzde göstergeli yükleme çubuğu
    st.write("Analiz verileri hesaplanıyor...")
    progress_text = st.empty()
    progress_bar = st.progress(0)
    
    for i in range(101):
        progress_bar.progress(i)
        progress_text.text(f"Yükleniyor: %{i}")
        time.sleep(0.02) # Burayı istediğin hıza göre değiştirebilirsin
    
    st.session_state.show_results = True
    st.rerun()

else:
    # Final Şok!
    st.image("intikam.png", use_container_width=True)
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>HEE ÇOK BEKLERSİN! AL SANA ANALİZ!</h1>", unsafe_allow_html=True)