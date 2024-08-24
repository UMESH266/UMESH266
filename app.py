from matplotlib import container
import streamlit as st
from streamlit_option_menu import option_menu
import base64
import pandas as pd
from streamlit_pdf_viewer import pdf_viewer

# Set up the main page layout and configuration
st.set_page_config(page_title="Umesh Hanumanagouda", layout="wide", page_icon="👨🏻‍💼")

# # background image set-up
# @st.cache_data
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# def set_png_as_page_bg(png_file):
#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
    
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return

# set_png_as_page_bg('profile_pic.jpg')

# Option menu
col1, col2= st.columns([1, 2])
with col1: 
    st.markdown("### UMESH")

with col2:
    choice = option_menu(
            menu_title=None,  # If required
            options=["Home", "About", "Experience", "Resume", "Contact"],
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
    st.markdown("<h2 style='text-align: center;'>Hi, I'm Umesh Hanumanagouda</h2>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>Help discovering insights from data to make better and informed business decisions.</h6>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
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

        st.markdown("#### :robot_face: GenAI")
        st.write("""I have certification in Genrative AI from Udemy and Looking for opportunities to apply the learnings to solve 
                 and add value.""")
    
    # Profile pic    
    with col2:
        st.image("./profile_pic.jpg", use_column_width=True, )  # Add your image here
    st.write("----")

# 2. About Me Section
elif choice == "About":
    st.markdown("### Inspired by the Data and Coding")
    st.write("""
                Umesh is motivated and attracted by the potential of quality data that can be used to make better and beneficial decisions. 
                He experiments and works to make it easier for people to understand the code and use data efficiently. Umesh primarily uses 
                Python to explore the Data and coding.
             
                Umesh has worked at Coal India Limited, Indian central public sector undertaking as Management Trainee, Assistant
                Manager and Deputy Manager over the span of seven and half years where he explored various facets of data helping the
                management to make better and efficient decisions. 
             
            """)
    
    with st.expander("Certifications"):
        st.write("Data Science")
        st.write("GenAI")
        st.write("Python")
        st.write("SQL")

    with st.expander("Education"):
        st.markdown("### Education")
        st.write("Umesh graduated in Mechanical Engineering from the National Institute of Technology Karnataka (NITK), Surathkal - India.")
        st.write("He has done schooling from Jawahar Navodaya Vidyalaya Koppal - Karnataka(India)")
    
    with st.expander("Skills"):
        st.markdown("### Skills")
        st.write("- Languages   : 	English (professional), Kannada (native), Hindi (limited)")
        st.write("- Programming :   Python (professional), SQL (professional)")
        st.write("- Libraries/Frameworks: TensorFlow, Scikit-learn, Pandas, Matplotlib, Seaborn, Streamlit, Flask")
        st.write("- Tools: VS Code, PyCharm, Jupyter, Google colab, MySQL, Git & Github, Docker, MLflow")
        st.write("- Visualization Tools: Tableau (professional), Power BI (professional)")
        st.write("""- Machine Learning 		:	Linear regression, Logistic regression, Clustering, Principal Component Analysis,
                    Algorithms			Association rules, Recommendation systems, Text mining, Naïve Bayes, Decision tree,
                    k-Nearest Neighbour, Random Forest, Support Vector Machines, Artificial Neural 
                    Networks, Convolutional Neural Networks, and Forecasting""")
        
# 3. Portfolio Section
elif choice == "Experience":
    with st.expander("Freelance projects"):
        
        # Maaya app project 
        col1, col2 = st.columns([2, 1])
        with col1:
            # Example of a project card
            st.write("#### Project 1: Streamlit App Development for Fuel Bunk Operations")
            st.write("""
                     Client: Axis Concept Construction Private Ltd., Bengaluru

                    Designed and developed an end-to-end Streamlit application using Python.
                    Scope includes real-time data capture and analysis for operations across 4 locations.
                    Automated data fetching and integration for comprehensive data analytics.
                    Created interactive dashboards for sales, expenses, and statistical analysis.
                    Implemented cash flow and indent information tracking modules.
                     
                    Final presentation of data using power BI business tool on daily basis.
                    """)
            st.write("Demo: [Link to app](https://maaya-autobahn.streamlit.app/)")
        with col2:
            st.image("Maaya_app.png", use_column_width=True)

        # Maaya app project 
        col1, col2 = st.columns([2, 1])
        with col1:
            # Example of a project card
            st.write("#### Project 2: Signature Hotel Feedback Analysis")
            st.write("""
                     Client: The Signature Hotels, Vishakapatnam.
                     
                     The Sentiment analysis of feedbacks of the Signatures Hotels, Vishakapatnam
                     to identify actionable insights. The data was cleaned and pre-processed to get
                     a workable format suitable for the application of Natural Language processing techniques.
                     The Exploratory data analysis using pandas, numpy, matplotlib, seaborn, and Sentiment analysis
                     of feedback text using Natural Language Processing libraries such as nltk, BERT.
                     
                     Analysis Dashboard prepared using Tableau and project deployed online using streamlit cloud platform.
                    """)
            st.write("Demo: [Link to app](https://feedback-sentiment-analysis.streamlit.app/)")
        with col2:
            st.image("Hotel_app.png", use_column_width=True)

    with st.expander("Internship"):
                
        # Example of a project card
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write("#### Stock price prediction")
            st.write("""
                        Employer: Aivariant, Bengaluru
                     
                        Stock price prediction, a team project to model price prediction using Data Science techniques.
                        Built machine-learning models applicable to Time series data such as ARIMA, Prophet, and LSTM using 
                        machine-learning techniques such as data collection, data cleaning/wrangling, exploratory data analysis, 
                        and data visualization.
                        
                        Deployed the best-performing ARIMA model online using Streamlit and GitHub. It has given lowest RMSE value
                        of 10.7 by the model.
                    """)
            st.write("GitHub: [Link to the project repository](https://github.com/UMESH266/P335-Stock-Price-prediction)")
            st.write("Demo: [Link to app](https://p335-stock-price-prediction.streamlit.app/)")
        with col2:
            st.image("Stock_price.png", use_column_width=True)

    with st.expander("Educational projects"):
        st.write("You can find all the project repositories I've worked on Github through below link.")
        st.write("GitHub: [Link to the project repositories](https://github.com/UMESH266?tab=repositories)")

    with st.expander("Days at Coal India Limited"):
        st.write("""
                    1. Deputy Manager                                                                                         
                    Managed the role of Technical Secretary to the Head of the department successfully and was 
                    In-charge of purchase repair tender cell with an outstanding performance rating for consecutive
                    financial years.
                    Published over 150 and finalized over 100 contracts per annum total valued at approximately 
                    Rs 350 lakhs.
                    Team achieved an annual coal production target of 10.5 MT.   

                    2. Assistant Manager                                                                                       
                    Successfully managed the role of In-charge, Purchase repair tender cell with outstanding 
                    performance ratings. 
                    Published over 150 and finalized over 100 contracts on average per annum and achieved zero 
                    pending files for tender finalization.
                    Assisted in the successful implementation of office software such as e-office and SAP in the
                    Excavation department. 
                    Team achieved 100% of the Annual Coal production target each financial year.  
        """)

# 4. Resume
elif choice == "Resume": 
    col1, col2, col3 = st.columns(3)
    col3.download_button(label="Download resume", file_name="UMESH_RESUME.pdf", data="pdf")
    pdf_viewer("UMESH_RESUME.pdf")
    
# 5. Contact Section
elif choice == "Contact":
    st.write("### Get in Touch")
    st.write("Feel free to reach out to me! through")
    col1, col2, col3 = st.columns(3)
    col1.write(":mailbox_with_mail: Mail: umeshgouda143@gmail.com")
    col2.write(":link: LinkedIn: [My LinkedIn](https://www.linkedin.com/in/umesh266/)")
    col3.write(":cat: GitHub: [My GitHub](https://github.com/UMESH266)")
    st.write("---")

    # Contact form
    st.write("### :postbox: Message box")
    st.write("Write to me for any collaborations and suggestions to improve")
    
    if "Message_df" not in st.session_state:
       st.session_state.Message_df = pd.DataFrame()
        
    with st.form(key="contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        text = st.text_area("Message")
        submit_button = st.form_submit_button("Send")

    message = {}
    if submit_button:
        st.write("Thank you! I'll get back to you soon.")
        message = [{"Name": name,
                    "Mail ID": email,
                    "Message": text}]
        st.write(message)
        
        msg_df = pd.DataFrame(message)
        st.session_state.Message_df = st.session_state.append(message)
        st.write(st.session_state.Message_df)
                
# Optional: Add Testimonials or Certifications Section
elif choice == "Testimonials":
    st.title("Testimonials")
    st.write("Here are some testimonials from people I've worked with.")
    # Add testimonials as text or cards

elif choice == "Certifications":
    st.title("Certifications")
    st.write("These are the certifications I've earned.")
    # List your certifications with logos or images
