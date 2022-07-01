from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

with st.echo(code_location='below'):
    tp = st.slider("Number of points in spiral", 1, 5000, 2000)
    nt = st.slider("Number of turns in spiral", 1, 100, 9)

    #Point = namedtuple('Point', 'x y')
    data = []

    #points_per_turn = total_points / num_turns

    for curr_point_num in range(tp):
        #curr_turn, i = divmod(curr_point_num, points_per_turn)
        #angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        #radius = curr_point_num / total_points
        x = curr_point_num
        y = curr_point_num/2
        data.append(x)
        print(data)
        print(x, y, x+y)
        st.text(data)
        st.text(x, y, x+y)


