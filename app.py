import streamlit as st
from datetime import date

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Movie Ticket Booking",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

.stApp {
    background-image: url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.main-title {
    text-align:center;
    color:white;
    font-size:55px;
    font-weight:bold;
}

.sub-title {
    text-align:center;
    color:#dddddd;
    font-size:20px;
}

.card {
    background: rgba(0,0,0,0.75);
    padding:20px;
    border-radius:15px;
    color:white;
    text-align:center;
    margin-bottom:20px;
}

.metric-card {
    background: rgba(0,0,0,0.75);
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;
}

footer {
    text-align:center;
    color:white;
    margin-top:50px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
menu = st.sidebar.radio(
    "📌 Navigation",
    [
        "🏠 Home",
        "🎬 Movies",
        "🎟 Book Ticket",
        "📊 Dashboard",
        "ℹ About"
    ]
)

# ---------------- HOME ---------------- #
if menu == "🏠 Home":

    st.markdown(
        '<h1 class="main-title">🎬 Movie Ticket Booking System</h1>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sub-title">Book Your Favorite Movies Instantly</p>',
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="card">
            <h3>🎥 Avengers Endgame</h3>
            <p>⭐ 9.0/10</p>
            <p>Action | Adventure</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="card">
            <h3>🚀 Interstellar</h3>
            <p>⭐ 8.9/10</p>
            <p>Sci-Fi | Drama</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            """
            <div class="card">
            <h3>🃏 Joker</h3>
            <p>⭐ 8.5/10</p>
            <p>Crime | Thriller</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------- MOVIES ---------------- #
elif menu == "🎬 Movies":

    st.title("🎬 Now Showing")

    movies = [
        ["Avengers Endgame", "Action", "9.0"],
        ["Interstellar", "Sci-Fi", "8.9"],
        ["Joker", "Thriller", "8.5"],
        ["Batman", "Action", "8.3"],
        ["Inception", "Sci-Fi", "9.1"]
    ]

    for movie in movies:
        st.markdown(
            f"""
            <div class="card">
            <h3>{movie[0]}</h3>
            <p>Genre: {movie[1]}</p>
            <p>Rating: ⭐ {movie[2]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------- BOOKING ---------------- #
elif menu == "🎟 Book Ticket":

    st.title("🎟 Book Your Ticket")

    customer_name = st.text_input("Enter Your Name")

    movie = st.selectbox(
        "Select Movie",
        [
            "Avengers Endgame",
            "Interstellar",
            "Joker",
            "Batman",
            "Inception"
        ]
    )

    booking_date = st.date_input(
        "Select Date",
        min_value=date.today()
    )

    show_time = st.selectbox(
        "Select Show Time",
        [
            "10:00 AM",
            "1:00 PM",
            "4:00 PM",
            "7:00 PM",
            "10:00 PM"
        ]
    )

    seats = st.slider(
        "Select Number of Seats",
        1,
        10,
        1
    )

    ticket_price = 250

    total = seats * ticket_price

    st.info(f"Total Amount: ₹{total}")

    if st.button("🎉 Confirm Booking"):

        st.success("Booking Successful!")

        st.balloons()

        st.write("### Booking Details")
        st.write(f"👤 Customer: {customer_name}")
        st.write(f"🎬 Movie: {movie}")
        st.write(f"📅 Date: {booking_date}")
        st.write(f"⏰ Time: {show_time}")
        st.write(f"🎟 Seats: {seats}")
        st.write(f"💰 Amount Paid: ₹{total}")

# ---------------- DASHBOARD ---------------- #
elif menu == "📊 Dashboard":

    st.title("📊 Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="metric-card">
        <h2>12</h2>
        <p>Total Movies</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="metric-card">
        <h2>250</h2>
        <p>Total Bookings</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="metric-card">
        <h2>₹50,000</h2>
        <p>Total Revenue</p>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="metric-card">
        <h2>320</h2>
        <p>Available Seats</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- ABOUT ---------------- #
elif menu == "ℹ About":

    st.title("ℹ About Project")

    st.markdown("""
    ### Professional Movie Ticket Booking Website

    Features:
    - Modern UI
    - Dashboard
    - Movie Listings
    - Ticket Booking
    - Price Calculation
    - Responsive Layout

    Developed using:
    - Python
    - Streamlit
    """)

# ---------------- FOOTER ---------------- #
st.markdown("""
<hr>
<footer>
Made with ❤️ using Python & Streamlit
</footer>
""", unsafe_allow_html=True)