import streamlit as st

# st.title("Hello world")

home = st.Page(
    page = "views/home.py",
    title='Home',
    default= True
)

about = st.Page(
    page = "views/about.py",
    title='Tentang Kami',
)

sampah = st.Page(
    page = "views/sampah.py",
    title='Sampah',
)

sampah_organik = st.Page(
    page = "views/organik.py",
    title='Sampah Organik',
)

sampah_anorganik = st.Page(
    page = "views/anorganik.py",
    title='Sampah Anorganik',
)

AI = st.Page(
    page = "views/AI.py",
    title = "AI",
)

pg = st.navigation(
    pages= [home, about, sampah, sampah_organik, sampah_anorganik, AI]
)

# {
#     "info" : [home],
#     "projects" :[about],
#     }



pg.run()


hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden; }
    </style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)

