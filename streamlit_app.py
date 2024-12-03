import streamlit as st

# Set page configuration
st.set_page_config(page_title="Doradz Photography", layout="wide")

# Navigation tabs
tabs = st.tabs(["About Me", "Weddings", "Events", "Portraits", "Studio", "Videos", "Contact Form"])


# About Me tab
with tabs[0]:
    st.header("About Me")
    st.write("""
    Welcome to **Doradz Photography**! I specialize in capturing life's most precious moments.
    With a passion for creativity and a dedication to excellence, I aim to tell stories through my lens.
    """)

    # Add your photo
    st.image("media/d1.jpg", caption="John Dorado - Photographer", use_container_width=True)

    st.subheader("Who I Am")
    st.write("""
    I’m John Dorado, a professional photographer with [X years] of experience in weddings, events, and portraits.
    My journey started when [short personal anecdote], and I haven’t looked back since.
    """)

    st.subheader("My Philosophy")
    st.write("""
    Every moment has a story, and my goal is to capture it in the most authentic and beautiful way possible.
    """)

   # Add more details, images, or personal info here

###############################################

# Weddings tab
# Weddings tab
with tabs[1]:
    st.header("Weddings")
    st.write("Capture the magic of your wedding day with timeless and stunning photos.")

    # List of sample wedding photos (update with your image paths or URLs)
    wedding_photos = [
        "media/weddings/wedding1.jpg",
        "media/weddings/wedding2.jpg",
        "media/weddings/wedding3.jpg",
        "media/weddings/wedding4.jpg",
        "media/weddings/wedding5.jpg",
        "media/weddings/wedding6.jpg",
        "media/weddings/wedding7.jpg",
        "media/weddings/wedding8.jpg",
        "media/weddings/wedding9.jpg",
    ]

    # Display photos in a 3-row grid
    rows = len(wedding_photos) // 3  # Calculate number of rows based on images
    for i in range(rows):
        cols = st.columns(3)  # Create 3 columns
        for j, col in enumerate(cols):
            # Calculate index for each photo
            photo_index = i * 3 + j
            if photo_index < len(wedding_photos):
                col.image(wedding_photos[photo_index], use_container_width=True)


###############################################

# Events tab
with tabs[2]:
    st.header("Events")
    st.write("From birthdays to corporate events, I ensure every moment is perfectly preserved.")

    # List of sample event photos in the media/events folder
    event_photos = [
        "media/events/event1.jpg",
        "media/events/event2.jpg",
        "media/events/event3.jpg",
        "media/events/event4.jpg",
        "media/events/event5.jpg",
        "media/events/event6.jpg",
        "media/events/event7.jpg",
        "media/events/event8.jpg",
        "media/events/event9.jpg",
    ]

    # Display photos in a 3-row grid
    rows = len(event_photos) // 3  # Calculate number of rows based on images
    for i in range(rows):
        cols = st.columns(3)  # Create 3 columns
        for j, col in enumerate(cols):
            # Calculate index for each photo
            photo_index = i * 3 + j
            if photo_index < len(event_photos):
                col.image(event_photos[photo_index], use_container_width=True)

###############################################

# Portraits tab
# Portraits tab
with tabs[3]:
    st.header("Portraits")
    st.write("Let your personality shine with professionally crafted portraits.")

    # List of sample portrait photos in the media/portraits folder
    portrait_photos = [
        "media/portraits/portrait1.jpg",
        "media/portraits/portrait2.jpg",
        "media/portraits/portrait3.jpg",
        "media/portraits/portrait4.jpg",
        "media/portraits/portrait5.jpg",
        "media/portraits/portrait6.jpg",
        "media/portraits/portrait7.jpg",
        "media/portraits/portrait8.jpg",
        "media/portraits/portrait9.jpg",
    ]

    # Display photos in a 3-row grid
    rows = len(portrait_photos) // 3  # Calculate number of rows based on images
    for i in range(rows):
        cols = st.columns(3)  # Create 3 columns
        for j, col in enumerate(cols):
            # Calculate index for each photo
            photo_index = i * 3 + j
            if photo_index < len(portrait_photos):
                col.image(portrait_photos[photo_index], use_container_width=True)

###############################################


# Studio tab
with tabs[4]:
    st.header("Studio")
    st.write("""
    Welcome to our professional photography studio, where creativity meets cutting-edge technology.
    Whether you're looking for portrait sessions, product shoots, or creative projects, we provide the perfect space and expertise.
    """)

    # List of sample studio photos in the media/studio folder
    studio_photos = [
        "media/studio/studio1.jpg",
        "media/studio/studio2.jpg",
        "media/studio/studio3.jpg",
        "media/studio/studio4.jpg",
        "media/studio/studio5.jpg",
        "media/studio/studio6.jpg",
        "media/studio/studio7.jpg",
        "media/studio/studio8.jpg",
        "media/studio/studio9.jpg",
    ]

    # Display photos in a 3-row grid
    rows = len(studio_photos) // 3  # Calculate number of rows based on images
    for i in range(rows):
        cols = st.columns(3)  # Create 3 columns
        for j, col in enumerate(cols):
            # Calculate index for each photo
            photo_index = i * 3 + j
            if photo_index < len(studio_photos):
                col.image(studio_photos[photo_index], use_container_width=True)
    
    
###############################################

# Videos tab
with tabs[5]:
    st.header("Videos")
    st.write("Explore some of my favorite moments captured in motion.")

    # List of video files in the media/videos folder
    video_files = [
        "media/videos/video1.mp4",
        "media/videos/video2.mp4",
        "media/videos/video3.mp4",
        #"media/videos/video4.mp4",
        #"media/videos/video5.mp4",
        #"media/videos/video6.mp4",
    ]

    # Display videos in a 3-row grid
    rows = len(video_files) // 3  # Calculate number of rows based on videos
    for i in range(rows):
        cols = st.columns(3)  # Create 3 columns for each row
        for j, col in enumerate(cols):
            video_index = i * 3 + j
            if video_index < len(video_files):
                video_path = video_files[video_index]
                # Embed video
                col.video(video_path)
                
###############################################

# Contact Form tab
with tabs[6]:
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