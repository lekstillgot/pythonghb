import streamlit as st
# basic
st.title("Hello Streamlit")
st.header("This is Header")
st.subheader("this is subheader")
st.markdown("**This** is Markdown")
st.code("print('Hello Streamlit')", language="python")
st.latex('''(a+b)^2 = a^2 + b^2''')
# button
if st.button("Click Me"):
    st.write("You clicked the button")
else:
    st.write("Please clicked the button")
# input text
data = st.text_input("Please in put data here")
if st.button("Submit"):
    st.write(f"Your data is {data}")

# slider
score = st.slider(
    "Please enter your Score",
    min_value=0,
    max_value=100,
    value=0
)
st.write(f"Your score is {score}")
