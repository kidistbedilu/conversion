import streamlit as st

st.title('conversion')
st.markdown('')

def MBps_to_Mbps():
    st.session_state.Mbps = st.session_state.MBps*0.125

def Mbps_to_MBps():
    st.session_state.MBps = st.session_state.Mbps/0.125

def h_to_d():
    st.session_state.d = st.session_state.h/24

def d_to_h():
    st.session_state.h = st.session_state.d*24

def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs/2.2046

def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg*2.2046

def inn_to_cm():
    st.session_state.cm = st.session_state.inn*2.54

def cm_to_inn():
    st.session_state.inn = st.session_state.cm/2.54

def c_to_f():
    st.session_state.f = (st.session_state.c*9/5)+32

def f_to_c():
    st.session_state.c = (st.session_state.f-32)*5/9

st.markdown('##### Data')
#col1, buff, col2 = st.columns([2,1,2])
col1, buff, col2 = st.columns(3)
with col1:
    megabyte = st.number_input('Megabyte per second (MBps):', key='MBps', on_change = MBps_to_Mbps)

with col2:
    megabit = st.number_input('Megabit per second (Mbps):', key='Mbps', on_change = Mbps_to_MBps)
st.markdown('***')

st.markdown('##### Time')
col3, buff, col4 = st.columns(3)
with col3:
    hour = st.number_input('Hour (h):', key='h', on_change = h_to_d)

with col4:
    day = st.number_input('Day (d):', key='d', on_change = d_to_h)
st.markdown('***')

st.markdown('##### Weight')
col5, buff, col6 = st.columns(3)
with col5:
    pounds = st.number_input('Pounds (lbs):', key='lbs', on_change = lbs_to_kg)

with col6:
    kilogram = st.number_input('Kilograms (kg):', key='kg', on_change = kg_to_lbs)
st.markdown('***')

st.markdown('##### Length')
col7, buff, col8 = st.columns(3)
with col7:
    inch = st.number_input('Inch (in):', key='inn', on_change = inn_to_cm)

with col8:
    centimeter = st.number_input('Centimeter (cm):', key='cm', on_change = cm_to_inn)
st.markdown('***')

st.markdown('##### Temperature')
col9, buff, col10 = st.columns(3)
with col9:
    celsius = st.number_input('Celsius (\N{DEGREE SIGN}C):', key='c', on_change = c_to_f)

with col10:
    fahrenheit = st.number_input('Fahrenheit (\N{DEGREE SIGN}F):', key='f', on_change = f_to_c)
