import streamlit as st

# Set page configuration
st.set_page_config(page_title="Doradz Photography", layout="wide")

# Navigation tabs
tabs = st.tabs(["About Me", "Weddings", "Events", "Portraits", "Studio", "Contact Form"])

# About Me tab
with tabs[0]:
    st.header("About Me")
    st.write("Welcome to Doradz Photography! I specialize in capturing life's most precious moments. "
             "With a passion for creativity and a dedication to excellence, I aim to tell stories through my lens.")
    # Add more details, images, or personal info here

# Weddings tab
with tabs[1]:
    st.header("Weddings")
    st.write("Capture the magic of your wedding day with timeless and stunning photos.")
    # Add sample photos, packages, and testimonials here

# Events tab
with tabs[2]:
    st.header("Events")
    st.write("From birthdays to corporate events, I ensure every moment is perfectly preserved.")
    # Showcase event highlights or client stories

# Portraits tab
with tabs[3]:
    st.header("Portraits")
    st.write("Let your personality shine with professionally crafted portraits.")
    # Add sample portrait photography

# Studio tab
with tabs[4]:
    st.header("Studio")
    st.write("Explore my studio services and see how we can bring your creative ideas to life.")
    # Include studio setup photos or services offered

# Contact Form tab
with tabs[5]:
    st.header("Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        phone = st.text_input("Your Phone Number")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success(f"Thank you, {name}! Your message has been sent successfully.")

#