import streamlit as st

st.balloons()

st.title("🙌Hi, my name is :blue[Liu Yang]")
st.title("Here is my profile page :sunglasses:")

col1, col2= st.columns(2)

with col1:
    st.image("./images/photo.jpg")
with col2:
    st.header("I'm a :red[UI & UX] Designer")
    st.header("About Me 👨‍🎤")
    st.markdown("""
            - School📙:
                - Beijing University of Technology
                - University of Washington
            - Major 🛠: 
                - Industrial Design
                - UI & UX Design
            - Skill:  
                - 3D Modeling
                - Prototyping
                - User Research

""")
col3, col4 = st.columns(2)
with col3:
    st.header(":rainbow[Work Experience]")  
    st.markdown("""
- Luckin Coffee ☕
- Madame Tussauds Beijing 🎓
- Net Ease 👔              
""")
with col4:
    st.header(":rainbow[Hobby & Interest]")  
    st.markdown("""
- Soccer ⚽
- Video Game 🎮
- Dog 🐶   
""")

st.header("Interesting Projects")
st.header(":orange[OOK]")  
st.image("./images/OOK.png")
st.header(":blue[IMASAZ]")  
st.image("./images/photo1.png")