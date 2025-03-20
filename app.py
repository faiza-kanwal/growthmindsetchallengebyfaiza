import streamlit as st

st.set_page_config (page_title= "growth mindset project", page_icon="✨")
st.title("Growth Mindset Challenge : Web App with Streamlit")

st.header("Welcome to your growth journey!")
st.write("Embrace challenge, learn from mistakes,and unllock your full potential. this AI-powered app help")

# quote section
st.header("💡 Today's Growth Mindset Quote")
st.write ("Success is not final,failure is not fatal,it is the courage to continue that counts.")

st.header("🔧What is your challenge Today?")
user_input= st.text_input("Describe a challenge you are facing:")

# condition
if user_input:
    st.success(f"you are facing:{user_input}.keep pushing forward towards your goal!🚀")
else:
    st.warning("Tell us about your challenge to get started!")

# reflexing


st.header("Reflect on your learning")
reflection= st.text_area("Write your reflection here")

if reflection:
    st.success(f"Great Insight! Your reflection:{reflection}")
else:
    st.info("Reflecting on past experience help you grow ! Share you difficulties")

# acheivements
st.header("🎉Celebrate Your Wins!")
achievement= st.text_input("Share something you have recently accomplished:")

if achievement:
    st.success(f"🎉Amazing! You achieved : {achievement}")
else :
    st.info("Big or small, every achievement counts! Share one now❤")

# footer
st.write("---")
st.write("Keep beleive in yourself .Growth is a journey , not a destination! ⭐")
st.write("**created by Faiza Kanwal**" )