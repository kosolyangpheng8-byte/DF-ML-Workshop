import streamlit as st

st.set_page_config(page_title="MyApp", layout="wide")

st.title("🏠 หน้าหลัก ")
st.write("### Boot Camp: Data Science and Machine Learning")
st.info("7 Day Intensive Hands-on Workshop")
st.markdown(''':rainbow[Kosol yangpheng]''')
st.write("##### Day 1: การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")

if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
    st.switch_page("pages/clean_app.py")
    
elif st.button("💰 ระบบคำนวณ"):
    st.switch_page("pages/clean_bbb.py")
    
elif st.button("💰 ระบบ Customers "):
    st.switch_page("pages/clean_customers.py")
