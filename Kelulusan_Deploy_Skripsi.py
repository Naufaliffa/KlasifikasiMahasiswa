# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:38:20 2024

@author: ACER
"""


import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time
import base64

st.set_page_config(
  page_title = "Klasifikasi Kelulusan Mahasiswa",
#  page_icon = ":heart:"
)

# tampilan web
st.write(""" # Klasifikasi Kelulusan Mahasiswa (Web Apps)
Aplikasi berbasis Web untuk memprediksi (mengklasifikasi)
Ketepatan Waktu Kelulusan Mahasiswa""")


def input_user():
    st.sidebar.text('')
    st.sidebar.header("User Input Sidebar")
    
    JenisKelamin = st.sidebar.selectbox('**Jenis Kelamin**', ('0', '1'))
    st.sidebar.write('Perempuan = 0, Laki-laki = 1')
    st.sidebar.write("")

    JalurPendaftaran = st.sidebar.selectbox('**Jalur Pendaftaran**', ('0', '1'))
    st.sidebar.write('Reguler = 0, PMDK = 1')
    st.sidebar.write("")
    
    Prestasi = st.sidebar.selectbox('**Prestasi**', ('0', '1'))
    st.sidebar.write('Apakah memiliki Pretasi')
    st.sidebar.write("")

    Umur = st.sidebar.number_input('**Umur**', min_value=0, step=1)
    st.sidebar.write('Usia saat melakukan pendaftaran')   
    st.sidebar.write("")

    IPS1 = st.sidebar.number_input('**IPS 1**', min_value=0.00,
    max_value=4.00)
    st.sidebar.write(":orange[Min] value: :orange[0], :red[Max] value: :red[4]")
    st.sidebar.write("")

    IPS2 = st.sidebar.number_input('**IPS 2**', min_value=0.00,
    max_value=4.00)
    st.sidebar.write(":orange[Min] value: :orange[0], :red[Max] value: :red[4]")
    st.sidebar.write("")

    IPS3 = st.sidebar.number_input('**IPS 3**', min_value=0.00,
    max_value=4.00)
    st.sidebar.write(":orange[Min] value: :orange[0], :red[Max] value: :red[4]")
    st.sidebar.write("")

    IPS4 = st.sidebar.number_input('**IPS 4**', min_value=0.00,
    max_value=4.00)
    st.sidebar.write(":orange[Min] value: :orange[0], :red[Max] value: :red[4]")
    st.sidebar.write("")
    
    IPS5 = st.sidebar.number_input('**IPS 5**', min_value=0.00,
    max_value=4.00)
    st.sidebar.write(":orange[Min] value: :orange[0], :red[Max] value: :red[4]")
    st.sidebar.write("")

 
      
    data = {'JenisKelamin' : JenisKelamin,
            'JalurPendaftaran' : JalurPendaftaran,
            'Prestasi' : Prestasi,
            'Umur' : Umur,
            'IPS1' : IPS1,
            'IPS2' : IPS2,
            'IPS3' : IPS3,
            'IPS4' : IPS4,
            'IPS5' : IPS5}
    fitur = pd.DataFrame(data, index=[0])
    return fitur
inputan = input_user()
        
df = inputan
# Menampilkan parameter hasil inputan
st.subheader('Parameter Inputan')
#membuat tab
tab1, tab2, tab3 = st.tabs(["Predict", "Multi-Predict", "About"])
with tab1:
    
    st.write(inputan)
    
    predict_btn = st.button("**Predict**", type="primary")
    result = ":violet[-]"
    
    
    if predict_btn:
        bar = st.progress(0)
        status_text = st.empty()
    
        for i in range(1, 101):
          status_text.text(f"{i}% complete")
          bar.progress(i)
          time.sleep(0.01)
          if i == 100:
            time.sleep(1)
            status_text.empty()
            bar.empty()
        
        # Load save model
        load_model = pickle.load(open('knn_model_skripsi.pkl', 'rb'))
        
        # Terapkan Random Forest
        prediction = load_model.predict(df)
        StatusKelulusan = np.array(['Terlambat', 'Tepat'])
            
        #st.subheader('Hasil Prediksi (Klasifikasi) Waktu Kelulusan Mahasiswa')
        
        #st.write(StatusKelulusan[prediction])
        
        if prediction == 0:
          result = ":red[**Terlambat**]"
        elif prediction == 1:
          result = ":green[**Tepat Waktu**]"

        st.write("")
        st.subheader("Prediksi Mahasiswa:")
        st.subheader(result)   
        
        
                
with tab2:       
    st.header("Predict multiple data:")
    
    excel_path = "sample_data_test_update.xlsx"
    
    if st.button("Download Existing Dataset (Excel)"):
        with open(excel_path, "rb") as f:
            excel_data = f.read()
            b64 = base64.b64encode(excel_data).decode()
            href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{excel_path.split("/")[-1]}">Download Excel File</a>'
            st.markdown(href, unsafe_allow_html=True)
    
    st.header('Upload your Excel file')
    upload_file = st.file_uploader('', )
    if upload_file is not None:
        df = pd.read_excel(upload_file)
        
        bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(1, 101):
          status_text.text(f"{i}% complete")
          bar.progress(i)
          time.sleep(0.02)
          
          if i == 100:
            # Jika progress telah mencapai 100%, kita akan menghapus progress bar
            bar.empty()
            # Kita juga bisa mengubah teks status untuk memberi tahu pengguna bahwa proses telah selesai
            status_text.text(" ")
            # Load save model
            load_model = pickle.load(open(knn_model_skripsi.pkl', 'rb'))
            # Terapkan Random Forest
            prediction = load_model.predict(df)
            
            StatusKelulusan = np.array(['Terlambat', 'Tepat'])
            
            st.subheader('Hasil Prediksi (Klasifikasi) Waktu Kelulusan Mahasiswa')
            hasil = StatusKelulusan[prediction]
            
            col1, col2 = st.columns([1, 6])

            with col1:
              st.dataframe(hasil)
            with col2:
              st.dataframe(df) 
            
  
    else:
        st.write('Waiting for the excel file to upload..')
        
   
      
with tab3:
    st.title("About Apps")
    st.write("Halaman ini memberikan informasi dasar tentang aplikasi yang dibuat.")
    
    st.header("Informasi Aplikasi")
    st.write("Tujuan aplikasi ini yaitu untuk dapat memprediksi apakah mahasiswa akan lulus tepat waktu atau tidak")
    st.write("Aplikasi ini dikembangkan dengan menggunakan Streamlit, sebuah framework Python untuk membuat aplikasi web interaktif.")
    st.write("Untuk fitur pada aplikasi saat ini yaitu, memprediksi kelulusan mahasiswa dengan data tunggal serta memprediksi kelulusan mahasiswa dengan data banyak sekaligus")
    
    
    
    st.markdown("---")  # Garis pemisah
    st.markdown("Created by: [Naufal Iffa Maulana Ramadhan](https://www.linkedin.com/in/naufal-iffa-maulana-ramadhan-19982b245/)")
    
  
    
    
    
      
