from matplotlib import container
import streamlit as st
from streamlit_option_menu import option_menu
import base64

# Set up the main page layout and configuration
st.set_page_config(page_title="Umesh Hanumanagouda", layout="wide", page_icon="👨🏻‍💼")

# Option menu
col1, col2= st.columns([1, 2])
with col1: 
    st.markdown("### UMESH HANUMANAGOUDA")

with col2:
    choice = option_menu(
            menu_title=None,  # If required
            options=["Home", "About", "Projects", "Resume", "Contact"],
            icons=['house-check', 'search-heart', 'person-workspace', 'pencil-square', 'telephone-outbound'],
            default_index=0,
            styles={
                "container": {"padding": "0!important"},
                "icon": {"color": "#E8751A", "font-size": "16px"},
                "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#90D26D"},
                "nav-link-selected": {"background-color": "green"},
                },
            orientation="horizontal"
            )
st.write("-----")

# 1. Homepage
if choice == "Home":
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("## Hi, I'm Umesh Hanumanagouda")
        
        st.write("Help discovering insights from data to make better and informed business decisions.")
        st.write("---")
        
        st.markdown("#### :1234: Collect")
        st.write("""Coming from a background in Engineering, Management and freelance, I have theoretical and practical 
                 knowledge in data collection and management experience with various pipelines lik google forms, 
                 microsoft forms and api tools using python.""")

        st.markdown("#### :broom: Process")
        st.write("""
                 I'm experienced in Data processing using python in which I have converted raw data into useful information. 
                 The process involved cleaning, manipulating, analyzing, and interpreting data to extract insights that 
                 can help organizations make better decisions, improve efficiency, and enhance customer experience. 
            """)

        st.markdown("#### :chart_with_upwards_trend: ML Modeling")
        st.write(""" Trained to experment with different Machine Learning models to find best one based on 
                 the performance metrics and hyperparameter tuning.""")

        st.markdown("#### :factory: Deployment")
        st.write("""Trained and experienced in deploying the best performing model in production by creating web apps on 
                 cloud platforms like streamlit, AWS etc.""")

    # Profile pic    
    with col2:
        st.image("./profile_pic.jpg", use_column_width=True, )  # Add your image here
        st.write("---")
        st.markdown("#### :robot_face: GenAI")
        st.write("""I have certification in Genrative AI from Udemy and Looking for opportunities to apply the learnings to solve 
                 and add value.""")
    
# 2. About Me Section
elif choice == "About":
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
elif choice == "Resume":
    st.title("Resume") 

    st.download_button(label="Download resume", file_name="UMESH_HANUMANAGOUDA.pdf", data="pdf")

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
