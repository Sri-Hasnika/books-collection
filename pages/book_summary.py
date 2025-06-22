import streamlit as st
import pandas as pd

st.title("Book Summary")

if "books" not in st.session_state or not st.session_state.books:
    st.write("No books added yet. Please add books in the Book Entry page.")
else:
    df = pd.DataFrame(st.session_state.books)

    st.subheader("Books by Genre")
    genre_summary = df.groupby("genre").size().reset_index(name="count")
    st.bar_chart(genre_summary.set_index("genre"))

    st.subheader("Average Rating by Genre")
    rating_summary = df.groupby("genre")["rating"].mean().reset_index()
    st.bar_chart(rating_summary.set_index("genre"))

    st.subheader("Total Books")
    total = len(df)
    st.write(f"**{total}** books added")
