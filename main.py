
import streamlit as st
import altair as alt
import numpy as np
import pandas as pd
st.set_page_config(page_title="Inventory Analytics",page_icon=":sunglasses:",initial_sidebar_state='expanded')
st.title("INVENTORY AND SALES ANALYSIS OF SCMS")

df=pd.read_csv("C:\\Users\\ajay\\Downloads\\COGS1.csv")
df=df.drop([0])
x=df.columns
col1,col2,col3=st.beta_columns(3)
with col1:
    item=st.selectbox("Select an Item",options=df[x[0]].values)
with col2:
    slct=st.selectbox("Select a Customised Metric",options=['Inventory','Ratio Analysis'])
with col3:
    chrt=st.selectbox("Select a Chart",options=['Bar','Circle','Area'])
for i in df[x[0]].values:
    if i in item:
        if 'Inventory' in slct:
            result=df.loc[df['Item']==i,[df.columns[j] for j in range(1,7) if j!=4]]
            st.table(result)
            chart_data = pd.DataFrame()
            chart_data['Quantity'] = result.values.ravel()
            chart_data['Inventory'] = result.columns
            if "Bar" in chrt:
                chart_v1 = alt.Chart(chart_data).mark_bar().encode(x='Inventory',y='Quantity',color=alt.value("red")).properties(width=500,height=300)
                st.write("", "", chart_v1)
            elif "Circle" in chrt:
                chart_v2=alt.Chart(chart_data).mark_circle().encode(x='Inventory',y='Quantity',color=alt.value("blue")).properties(width=500,height=300)
                st.write("","",chart_v2)
            else:
                chart_v3=alt.Chart(chart_data).mark_area().encode(x="Inventory",y='Quantity',color=alt.value('green')).properties(width=500,height=300)
                st.write("","",chart_v3)
        else:
            answer=df.loc[df['Item']==i,[df.columns[j] for j in range(4,11) if j!=5 if j!=6]]
            st.table(answer)
