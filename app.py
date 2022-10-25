# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd


st.title("Project on BTRC Data Analysis")
st.subheader("A small project By Mahedi")

upload = st.file_uploader("Upload Your Dataset (In CSV Format)")

if upload is not None:
    data=pd.read_csv(upload,error_bad_lines=False,skiprows = 9)
    data=data.dropna(how='any',axis=0)

    data = data[data.Inbound != 0] 
    data['Date']= pd.to_datetime(data['Date'])
    a=data.groupby(data['Date'].dt.strftime('%B'))['Outbound'].mean()
    b=data.groupby(data['Date'].dt.strftime('%B'))['Inbound'].mean()
    data1 = pd.DataFrame(b)
    data1['Inbound']=b
    data1['Outbound']=a
    data1['Outbound']= data1['Outbound'].floordiv(1000000)
    data1['Inbound']= data1['Inbound'].floordiv(1000000)
    pd.options.display.float_format = '{:.0f}'.format    
    
# 3. Show Dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
            st.write(data1)
            st.success("You Have Seen Average Data By Month ")
            
            
print(st.__version__)
print(pd.__version__)

