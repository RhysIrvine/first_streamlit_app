import streamlit
import pandas

streamlit.title('Healthy Diner')
streamlit.header('Breakfast  Favorites')
streamlit.text('🥣Protein Punch')
streamlit.text('🐔Yoked Egg')
streamlit.text('🥗Klassic Kale')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
