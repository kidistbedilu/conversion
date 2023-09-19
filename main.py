import streamlit as st

st.title('conversion')
st.markdown('')

def MBps_to_Mbps():
    st.session_state.Mbps = st.session_state.MBps*0.125

def Mbps_to_MBps():
    st.session_state.MBps = st.session_state.Mbps/0.125

#col1, buff, col2 = st.columns([2,1,2])
col1, buff, col2 = st.columns(3)
with col1:
    megabyte = st.number_input('Megabyte per second (MBps):', key='MBps', on_change = MBps_to_Mbps)

with col2:
    megabit = st.number_input('Megabit per second (Mbps):', key='Mbps', on_change = Mbps_to_MBps)
