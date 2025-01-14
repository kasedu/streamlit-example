from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import sympy as sp

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
a = 1
b = 2
c = 3

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

st.write('1 + 1 = ', 2)
st.write('a + b + c =', a + b + c) 

st.latex(r''' a + b + c = ''')

d = sp.Symbol('d')

st.write('a = {}'.format(a))

t = 5

st.latex(r'''\theta_b='''+ rf'''{t} ''')

st.write(d)

with st.echo(code_location='below'):
    tp = st.slider("Number of points in spiral", 1, 2, 3)
    nt = st.slider("Number of turns in spiral", 1, 10, 3)

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
