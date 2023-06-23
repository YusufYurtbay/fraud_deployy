import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from PIL import Image
import base64

st.set_page_config(page_title='Fraud Detection')
st.sidebar.image("identity-fraud.jpg", use_column_width=True)
html_temp = """
<div style="background-color:Yellow;padding:10px">
<h2 style="color:blue;text-align:center;font-size: 50px;">Fraud Detection Prediction</h2>
</div><br>"""

st.markdown(html_temp, unsafe_allow_html=True)
original_title = '<p style="font-family:Courier; color:Blue; text-align:center; font-size: 50px;"><b>Select Your Model</b></p>'
st.markdown(original_title, unsafe_allow_html=True)
selection = st.selectbox("", ["final_model"])


st.write( "You selected", selection, "model")
model = pickle.load(open('pickle_model', 'rb'))



# columns = ["v4", ‘v14’, ‘v12’, ‘v10’, ‘v11’]
v4 = st.sidebar.slider(label="V4", min_value=-80.00, max_value=3.00, step=0.01)
v14 = st.sidebar.slider(label="V14", min_value=-6.00, max_value=17.00, step=0.01)
v10 = st.sidebar.slider(label="V10", min_value=-25.00, max_value=24.00, step=0.01)
v11 = st.sidebar.slider("V11", min_value=-19.00, max_value=8.00, step=0.01)
v12 = st.sidebar.slider("V12", min_value=-20.00, max_value=11.00, step=0.01)

feature  = pd.DataFrame({"V4":[v4], "V14":[v14], "V10":[v10], "V11":[v11], "V12":[v12]})

hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """        
st.markdown(hide_table_row_index, unsafe_allow_html=True)   

st.markdown("#### <center>Transaction Information</center>",unsafe_allow_html=True)
st.table(feature)

prediction = model.predict(feature)


st.subheader('Click PREDICT if configuration is OK')

if st.button('PREDICT'):
	if prediction[0]==0:
		st.markdown("![Alt Text](https://media4.giphy.com/media/xTiTnqUxyWbsAXq7Ju/giphy.gif?cid=ecf05e47grau32b1q0m9j9v3ej0z7f2u5h1lfb3vli5hvhbr&ep=v1_gifs_search&rid=giphy.gif&ct=g)")
		st.success(prediction[0])
		st.success(f'Safe transaction done.')
		
        

	elif prediction[0]==1:
		st.markdown("![Alt Text](https://media0.giphy.com/media/hgjNPEmAmpCMM/giphy.gif?cid=ecf05e47mb1nue9xxwroleew595ht26vghqr92jdnvt37djt&ep=v1_gifs_search&rid=giphy.gif&ct=g)")
		
		st.warning(prediction[0])
		st.warning(f'Fraudulent transaction detected.')
		

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
