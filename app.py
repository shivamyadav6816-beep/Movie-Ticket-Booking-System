import streamlit as st

st.set_page_config(
    page_title="Movie Ticket Booking",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>
.main{
    background-color:#0E1117;
}

.movie-card{
    background:#1c1f26;
    padding:20px;
    border-radius:15px;
    text-align:center;
    box-shadow:0 4px 8px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

st.title("🎬 Movie Ticket Booking System")

st.write("Book your favorite movies instantly!")

col1,col2,col3 = st.columns(3)

with col1:
    st.image(
        "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba",
        use_container_width=True
    )
    st.subheader("Avengers Endgame")
    st.write("⭐ 9.0/10")
    st.button("Book Now", key="1")

with col2:
    st.image(
        "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c",
        use_container_width=True
    )
    st.subheader("Interstellar")
    st.write("⭐ 8.9/10")
    st.button("Book Now", key="2")

with col3:
    st.image(
        "https://images.unsplash.com/photo-1440404653325-ab127d49abc1",
        use_container_width=True
    )
    st.subheader("Joker")
    st.write("⭐ 8.5/10")
    st.button("Book Now", key="3")

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "🏠 Home",
        "🎟 Book Ticket",
        "📋 My Bookings",
        "⚙ Admin Panel"
    ]
)

st.subheader("Book Your Ticket")

name = st.text_input("Customer Name")

movie = st.selectbox(
    "Select Movie",
    ["Avengers", "Interstellar", "Joker"]
)

tickets = st.number_input(
    "Number of Tickets",
    min_value=1,
    max_value=10
)

if st.button("Confirm Booking"):
    st.success(
        f"{name}, your {tickets} ticket(s) for {movie} are booked successfully!"
    )
    
col1,col2,col3 = st.columns(3)

col1.metric("Movies", "15")
col2.metric("Bookings", "250")
col3.metric("Revenue", "₹50,000")