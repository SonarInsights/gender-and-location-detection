import streamlit as st
import joblib
import pandas as pd
import numpy as np
from io import BytesIO
import re
from location_list import locations_mapping
from linguistic_keywords import linguistic_keywords_18_24 
from linguistic_keywords import linguistic_keywords_25_34 
from linguistic_keywords import linguistic_keywords_35_44 
from linguistic_keywords import linguistic_keywords_45_54 
from linguistic_keywords import linguistic_keywords_55_64 
from linguistic_keywords import linguistic_keywords_65_plus 

# Load the model and vectorizer
class GenderPredictor:
    def __init__(self):
        model_path = 'path_needs/file1.pkl'
        vectorizer_path = 'path_needs/file2.pkl'
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)
        self.labels = {1: "male", 0: "female"}

    def predict(self, name: str):
        if not isinstance(name, str) or name.strip() == "":
            return None, 0  # Return None and 0 if the name is not valid

        vector = self.vectorizer.transform([name])
        result = self.model.predict(vector)[0]
        proba = self.model.predict_proba(vector).max()
        return self.labels[result], round(proba * 100, 2)

# Create Streamlit UI
st.title("Gender , Age and Location Prediction App")

# Upload Excel file
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Read the Excel file
    df = pd.read_excel(uploaded_file, sheet_name=0)  # Read the first sheet

    # Check if 'Gender', 'Location', 'Age' column exists, if not, create it
    for col in ['Gender', 'Location', 'Age']:
        if col not in df.columns:
            df[col] = None

    # Hindari warning dtype saat assign string
    df['Location'] = df['Location'].astype('object')

    # Simpan jumlah data sebelum prediksi
    initial_gender_filled = df['Gender'].notna().sum()
    initial_age_filled = df['Age'].notna().sum()
    initial_location_filled = df['Location'].notna().sum()

    # Initialize GenderPredictor
    predictor = GenderPredictor()
    valid_channels = ['Facebook', 'Tiktok', 'Instagram', 'Twitter', 'Youtube']

    # Loop through the rows of the DataFrame
    for index, row in df.iterrows():
        # Gender prediction logic only for selected channels
        author_name = row.get('Author')
        channel_name = str(row.get('Channel')).strip()

        if pd.isna(row['Gender']) and isinstance(author_name, str) and channel_name in valid_channels:
            gender, probability = predictor.predict(author_name)
            if probability > 70:
                df.at[index, 'Gender'] = gender

        # Check for city names or abbreviations
        content = str(row.get('Content', '')).lower()
        found_location = None
        for city, variations in locations_mapping.items():
            for variation in variations:
                if variation in content:
                    found_location = city
                    break
            if found_location:
                break
        if found_location:
            df.at[index, 'Location'] = found_location


    # === Age Prediction ===
    slang_keywords = list(set([
        'anjay', 'wkwk', 'cie', 'gaje', 'gabut', 'mager', 'nongki', 'kepo', 'lebay', 'gila lu', 'yaelah',
        'santuy', 'caper', 'bucin', 'panik ga sih', 'receh', 'ciyee', 'baper', 'ngab', 'ngopi', 'ngabers',
        'fomo', 'flexing', 'healing', 'self-reward', 'auto', 'bestie', 'lo', 'gue', 'btw', 'OOTD', 'OOTN',
        'nolep', 'halu', 'cihuy', 'canda', 'goks', 'mantul', 'syantik', 'demen', 'alay', 'skuy', 'gaskeun',
        'ngablu', 'ngegas', 'pansos', 'julid', 'ngeri', 'ngakak', 'ngenes', 'sabi', 'eaaa', 'apasi',
        'woles', 'cuan', 'nyinyir', 'emang iya', 'kzl', 'idk', 'bruh', 'okey sip', 'ya kan', 'loh', 'lah',
        'lho', 'haha', 'hihi', 'hehe', 'wakaka', 'cuy', 'bro', 'sis', 'bray', 'woke', 'keknya', 'yahud',
        'sekut', 'slebew', 'emesh', 'gemay', 'pede', 'pd banget', 'rempong', 'ngaret', 'cocoklogi',
        'mabar', 'kepo banget', 'ga ngerti', 'ga jelas', 'sok iye', 'lebai', 'basi', 'kudet', 'kekinian',
        'peka', 'php', 'modus', 'bodo amat', 'udah lah', 'gatau', 'susah move on', 'galau', 'curhat'
    ]))

    formal_keywords = list(set([
        'dengan ini', 'berdasarkan', 'diharapkan', 'kepada', 'menginformasikan', 'pengumuman',
        'dalam rangka', 'kami informasikan', 'sehubungan dengan', 'mohon perhatian', 'dimohon untuk',
        'demikian disampaikan', 'mengacu pada', 'sesuai dengan', 'diharapkan untuk', 'terlampir',
        'diberitahukan bahwa', 'kami sampaikan', 'merujuk pada', 'sesuai arahan', 'pengajuan', 'pemberitahuan',
        'pemberlakuan', 'sesuai ketentuan', 'berkenaan dengan', 'kami mohon kerja samanya', 'sesuai prosedur',
        'telah dilakukan', 'mohon konfirmasi', 'perlu kami sampaikan', 'hal tersebut', 'merupakan kewajiban',
        'disampaikan kepada', 'dalam hal ini', 'demi kelancaran', 'kami beritahukan', 'dengan hormat',
        'kami harap', 'harap diperhatikan', 'bapak/ibu', 'sesuai kebijakan', 'dalam waktu dekat',
        'berikut kami sampaikan', 'dalam kesempatan ini', 'sesuai surat', 'mohon ditindaklanjuti',
        'harap segera', 'dengan surat ini', 'segera disampaikan', 'sehubungan dengan hal tersebut',
        'demi kebaikan bersama', 'atas perhatian dan kerja samanya', 'dengan penuh hormat',
        'atas dasar pertimbangan', 'pemberitahuan resmi', 'mohon kerja sama', 'kami lampirkan'
    ]))
    
    df_age = df[df['Channel'].isin(valid_channels) & df['Age'].isna()].copy()
    df_age['Title'] = df_age['Title'].fillna('')
    df_age['Content'] = df_age['Content'].fillna('')
    df_age['Combined_Text'] = df_age.apply(lambda x: f"{x['Title']} {x['Content']}", axis=1)

    def linguistic_score(text):
        text = str(text).lower()
        slang_count = sum(1 for word in slang_keywords if word in text)
        formal_count = sum(1 for word in formal_keywords if word in text)
        total = slang_count + formal_count
        if total == 0:
            return None
        elif slang_count / total > 0.7:
            return '18-24'
        elif formal_count / total > 0.7:
            return '35-44'
        return None

    def topic_based_age(text):
        text = str(text).lower()
        if any(kw in text for kw in ['sekolah', 'kuliah', 'kampus', 'ujian', 'skripsi']):
            return '18-24'
        elif any(kw in text for kw in ['kerja', 'gaji', 'karir', 'pernikahan', 'cicilan', 'keluarga']):
            return '25-34'
        elif any(kw in text for kw in ['bpjs', 'pensiun', 'jantung', 'asam urat', 'diabetes']):
            return '45-54'
        return None

    def gender_channel_based_age(gender, channel):
        gender = str(gender).lower()
        channel = str(channel).lower()
        if channel in ['twitter', 'tiktok'] and gender == 'male':
            return '18-24'
        elif channel in ['facebook', 'youtube'] and gender == 'female':
            return '35-44'
        elif channel == 'instagram' and gender == 'female':
            return '25-34'
        return None

    df_age['Age_Linguistic'] = df_age['Combined_Text'].apply(linguistic_score)
    df_age['Age_Topic'] = df_age.apply(
        lambda x: topic_based_age(x['Combined_Text']) if pd.isna(x['Age_Linguistic']) else None,
        axis=1
    )
    df_age['Age_Gender_Channel'] = df_age.apply(
        lambda x: gender_channel_based_age(x['Gender'], x['Channel']) if pd.isna(x['Age_Linguistic']) and pd.isna(x['Age_Topic']) else None,
        axis=1
    )

    def final_age(row):
        if pd.notna(row['Age_Linguistic']):
            return row['Age_Linguistic']
        elif pd.notna(row['Age_Topic']):
            return row['Age_Topic']
        elif pd.notna(row['Age_Gender_Channel']):
            return row['Age_Gender_Channel']
        return None

    df_age['Predicted_Age'] = df_age.apply(final_age, axis=1)
    df.loc[df_age.index, 'Age'] = df_age['Predicted_Age']
    
    
    # Show the updated DataFrame
    st.write("Updated DataFrame:")
    st.dataframe(df[['Title', 'Content', 'Gender', 'Channel', 'Age']].head(20))

    # Calculate summary
    gender_counts = df['Gender'].value_counts(normalize=True) * 100
    location_counts = df['Location'].value_counts(normalize=True) * 100

    # Display summary
    st.write("### Summary")

    # Summary of total filled
    filled_gender = df['Gender'].notna().sum()
    filled_age = df['Age'].notna().sum()
    filled_location = df['Location'].notna().sum()

    st.markdown(f"**Filled Data Count:**")
    st.markdown(f"- Gender: {filled_gender} data (before {initial_gender_filled} data)")
    st.markdown(f"- Age: {filled_age} data (before {initial_age_filled} data)")
    st.markdown(f"- Location: {filled_location} data (before {initial_location_filled} data)")


    st.markdown("**Persentase Gender:**")
    gender_data = df[df['Gender'].notna()]
    gender_counts = gender_data['Gender'].value_counts()
    gender_total = gender_counts.sum()
    for label in ['male', 'female']:
        count = gender_counts.get(label, 0)
        percent = (count / gender_total) * 100 if gender_total else 0
        st.markdown(f"- {label.capitalize()}: {percent:.2f}%")



    st.markdown("\n**Persentase Age:**")
    age_data = df[df['Age'].notna()]
    age_counts = age_data['Age'].value_counts()
    age_total = age_counts.sum()
    for age in ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']:
        count = age_counts.get(age, 0)
        percent = (count / age_total) * 100 if age_total else 0
        st.markdown(f"- {age} : {percent:.2f}%")


    st.markdown("\n**Top Location (max top 20):**")
    top_locations = df['Location'].value_counts().head(20)
    st.write("| Name Location | Persentase | Mention |")
    st.write("|---------------|------------|---------|")
    total_location = df['Location'].notna().sum()
    for loc, count in top_locations.items():
        percent = (count / total_location) * 100 if total_location > 0 else 0
        st.write(f"| {loc} | {percent:.2f}% | {count} |")

    # === Export ===
    excel_buffer = BytesIO()
    with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Sheet1")
    excel_buffer.seek(0)

    st.download_button(
        label="Download Updated File",
        data=excel_buffer,
        file_name="updated_gender_location_age.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    
else:
    st.write("Please upload an Excel file to proceed.")
