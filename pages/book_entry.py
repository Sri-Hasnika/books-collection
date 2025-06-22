import streamlit as st

st.title("Book Entry")

# Initialize session state for books
if "books" not in st.session_state:
    st.session_state.books = []

# Book entry form
with st.form("book_form", clear_on_submit=True):
    st.subheader("Add New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    genre = st.selectbox("Genre", ["Fiction", "Non-Fiction", "Science Fiction", "Fantasy", "Biography", "Other"])
    rating = st.slider("Rating", min_value=0, max_value=5, step=1)
    submitted = st.form_submit_button("Add Book")

    if submitted:
        book = {
            "title": title,
            "author": author,
            "genre": genre,
            "rating": rating
        }
        st.session_state.books.append(book)
        st.success("Book added!")

# Display books
if st.session_state.books:
    st.subheader("Books")
    st.dataframe(st.session_state.books)
else:
    st.write("No books added yet.")
