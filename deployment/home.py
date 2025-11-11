import streamlit as st
from PIL import Image

def run():
    # Header
    st.title("Selamat Datang di SkillMatch")
    st.write("#### Temukan pekerjaan impianmu dengan bantuan AI 🔍")
    
    st.image("./src/logo.png", use_container_width=True)

    st.markdown("""
    Hai, 👋  
    Kami senang kamu datang ke **SkillMatch** — asisten cerdas yang akan membantumu menemukan
    **pekerjaan paling cocok** dengan skill yang kamu miliki.

    Cukup masukkan kemampuanmu, dan biarkan AI kami mencarikan peluang terbaik dari berbagai bidang industri:
    - 💻 Data & IT  
    - 🧠 Software Development  
    - 💰 Banking & Finance  
    - 🎓 Education  
    - 🏨 Hospitality  
    - 🏥 Medical, dan masih banyak lagi!
    """)

    st.markdown("---")
    st.subheader("✨ Siap Mulai? 🔍")
    st.write("YUK cari pekerjaan yang sesuai dengan skill kamu 💼💡")
    st.markdown("---")

    # Info aplikasi
    st.write("💬 About Me")
    with st.expander("🌟 Apa itu SkillMatch?"):
        st.markdown("""
        **SkillMatch** adalah platform berbasis *Artificial Intelligence* yang memahami
        makna dari skill kamu — bukan hanya kata-katanya.

        Sistem kami akan mencocokkan kemampuanmu dengan ribuan deskripsi pekerjaan yang sedang *high demand*,
        lalu merekomendasikan posisi terbaik untukmu secara otomatis.

        💬 *“Kamu cukup fokus pada skill-mu — biar AI yang carikan peluangnya.”*
        """)

    with st.expander("💡 Mengapa Harus SkillMatch?"):
        st.markdown("""
        - 🔍 Rekomendasi pekerjaan yang **benar-benar relevan**  
        - ⚡ Hasil cepat dan akurat  
        - 🌍 Menjangkau lebih dari **15 bidang industri**  
        - 🧭 Bantu kamu memahami arah karier yang sesuai dengan kemampuanmu  
        """)

    st.markdown("---")
    st.caption("© 2025 SkillMatch | Smart Job Recommendation Platform 💼")

if __name__ == "__main__":
    run()