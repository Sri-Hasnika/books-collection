import streamlit as st

st.set_page_config(page_title="Book Collection Dashboard", layout="wide")

book_entry_page = st.Page("sample/pages/book_entry.py", title="Book Entry")
book_summary_page = st.Page("sample/pages/book_summary.py", title="Book Summary")

pg = st.navigation([
    book_entry_page,
    book_summary_page
])

pg.run()
