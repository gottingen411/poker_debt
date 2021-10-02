import streamlit as st 
import pandas as pd 
from helper_functions import poker_calc
st.title("Poker Debt Calculator")
players = []
results = []
c1, c2, c3 = st.columns(3)
with c1: 
    with st.form(key="form1"):
        np = st.number_input("Enter number of players: ", min_value=1, max_value=10, step=1, key="np")
        submit0 = st.form_submit_button("Enter")

with c2:
    with st.form(key="poker_input_form"):
        st.header("Enter results here (- for loss): ")
        for i in range(np): 
            players.append(st.text_input("Name: ", "ANGELNA", key=f"name_{i}"))
            results.append(st.number_input("Profit/Loss: ", key=f"number_{i}"))
        submit = st.form_submit_button(label="Calculate debt")
if submit:
    with c3:
        input_dict_w = dict((x, y) for x, y in zip(players, results) if y > 0)
        input_dict_l = dict((x, -y) for x, y in zip(players, results) if y < 0)
        input_dict_pd = {"Player": players, "Result": results}
        st.write(pd.DataFrame(input_dict_pd))
        st.write(poker_calc(input_dict_l, input_dict_w))
