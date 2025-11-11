import streamlit as st
import pandas as pd
import numpy as np
import re
import contractions
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastopic import FASTopic

# Download NLTK
nltk.download('punkt_tab', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
nltk.download('omw-1.4', quiet=True)

def run():
    st.title("🔎 Temukan Pekerjaan yang Cocok untuk Kamu")
    st.caption("Masukkan skill atau kemampuanmu, dan biarkan AI mencari pekerjaan terbaik untukmu 💼")

    # Load Dataset 
    @st.cache_data
    def load_data(path="./src/data_clean.csv"):
        df = pd.read_csv(path)
        df.fillna("", inplace=True)
        return df

    df = load_data()

    # Preprocessing 
    stpwds_en = set(stopwords.words('english'))
    stpwds_en = stpwds_en.union({'about', 'the', 'job'})
    lemmatizer = WordNetLemmatizer()

    def get_wordnet_pos(tag):
        if tag.startswith('J'):
            return 'a'
        elif tag.startswith('V'):
            return 'v'
        elif tag.startswith('N'):
            return 'n'
        elif tag.startswith('R'):
            return 'r'
        else:
            return 'n'

    def lemmatize_text(token_list):
        tagged_tokens = pos_tag(token_list)
        return [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in tagged_tokens]

    def text_preprocessing(text):
        text = text.lower()
        text = contractions.fix(text)
        text = re.sub(r"\n", " ", text)
        text = re.sub(r"[^A-Za-z\s]", " ", text)
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word not in stpwds_en and len(word) > 1]
        tokens = lemmatize_text(tokens)
        tokens = [word for word in tokens if word not in stpwds_en and len(word) > 1]
        return ' '.join(tokens)

    # TF-IDF
    @st.cache_resource
    def train_tfidf(df):
        df['text_for_tfidf'] = (df['job_title'] + ' ' + df['job_description']).apply(text_preprocessing)
        corpus = df['text_for_tfidf'].astype(str).tolist()
        tfidf_vectorizer = TfidfVectorizer(max_df=0.90, ngram_range=(1, 2))
        tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
        return tfidf_vectorizer, tfidf_matrix, df

    tfidf_vectorizer, tfidf_matrix, df = train_tfidf(df)

    # Fungsi Rekomendasi 
    def get_sentence_vector(sentence):
        preprocessed = text_preprocessing(sentence)
        return tfidf_vectorizer.transform([preprocessed])

    def recommend_jobs(user_input, top_n=10):
        input_vector = get_sentence_vector(user_input)
        similarities = cosine_similarity(input_vector, tfidf_matrix).flatten()
        top_indices = similarities.argsort()[-top_n:][::-1]
        recommendations = df.iloc[top_indices][['job_title', 'company_name', 'job_url', 'job_description']].copy()
        recommendations['similarity'] = similarities[top_indices]
        return recommendations

    # Input Pengguna 
    st.markdown("### 🧠 Masukkan Skill Kamu")
    user_input = st.text_area("Contoh: `communication, teamwork, python, data analysis`", height=100)

    if st.button("🎯 Cari Pekerjaan yang Cocok"):
        if user_input.strip() == "":
            st.warning("Silakan isi kemampuan kamu terlebih dahulu.")
        else:
            with st.spinner("🔍 Mencarikan pekerjaan terbaik untukmu..."):
                df_result = recommend_jobs(user_input, top_n=20)
                if df_result.empty or (len(df_result['similarity'].unique()) == 1 and df_result['similarity'].unique()[0] == 0):
                    st.info("Maaf, tidak ada pekerjaan yang cocok ditemukan.")
                else:
                    if len(df_result) >= 3:
                        # Clustering dengan FASTopic
                        model = FASTopic(num_topics=3)
                        job_texts = (df_result['job_title'] + ' ' + df_result['job_description']).tolist()
                        top_words, doc_topic_dist = model.fit_transform(job_texts)
                        doc_topic_dist = np.array(doc_topic_dist)

                        df_result['cluster'] = np.argmax(doc_topic_dist, axis=1)
                        df_result['cluster_prob'] = np.max(doc_topic_dist, axis=1)
                        index_cluster = 0
                        st.success(f"Ditemukan {len(df_result)} pekerjaan dalam {len(df_result['cluster'].unique())} group berbeda yang cocok dengan kemampuanmu!")
                        for cluster_id in df_result['cluster'].unique():
                            job_cluster_list = df_result.query(f'cluster == {cluster_id}').sort_values(by='similarity', ascending=False)
                            with st.expander(f"💡 Group {index_cluster + 1}"):
                                st.caption(f"Menampilkan {len(job_cluster_list)} pekerjaan untuk group ini.")
                                for i, row in job_cluster_list.iterrows():
                                    st.markdown(f"### {row['job_title']} — {row['company_name']}")
                                    st.markdown(f"[🌐 Lihat Detail Pekerjaan]({row['job_url']})")
                                    st.caption(f"**Similarity:** {row['similarity']:.2f}")
                                    st.markdown("📋 **Deskripsi Pekerjaan:**")
                                    st.write(row['job_description'])
                                    st.markdown("---")
                            index_cluster += 1
                    else:
                        st.success(f"Ditemukan {len(df_result)} pekerjaan yang cocok dengan kemampuanmu!")
                        for i, row in df_result.iterrows():
                            with st.expander(f"{row['job_title']} — {row['company_name']}"):
                                st.markdown(f"[🌐 Lihat Detail Pekerjaan]({row['job_url']})")
                                st.caption(f"**Similarity:** {row['similarity']:.2f}")
                                st.markdown("📋 **Deskripsi Pekerjaan:**")
                                st.write(row['job_description'])
                                st.markdown("---")


if __name__ == "__main__":
    run()