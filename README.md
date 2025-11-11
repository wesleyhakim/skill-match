# 💼 SkillMatch for Job Searching

<div style="text-align: center;">
    <img src="logo.png" alt="SkillMatch Preview" width="500">
</div>

Lagi bingung cari kerja yang cocok sama kemampuanmu? Tenang, kamu nggak sendiri!  

Di **SkillMatch**, kamu bisa menemukan pekerjaan yang pas banget sama skill dan minatmu. Nggak perlu scroll ratusan lowongan, tinggal tunjukin keahlianmu, dan biar kami bantu temuin kerjaan yang paling cocok buat kamu.  

✨ Temukan pekerjaan yang sesuai dengan skillmu di sini!

```
Developed by:
- Annisa Herliansyah
- Aqib Abdul Aziz
- Muhammad Alwi Rifqi
- Wesley Hakim
```


---
## 📁 Repository Outline
```
    skill-match
    |
    ├── data/
    │   ├── gx_data_context/
    │   ├── data_clean.csv
    │   ├── data_cleaning_validation.ipypnb
    │   ├── job1to5.csv
    │   ├── job6to7.csv
    │   ├── job8to10.csv
    │   ├── job16to20.csv
    │   └── scrapping.ipynb
    ├── deployment/
    │   ├── home.py
    │   ├── logo.png
    │   ├── prediction.py
    │   ├── requirements.txt
    │   └── streamlit_app.py
    ├── logo.png
    ├── README.md
    └── SkillMatch_model_building.ipynb
```
- **skill-match**  
    Repository github ini.

- **data**  
    Folder yang berisi file mengenai pengambilan, pembersihan, dan validasi data.

    - **gx_data_context/**  
    Folder data context dari validasi data library python Great Expectation.

    - **data_clean.csv**  
    Dataset yang digunakan yang telah dibersihkan dari missing value, duplikat, dan hanya berisi teks deskripsi bahasa inggris.

    - **jobXtoY.csv**  
    Dataset bagian X hingga Y, merupakan sebagian dari data keseluruhan.

    - **scrapping.ipynb**  
    Program notebook python yang digunakan untuk melakukan webscraping.

- **deployment**  
    Folder yang berisi file deployment aplikasi web pada huggingface.

    - **home.py**  
    Program python untuk membentuk halaman home aplikasi web.

    - **logo.png**  
    Gambar logo SkillMatch

    - **prediction.py**  
    Program python untuk membentuk halaman prediction aplikasi web.

    - **requirements.txt**  
    Daftar library python yang digunakan untuk deployment di huggingface.

    - **streamlit_app.py**  
    Program python untuk membuat aplikasi web.


- **logo.png**  
    Gambar logo SkillMatch

- **README.md**  
    File dokumentasi yang berisi mengenai overview dan penjelasan repository ini.

- **SkillMatch_model_building.ipynb**  
    Python notebook yang berisi mengenai Latar Belakang, Tujuan, EDA, preprocessing, dan model building dari project


## 🌐 Try it Online

Coba aplikasi **SkillMatch** secara langsung di browser kamu:  
[🔗 Akses SkillMatch](https://huggingface.co/spaces/Annisa123/job_recomendation)

---

## 🎯 Problem Background

Banyak pencari kerja memiliki keahlian luar biasa, namun sering kali kesulitan menemukan pekerjaan yang benar-benar sesuai dengan kemampuan mereka.
Melalui SkillMatch, sistem rekomendasi berbasis AI yang memanfaatkan Natural Language Processing (NLP) dan TF-IDF, pengguna dapat menemukan lowongan yang paling relevan dengan keterampilan mereka.

SkillMatch hadir sebagai jembatan antara skill dan opportunity, dengan menganalisis deskripsi pekerjaan dari berbagai industri untuk membantu setiap individu menemukan pekerjaan yang sesuai dengan potensinya.

---

## 🚀 Project Description

**SkillMatch** menghasilkan sistem rekomendasi pekerjaan interaktif berbasis web yang mampu:  

- Menganalisis kemampuan pengguna dan mencocokkannya dengan deskripsi pekerjaan yang relevan.  
- Mengukur tingkat kemiripan antara input pengguna dan lowongan kerja menggunakan Cosine Similarity.  
- Memberikan hasil rekomendasi beserta tautan pekerjaan asli dari LinkedIn.  
- Melakukan analisis topik pekerjaan menggunakan FASTopic Clustering untuk mengelompokkan jenis pekerjaan berdasarkan pola teks.  

---

## 📊 Data Overview

**Deskripsi singkat:**  
Dataset berisi kumpulan lowongan pekerjaan hasil scraping dari **LinkedIn**, mencakup:  

| No | Kolom            | Deskripsi                     |
|----|------------------|-------------------------------|
| 1  | company_name     | Nama perusahaan               |
| 2  | job_location     | Domisili Perusahaan/Pekerjaan |
| 3  | job_title        | Posisi pekerjaan              |
| 4  | job_description  | Deskripsi pekerjaan           |
| 5  | job_url          | Tautan ke halaman lowongan    |  

---

**Langkah Cleaning & Preprocessing data:**  
1. Menghapus duplikat dan missing value  
2. Mengambil data dengen deskripsi teks berbahasa Inggris saja  
3. Membersihkan teks (lowercase, contractions, non-letter removal, stopwords removal, lemmatization)  
4. Mengubah teks menjadi representasi vektor menggunakan **TF-IDF Vectorizer**

> **Note**: data lowongan kerja LinkedIn ini diambil pada tanggal 31 Oktober 2025 hingga 6 November 2025, besar kemungkinan lowongan kerja tersebut sudah tidak menerima pelamar kerja.
---

## ⚙️ Methodology

Proyek ini menggunakan pendekatan berbasis **Content-Based Filtering** dengan **Cosine Similarity** dan **NLP**.  

**Langkah-langkah utama:**  
1. **Web Scraping** – Mengambil data dari LinkedIn menggunakan Selenium  
2. **Data Validation** – Menggunakan *Great Expectations* untuk menjaga kualitas data  
3. **Text Preprocessing** – Pembersihan dan normalisasi teks deskripsi pekerjaan  
4. **TF-IDF Vectorization** – Mengubah teks menjadi bentuk numerik  
5. **Cosine Similarity** – Mengukur tingkat kesamaan antara skill pengguna dan deskripsi pekerjaan  
6. **FASTopic Clustering** – Mengelompokkan pekerjaan berdasarkan topik  
7. **Web Deployment** – Implementasi sistem rekomendasi dalam aplikasi web interaktif

---

## 🧩 Tech Stack

**Bahasa Pemrograman & Tools:**  
- Python  
- Jupyter Notebook  
- HuggingFace (untuk web application)  

**Library Utama:**  
- `pandas`, `numpy` – Manipulasi data
- `Selenium` – Web scraping
- `nltk`, `re`, `contractions` – Preprocessing teks  
- `scikit-learn` – TF-IDF & Cosine Similarity  
- `matplotlib`, `seaborn`, `WordCloud` – Visualisasi  
- `FASTopic` – Topic Clustering  
- `Great Expectations` – Validasi data
- `Streamlit` – Membuat web app

---

## 🎨 Future Improvement
- Integrasi model BERT/Sentence Transformers untuk rekomendasi yang lebih kontekstual dan akurat.
- Analisis keterampilan otomatis dari CV/resume pengguna untuk mempermudah input skill.
- Dashboard interaktif untuk visualisasi tren pekerjaan, misal: job demand per industri, skill populer.
- Keamanan & privasi data – implementasi enkripsi dan anonimisasi data pengguna.
- Multi-language support – menambahkan dukungan bahasa Indonesia atau bahasa lain agar lebih inklusif.

---

## 📚 Reference

- LinkedIn Job Portal – Cek lowongan langsung di [LinkedIn Jobs](https://www.linkedin.com/jobs)  
- scikit-learn Docs – Panduan TF-IDF & Cosine Similarity di [scikit-learn Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)  
- Great Expectations – Framework untuk validasi data, liat di [Great Expectations Docs](https://docs.greatexpectations.io/docs/home/)  
- FASTopic – Untuk clustering topik pekerjaan, info lengkap di [FASTopic PyPI](https://pypi.org/project/fastopic/) 

---

## 🌟 Contributors

| Name       | LinkedIn | GitHub |
|------------|----------|--------|
| Annisa Herliansyah | [🔗 Connect](https://www.linkedin.com/in/annisa-herliansyah-1a8257287/) | [✅ Follow](https://github.com/Annisa123-lab) |
| Aqib Abdul Aziz | [🔗 Connect](https://www.linkedin.com/in/aqib-az/) | [✅ Follow](https://github.com/aqib-az) |
| Muhammad Alwi Rifqi | [🔗 Connect](https://www.linkedin.com/in/m-alwirifqi/) | [✅ Follow](https://github.com/quadzero1) |
| Wesley Hakim | [🔗 Connect](https://www.linkedin.com/in/wesley-hakim/) | [✅ Follow](https://github.com/wesleyhakim) |
---
## 📝 Berikan Masukan Anda

[💬 Isi Formulir Feedback](https://forms.gle/aJnEeBsktNnLJBrL9)  

Terima kasih telah mencoba **SkillMatch**! 😊  
Setiap saran dan masukan Anda akan sangat berarti bagi pengembangan SkillMatch ke depannya. Terima kasih atas partisipasinya. 🙏✨

---

> ✨ *“Membantu setiap individu menemukan pekerjaan yang sesuai dengan potensinya.”*  
> 🛠️ Built with love by **Group 2** - **RMT047** for data-driven solutions.