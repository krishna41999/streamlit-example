import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from datetime import date, timedelta
import time

st.set_page_config(
    page_title = 'Twitter Scraper',
    page_icon = ':twitter_bird:',
    layout = "centered",
    initial_sidebar_state = "expanded",
    menu_items = {
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     })

st.title("A.V.C. College of Engineering")

st.header("Computer Science DEpartment")

st.subheader("Nan Muthalvan - ChatGPT")

st.text("Hello World")

st.markdown("""Hello World""")

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
 }))

# Creating a 3 x 4 numpy array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Creating a dictionary
dct = {"name": ["Alice", "Bob", "Charlie", "David"],
       "age": [25, 30, 35, 40],
       "city": ["New York", "Los Angeles", "Chicago", "Houston"]}

# Creating a pandas DataFrame
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9], "D": [10, 11, 12]})

st.write(arr)
st.write(dct)
st.write(df)

st.dataframe(dct)

st.table(dct)
st.json(dct)

data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ["A", "B", "C"]
)

st.line_chart(data)

st.bar_chart(data)

st.area_chart(data)


fig, ax = plt.subplots()
ax.scatter(data["A"], data["B"])

st.pyplot(fig)          # No need of plt.show() here as we are running it over streamlit

df = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width = True)

if st.button("Subscribe"):
    st.write("Like this video too")

name = st.text_input("Name", "Default Value if any", 15, placeholder = "Enter your name here")
st.write(name)

txt = st.text_area('Text to analyze', '''
        It was the best of times, it was the worst of times, it was 
        the age of wisdom, it was the age of foolishness, it was
        the epoch of belief, it was the epoch of incredulity, it
        was the season of Light, it was the season of Darkness, it
        was the spring of hope, it was the winter of despair, (...)
        ''')


col1, col2 = st.columns(2)

with col1:
    st.date_input("Enter starting date", date.today() - timedelta(days = 182))
    
with col2:
    col2.date_input("Enter ending date")  



col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")


st.image([
    "https://static.streamlit.io/examples/cat.jpg",
    "https://static.streamlit.io/examples/dog.jpg",
    "https://static.streamlit.io/examples/owl.jpg"
], ["Cat", "Dog", "Owl"])


st.time_input("Enter time here")

if st.checkbox("I agree to the T & C of the agreement"):
    st.write("Thank you")

v1 = st.radio("Colors", ["r", "g", "b"], index = 0)            # Default is 'r' as index = 0 

v2 = st.selectbox("Colors", ["r", "g", "b"], index = 2)

st.write(v1.upper(), v2.upper())

v3 = st.multiselect("Colors", ["r", "g", "b"])

st.write(v3)

v4 = st.slider("Age",min_value = 1, max_value = 1000, value = 1, step = 1)
st.write(v4)

v5 = st.number_input("Age",min_value = 1, max_value = 1000, value = 1, step = 1)
st.write(v5)

v6 = st.file_uploader("Upload a file", "jpg", True)
st.image(v6)



data = {
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}


sel = st.sidebar.selectbox("Select a number", [1,2,3,4,5])

rad = st.sidebar.radio("Navigation",["Home","About Us"])

if rad == "Home":

    df = pd.DataFrame(data)
    col = st.sidebar.multiselect("Select a Column", df.columns)

    plt.style.use("ggplot")
    fig, ax = plt.subplots()
    ax.plot(df["num"], df[col])
    st.pyplot(fig)

if rad == "About Us":
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)
         
    st.balloons()
    st.error("Error")
    st.success("Show Success")
    st.info("Information")
    st.exception(RuntimeError("this is an error"))
    st.warning("this is a warning")