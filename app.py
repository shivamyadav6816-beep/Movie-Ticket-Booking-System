import streamlit as st
import json
from pathlib import Path

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Movie Ticket Booking",
    page_icon="🎬",
    layout="wide"
)

# ---------------- DATABASE ---------------- #
DATABASE = "Movies.json"

if not Path(DATABASE).exists():
    with open(DATABASE, "w") as file:
        json.dump([], file)

with open(DATABASE, "r") as file:
    movies = json.load(file)


def save_data():
    with open(DATABASE, "w") as file:
        json.dump(movies, file, indent=4)


# ---------------- HEADER ---------------- #
st.markdown("""
    <h1 style='text-align:center;color:#ff4b4b'>
        🎬 Movie Ticket Booking System
    </h1>
""", unsafe_allow_html=True)

st.divider()

# ---------------- SIDEBAR ---------------- #
menu = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "➕ Add Movie", "🎟 Book Ticket"]
)

# ---------------- HOME PAGE ---------------- #
if menu == "🏠 Home":

    st.subheader("Available Movies")

    if movies:
        cols = st.columns(3)

        for index, movie in enumerate(movies):
            with cols[index % 3]:
                st.card = st.container()

                with st.card:
                    st.markdown(f"""
                    ### 🎥 {movie['movie_name']}
                    """)
                    st.success(
                        f"Available Seats: {movie['available_seats']}"
                    )
    else:
        st.warning("No movies available.")


# ---------------- ADD MOVIE ---------------- #
elif menu == "➕ Add Movie":

    st.subheader("Add New Movie")

    with st.form("movie_form"):
        movie_name = st.text_input("Movie Name")
        seats = st.number_input(
            "Available Seats",
            min_value=1,
            step=1
        )

        submit = st.form_submit_button("Add Movie")

        if submit:
            movies.append({
                "movie_name": movie_name,
                "available_seats": seats
            })

            save_data()
            st.success("Movie Added Successfully!")


# ---------------- BOOK TICKET ---------------- #
elif menu == "🎟 Book Ticket":

    st.subheader("Book Tickets")

    if movies:

        movie_names = [movie["movie_name"] for movie in movies]

        selected_movie = st.selectbox(
            "Select Movie",
            movie_names
        )

        tickets = st.number_input(
            "Number of Tickets",
            min_value=1,
            step=1
        )

        if st.button("Book Now"):

            for movie in movies:

                if movie["movie_name"] == selected_movie:

                    if movie["available_seats"] >= tickets:

                        movie["available_seats"] -= tickets
                        save_data()

                        st.success(
                            f"{tickets} Ticket(s) booked for {selected_movie}"
                        )

                    else:
                        st.error("Not enough seats available!")
    else:
        st.warning("No movies available.")