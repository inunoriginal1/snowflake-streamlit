import streamlit as st

st.title("My Parent's New Healthy Diner")

st.header("Breakfast Favourites")
st.text("🥣 Omega 3 & Blueberry Oatmeal")
st.text("🥗 Kale, Spinach & Rocket Smoothie")
st.text("🐔 Hard-Boiled, Free-Range Egg")
st.text("🥑🍞 Avocado Toast")

st.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ["Avocado", "Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.dataframe(fruits_to_show)

#New section to displaying FruityVice API response.
st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input('What fruit would you like information about?', 'Kiwi')
st.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Creates a variable to hold fruityvice_response in a dataframe.
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# Display the table for fruityvice_response on the page.
st.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
my_data_rows = my_data_rows.set_index('Fruit')
st.header("The fruit load list contains:")
st.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list
add_my_fruit = st.multiselect("What fruit would you like to add?", list(my_data_rows.index), "Jackfruit")
st.text("Thanks for adding " + add_my_fuit)
