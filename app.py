# Library
import streamlit as st

# write
st.title('Ini aplikasi koncol')
st.subheader('Anjas')

#input bilangan pertama
number = st.number_input('masukkan bilangan tod')
st.write(f'bilangan pretama  adalah {number}')

#input bilangan kedua
number2 = st.number_input('masukkan bilangan kedua tod')
st.write(f'bilangan kdua adalah {number2}')

hasil=number*number2

if st.button('Hitung'):
    st.write(f'Hasil kali antara {number} dan {number2} adalah {hasil}')
else:
    st.write('Silahkan klik tombol hitung mek!')