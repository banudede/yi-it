import streamlit as st
import time

# Sayfa ayarları
st.set_page_config(page_title="Yiğit ile Banu'nun Uyum Envanteri", page_icon="📊")

# Soruları bir listede tutalım
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

# Session state başlatma
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

st.title("📊 Yiğit İle Banu'nun Uyum Envanteri")
st.write("Merhaba Yiğit! Bu çalışma, Banu'nun eğitim projesi kapsamında geliştirilmiştir. Lütfen tüm soruları objektif ve içtenlikle yanıtlayınız.")

# Soru gösterme mantığı
if st.session_state.step < len(questions):
    st.write(f"Soru {st.session_state.step + 1} / 10")
    
    # Sorulara göre giriş tipleri
    if st.session_state.step == 0:
        ans = st.slider(questions[st.session_state.step], 1, 10, 5)
    elif st.session_state.step == 1:
        ans = st.radio(questions[st.session_state.step], ["Dürüstlük", "Ortak hobiler", "İletişim sıklığı"])
    elif st.session_state.step == 2:
        ans = st.radio(questions[st.session_state.step], ["Gözlemci", "Yönlendirici", "Ortama göre dengeleyici"])
    elif st.session_state.step == 3:
        ans = st.radio(questions[st.session_state.step], ["Genelde benim fikirlerim", "Genelde Banu'nun fikirleri", "Ortak bir noktada buluşuruz"])
    elif st.session_state.step == 4:
        ans = st.radio(questions[st.session_state.step], ["Sakinleştirici", "Hareketlendirici", "Duruma göre değişir"])
    elif st.session_state.step == 5:
        ans = st.radio(questions[st.session_state.step], ["Planlı", "Akışına bırakırım"])
    elif st.session_state.step == 6:
        ans = st.radio(questions[st.session_state.step], ["İlk adımı atarım", "Karşı taraf gelsin"])
    elif st.session_state.step == 7:
        ans = st.radio(questions[st.session_state.step], ["Teknoloji", "Eğlence", "Sosyal Projeler"])
    elif st.session_state.step == 8:
        ans = st.radio(questions[st.session_state.step], ["Ben onu eğlendiriyorum", "O beni daha çok eğlendiriyor", "İkimiz de birbirimizi tamamlıyoruz"])
    else:
        ans = st.radio(questions[st.session_state.step], ["Oldukça yüksek bir skor", "Gözlem aşamasında olduğumuz bir sonuç", "Henüz keşfedilmemiş bir potansiyel"])

    if st.button("Sıradaki Soru"):
        st.session_state.answers.append(ans)
        st.session_state.step += 1
        st.rerun()

else:
    # 10 Soru bitti, Yükleme çubuğu başlasın
    st.write("Analizler hesaplanıyor, lütfen bekleyiniz...")
    progress_bar = st.progress(0)
    
    for i in range(101):
        time.sleep(0.05) # Hızını buradan ayarlayabilirsin, 0.05 yavaş ilerletir
        progress_bar.progress(i)
    
    st.session_state.step += 1
    st.rerun()

# Sonuç ekranı
if st.session_state.step > len(questions):
    st.image("intikam.png", use_container_width=True)
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>HEE ÇOK BEKLERSİN! AL SANA ANALİZ!</h1>", unsafe_allow_html=True)