import streamlit as st
import pickle
import pandas as pd
import time
import streamlit.components.v1 as components

df = pd.read_pickle('my_dataframe2.pkl')

with open('simmilarity2.pkl', 'rb') as file_object:
        sim= pickle.load(file_object)
op={
    df.iloc[0].Title:df.iloc[0].URL,
    df.iloc[1].Title:df.iloc[1].URL,
    df.iloc[2].Title:df.iloc[2].URL,
    df.iloc[3].Title:df.iloc[3].URL,
    df.iloc[4].Title:df.iloc[4].URL,
    df.iloc[5].Title:df.iloc[5].URL,
    df.iloc[6].Title:df.iloc[6].URL,
    df.iloc[7].Title:df.iloc[7].URL,
    df.iloc[8].Title:df.iloc[8].URL,
    df.iloc[9].Title:df.iloc[9].URL,
    df.iloc[10].Title:df.iloc[10].URL
}
def recommend(newss):
        news_idx= df[df['Title']== newss].index[0]
        lit=sorted(list(zip(df['Title'].tolist(),sim[news_idx].tolist())),reverse=True,key=lambda x:x[1])[1:6]
        reco={}
        for i in lit:
            x=df[df['Title']==i[0]].index[0]
            if (x!=news_idx):
                reco[df.iloc[x].Title]=df.iloc[x].URL
        return reco


if "url_options" not in st.session_state:
    st.session_state.url_options =op
if "selected_option" not in st.session_state:
    st.session_state.selected_option = None
if "iframe_url" not in st.session_state:
    st.session_state.iframe_url = None

st.title('News recommender System')
placeholder2 = st.empty()
selected_option=placeholder2.radio("Recommended articles:", list(st.session_state.url_options.keys()),index=None)
st.session_state.selected_option=selected_option
placeholder = st.empty()
   
while(selected_option==None):
        time.sleep(1)
    
st.session_state.selected_option=selected_option

st.session_state.url_options =recommend(st.session_state.selected_option)
placeholder.empty()
placeholder2.empty()
selected_option=placeholder2.radio("Recommended articles:", list(st.session_state.url_options.keys()),index=None)
placeholder.title(f"{st.session_state.selected_option}")
st.session_state.iframe_url = df.iloc[df[df['Title']==st.session_state.selected_option].index[0]].URL

st.components.v1.iframe(st.session_state.iframe_url, height=600, scrolling=True)
 


