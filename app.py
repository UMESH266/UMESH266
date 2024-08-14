import streamlit as st
from streamlit_option_menu import option_menu

# Set up the main page layout and configuration
st.set_page_config(page_title="Umesh Hanumanagouda - Data Scientist", layout="centered", page_icon="👨🏻‍💼")
st.title("Welcome to My Data Science Portfolio")

# Option menu
choice = option_menu(
        menu_title='Navigation',  # If required
        options=["Home", "About Me", "Portfolio", "Blog", "Contact"],
        icons=['house-check', 'search-heart', 'person-workspace', 'pencil-square', 'telephone-outbound'],
        default_index=0,
        styles={
            "container": {"padding": "0!important"},
            "icon": {"color": "#E8751A", "font-size": "18px"},
            "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#90D26D"},
            "nav-link-selected": {"background-color": "green"},
            },
        orientation="horizontal"
        )

# # Sidebar Navigation
# st.sidebar.title("Navigation")
# options = ["Home", "About Me", "Portfolio", "Blog", "Contact"]
# choice = st.sidebar.radio("Go to", options)

# 1. Homepage
if choice == "Home":
    st.write("""
    Hi, I'm Umesh Hanumanagouda, an aspiring data scientist with a passion for discovering insights from data.
    """)
    st.image("./profile_pic.jpg", width=250)  # Add your image here
    st.write("Use the sidebar to navigate through my site and learn more about me and my work.")

# 2. About Me Section
elif choice == "About Me":
    st.title("About Me")
    st.write("""
    *Biography:*
    - Background: Brief background about yourself.
    - Education: Mention your educational qualifications.
    - Skills: Python, SQL, Machine Learning, Data Visualization, etc.
    """)
    st.subheader("Skills")
    st.write("- Programming: Python, R")
    st.write("- Libraries/Frameworks: TensorFlow, Scikit-learn, Pandas")
    st.write("- Tools: Jupyter, Git, Docker")
    # Optionally, add a download button for your resume
    st.download_button("Download Resume", data=open("./UMESH_HANUMANAGOUDA.pdf", "rb"), file_name="UMESH_HANUMANAGOUDA.pdf")

# 3. Portfolio Section
elif choice == "Portfolio":
    st.title("Portfolio")
    st.write("Here are some of the projects I've worked on:")
    
    # Example of a project card
    st.subheader("Project 1: Stock price prediction")
    st.write("Brief description of the project.")
    # st.image("path/to/project_image.jpg", width=400)  # Optional: Add an image related to the project
    st.write("GitHub: [Link to the project repository](https://github.com/yourusername/project)")
    st.write("Demo: [Link to live demo or dashboard](https://yourdemo.com)")

    # Repeat for other projects

# 4. Blog Section
elif choice == "Blog":
    st.title("Blog")
    st.write("Welcome to my blog! Here, I share my thoughts, tutorials, and experiences in data science.")
    
    # Example of a blog post
    st.subheader("Blog Post 1: [Post Title]")
    st.write("Excerpt or introduction to the blog post.")
    st.write("Read more: [Link to full post](/post_url)")

    # Repeat for other blog posts

# 5. Contact Section
elif choice == "Contact":
    st.title("Contact Me")
    st.write("Feel free to reach out to me!")
    st.write("LinkedIn: [Your LinkedIn](https://www.linkedin.com/in/yourprofile)")
    st.write("GitHub: [Your GitHub](https://github.com/yourusername)")
    
    # Contact form
    with st.form(key="contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Send")

        if submit_button:
            st.write("Thank you! I'll get back to you soon.")

# Optional: Add Testimonials or Certifications Section
elif choice == "Testimonials":
    st.title("Testimonials")
    st.write("Here are some testimonials from people I've worked with.")
    # Add testimonials as text or cards

elif choice == "Certifications":
    st.title("Certifications")
    st.write("These are the certifications I've earned.")
    # List your certifications with logos or images
