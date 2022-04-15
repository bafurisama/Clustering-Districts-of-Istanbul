import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
st.set_page_config(layout="wide")
st.title("""
 Clustering Analysis Dashboard 
""")


df1 = pd.read_csv('Rare.csv',index_col="District") # cluster1
df2 = pd.read_csv('Medium.csv',index_col="District") # cluster2
df3 = pd.read_csv('Well-done.csv',index_col="District") # cluster3


st.sidebar.header('User Input Features')
option = st.sidebar.selectbox(
     'Please choose your grouped districts',
     ('Rare Group', 'Medium Group', 'Well-done Group'))

st.sidebar.write('You selected:', option)

st.subheader("""Summary""")

# metrics
with st.container():
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        if option == 'Rare Group':
            st.metric(label = "Average Total Competitors",value=round(df1["Total_Competitors"].mean()))
        elif option == 'Medium Group':
            st.metric(label = "Average Total Competitors",value=round(df2["Total_Competitors"].mean()))
        else:
            st.metric(label = "Average Total Competitors",value=round(df3["Total_Competitors"].mean()))
    with col2:
        if option == 'Rare Group':
            st.metric(label = "Average Total Venues",value=round(df1["Total_Venues"].mean()))
        elif option == 'Medium Group':
            st.metric(label = "Average Total Venues",value=round(df2["Total_Venues"].mean()))
        else:
            st.metric(label = "Average Total Venues",value=round(df3["Total_Venues"].mean()))

    with col3:
        if option == 'Rare Group':
            st.metric(label = "Average Population",value=round(df1["Population"].mean()))
        elif option == 'Medium Group':
            st.metric(label = "Average Population",value=round(df2["Population"].mean()))
        else:
            st.metric(label = "Average Population",value=round(df3["Population"].mean()))

    with col4:
        if option == 'Rare Group':
            st.metric(label = "Average Annual Income (₺)",value=round(df1["Annual_Income"].mean()))
        elif option == 'Medium Group':
            st.metric(label = "Average Annual Income (₺)",value=round(df2["Annual_Income"].mean()))
        else:
            st.metric(label = "Average Annual Income (₺)",value=round(df3["Annual_Income"].mean()))



if option == 'Rare Group':
    st.subheader("Rare")
    st.write("""
     This group has the lowest venue and people who live in
     these districts has average annual income. Their population is also lower than others in general.""")
elif option == 'Medium Group':
    st.subheader("Medium")
    st.write("""Districts in this group has higher population compared to rare segment. There are many food venue. Annual income of this group is average of entire boroughs. It is a middle segment group of our analysis.""")
else:
    st.subheader("Well-done")
    st.write("""
This group has higher number of venues and annual income. There are many Transportation ,Food Venues, Nightlife Spots in this group. If average price of menu is expensive. We can choose to start with this group.
          """)


# expander
with st.expander("See Dataframe"):
        if option == 'Rare Group':
            st.dataframe(df1)
        elif option == 'Medium Group':
            st.dataframe(df2)
        else:
            st.dataframe(df3)



#container1
with st.container():
    col1,col2 = st.columns(2)
    with col1: # bar chart for Annual Income
        if option == 'Rare Group':
            st.subheader("Annual Income of Rare Group")
            fig = px.bar(df1.sort_values(by = "Annual_Income",ascending=False), x=df1.reset_index()["District"], y='Annual_Income')
            st.plotly_chart(fig,use_container_width=True)
        elif option == 'Medium Group':
            st.subheader("Annual Income of Medium Group")
            fig = px.bar(df2.sort_values(by = "Annual_Income",ascending=False), x=df2.reset_index()["District"], y='Annual_Income')
            st.plotly_chart(fig,use_container_width=True)
        else:
            st.subheader("Annual Income of Welldone Group")
            fig = px.bar(df3.sort_values(by = "Annual_Income",ascending=False), x=df3.reset_index()["District"], y='Annual_Income')
            st.plotly_chart(fig,use_container_width=True)
    with col2: # pie chart for population
        with st.container():
            if option == 'Rare Group':
                st.subheader("Population of Rare Group")
                fig = px.pie(df1, values='Population',names = df1.reset_index()["District"])
                st.plotly_chart(fig,use_container_width=True)
            elif option == 'Medium Group':
                st.subheader("Population of Medium Group")
                fig = px.pie(df2, values='Population',names = df2.reset_index()["District"])
                st.plotly_chart(fig,use_container_width=True)
            else:
                st.subheader("Population of Welldone Group")
                fig = px.pie(df3, values='Population',names = df3.reset_index()["District"])
                st.plotly_chart(fig,use_container_width=True)
#container2
with st.container():
    col1,col2 = st.columns(2)
    with col1:  # bar chart for Total Venues
        if option == 'Rare Group':
            st.subheader("Total Venues of Rare Group")
            fig = px.bar(df1.sort_values(by = "Total_Venues",ascending=False), x=df1.reset_index()["District"], y='Total_Venues')
            fig.update_traces(marker_color='#17becf')
            st.plotly_chart(fig,use_container_width=True)

        elif option == 'Medium Group':
            st.subheader("Total Venues of Medium Group")
            fig = px.bar(df2.sort_values(by = "Total_Venues",ascending=False), x=df2.reset_index()["District"], y='Total_Venues')
            fig.update_traces(marker_color='#17becf')
            st.plotly_chart(fig,use_container_width=True)
        else:
            st.subheader("Total Venues of Welldone Group")
            fig = px.bar(df3.sort_values(by = "Total_Venues",ascending=False), x=df3.reset_index()["District"], y='Total_Venues')
            fig.update_traces(marker_color='#17becf')
            st.plotly_chart(fig,use_container_width=True)
    with col2: # Total Competitors bar chart
        with st.container():
            if option == 'Rare Group':
                st.subheader("Total Competitors of Rare Group")
                fig = px.bar(df1.sort_values(by = "Total_Competitors",ascending=False), x=df1.reset_index()["District"], y='Total_Competitors')
                fig.update_traces(marker_color='slateblue')
                st.plotly_chart(fig,use_container_width=True)
            elif option == 'Medium Group':
                st.subheader("Total Competitors of Medium Group")
                fig = px.bar(df2.sort_values(by = "Total_Competitors",ascending=False), x=df2.reset_index()["District"], y='Total_Competitors')
                fig.update_traces(marker_color='red')
                st.plotly_chart(fig,use_container_width=True)
            else:
                st.subheader("Total Competitors of Welldone Group")
                fig = px.bar(df3.sort_values(by = "Total_Competitors",ascending=False), x=df3.reset_index()["District"], y='Total_Competitors')
                fig.update_traces(marker_color='red')
                st.plotly_chart(fig,use_container_width=True)
