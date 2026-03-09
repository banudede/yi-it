import streamlit as st
import time

# Sayfa ayarları
st.set_page_config(page_title="Uyum Envanteri", page_icon="📊")

# Uygulama akışı için session state
if 'stage' not in st.session_state:
    st.session_state.stage = 'anket'

if st.session_state.stage == 'anket':
    st.title("📊 Yiğit İle Banu'nun Uyum Envanteri")
    st.write("Merhaba Yiğit! Bu çalışma, Banu'nun eğitim projesi kapsamında geliştirilmiştir. Lütfen tüm soruları objektif ve içtenlikle yanıtlayınız.")
    
    with st.form("uyum_formu"):
        # Sorular (Daha önce konuştuğumuz 10 soru)
        q1 = st.slider("1. İnsan ilişkilerinde 'güven' faktörünü 1'den 10'a kadar puanlayın:", 1, 10, 5)
        q2 = st.radio("2. Bir arkadaşlıkta en çok neye önem verirsiniz?", ["Dürüstlük", "Ortak hobiler", "İletişim sıklığı"])
        q3 = st.radio("3. Sosyal ortamlarda genellikle gözlemci mi yoksa yönlendirici mi olmayı tercih edersin?", ["Gözlemci", "Yönlendirici", "Ortama göre dengeleyici"])
        q4 = st.radio("4. Banu ile ortak bir karar almanız gerekse, genelde kimin fikri daha baskın olur?", ["Genelde benim fikirlerim", "Genelde Banu'nun fikirleri", "Ortak bir noktada buluşuruz"])
        q5 = st.radio("5. Genel olarak arkadaşlıklarında 'sakinleştirici' bir güç müsün, yoksa 'hareketlendirici' mi?", ["Sakinleştirici", "Hareketlendirici", "Duruma göre değişir"])
        q6 = st.radio("6. Planlı hareket etmeyi mi seversin, yoksa akışına bırakmayı mı?", ["Planlı", "Akışına bırakırım"])
        q7 = st.radio("7. Küçük bir anlaşmazlıkta ilk adımı atmayı mı tercih edersin, yoksa karşı tarafın gelmesini mi?", ["İlk adımı atarım", "Karşı taraf gelsin"])
        q8 = st.radio("8. Banu ile ortak bir ilgi alanınız olsaydı bu ne olurdu?", ["Teknoloji", "Eğlence", "Sosyal Projeler"])
        q9 = st.radio("9. Banu ile vakit geçirirken sence hangimiz daha çok eğleniyoruz?", ["Ben onu eğlendiriyorum", "O beni daha çok eğlendiriyor", "İkimiz de birbirimizi tamamlıyoruz"])
        q10 = st.radio("10. Sence bu testin sonunda aramızdaki 'uyum' ne çıkacak?", ["Oldukça yüksek bir skor", "Gözlem aşamasında olduğumuz bir sonuç", "Henüz keşfedilmemiş bir potansiyel"])
        
        submitted = st.form_submit_button("Analizi Gör")

    if submitted:
        st.session_state.stage = 'loading'
        st.rerun()

elif st.session_state.stage == 'loading':
    # Yavaş yükleme illüzyonu
    with st.spinner('Analiz verileri işleniyor, lütfen bekleyiniz...'):
        time.sleep(4) # Yiğit bu 4 saniyede iyice sabırsızlanacak
    st.session_state.stage = 'final'
    st.rerun()

elif st.session_state.stage == 'final':
    # Görselin basılması
    st.image("intikam.png", use_container_width=True)
    
    # Yazının gecikmeli belirmesi (opsiyonel ama daha etkileyici)
    time.sleep(1)
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>HEE ÇOK BEKLERSİN! AL SANA ANALİZ!</h1>", unsafe_allow_html=True)