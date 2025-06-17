from tkinter import S
from pyparsing import col
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from streamlit_pdf_viewer import pdf_viewer
import base64
from streamlit_gsheets import GSheetsConnection


# Set up the main page layout and configuration
st.set_page_config(page_title="Umesh Hanumanagouda", layout="wide", page_icon="👨🏻‍💼")

# Main menu and footer hiding
hide_setting = """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
</style>
"""
st.markdown(hide_setting, unsafe_allow_html=True)
# Background image set up
def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "jpg"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_hack("Background.jpg")

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
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown("<h2 style='text-align: center;'>Hi,</h2>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>I'm Umesh Hanumanagouda</h2>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<h6 style='text-align: center;'>Help discovering insights from data to make better and informed business decisions.</h6>", unsafe_allow_html=True)
    # Profile pic    
    with col2:
        st.image("./Profile_pic.png")  # Add your image here
    
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### :1234: Collect")
        st.write("""Coming from a background in Engineering, Management and freelance, I have theoretical and practical 
                 knowledge in data collection using various methods and api tools using python.""")
    with col2:
        st.markdown("#### :broom: Process")
        st.write("""
                 I'm experienced in Data processing using python to converted raw data into useful information, which
                 involves cleaning, manipulating, analyzing, and interpreting data to extract insights. 
            """)
    with col3:
        st.markdown("#### :chart_with_upwards_trend: ML Modeling")
        st.write(""" Trained to experment with different Machine Learning models to find best one based on 
                 the performance metrics and hyperparameter tuning.""")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### :factory: Deployment")
        st.write("""Trained and experienced in deploying the best performing model in production by creating web apps on 
                 cloud platforms like streamlit, AWS etc.""")
    with col2:
        st.markdown("#### :robot_face: GenAI")
        st.write("""I have certification in Genrative AI from Udemy and Looking for opportunities to apply the learnings to solve 
                 and add value.""")
    
    st.write("----")

# 2. About Me Section
elif choice == "About":
    section = option_menu(
        menu_title='',  # If required
        options=["Know me", "Certifications", "Education", "Skills"],
        icons=['person-circle', 'file-text-fill', 'book-half', 'tools'],
        default_index=0,
        styles={
            "container": {"padding": "0!important"},
            "icon": {"color": "#E8751A", "font-size": "18px"},
            "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#90D26D"},
            "nav-link-selected": {"background-color": "green"},
        },
        orientation='horizontal'
    )
        
    if section == "Know me":
        st.markdown("#### Intrigued by the information hidden in data and ways to extract it.")
        st.write("""
                    I am a passionate and results-driven Junior Data Scientist with a strong foundation in machine learning, data analysis, and predictive 
                    modeling. I collaborate with cross-functional teams to deliver data-driven solutions that drive business growth and efficiency. My 
                    expertise lies in fraud detection, customer analytics, credit scoring, and time-series forecasting, where I leverage machine learning 
                    and advanced algorithms like XGBoost, LightGBM, ARIMA, and LSTM to extract actionable insights from complex datasets.

                    With a background in Mechanical Engineering from the National Institute of Technology Karnataka, I bring a unique blend of technical 
                    and analytical skills to the table. My transition from Executive Manager at Coal India Limited to Data Science showcases my adaptability
                    and commitment to continuous learning. I am certified in Data Science, Generative AI, and AWS Cloud, and I am always eager to explore 
                    new technologies and methodologies to solve real-world problems.

                    I thrive in collaborative environments and have hands-on experience with tools like Python, SQL, Tableau, Power BI, and PySpark. My 
                    freelance projects, including developing data entry web apps and sentiment analysis dashboards, reflect my ability to deliver end-to-end 
                    solutions tailored to business needs.

                    When I'm not crunching numbers, you can find me honing my skills on Leetcode, and HackerRank, where I hold a 5-star Gold badge in both 
                    Python and SQL. I am excited about opportunities to contribute to innovative projects and make a meaningful impact through data science. 
                
                """)
    
    elif section == "Certifications":
        st.write("### Certificates and acclodes")
        col1, col2= st.columns(2)
        with col1:
            panel = st.container(height=None, border=True) # 870
            with panel:
                st.write("1. Data Science")
                st.image("Data Science certificate.jpg", caption="Data Science")
        with col2:
            top = col2.container(height=None, border=True)
            bottom = col2.container(height=None, border=True) # 425
            with top:
                st.write("2. GenAI")
                st.image("GenAI.jpg", caption="GenAI")

            with bottom:
                st.write("3. NASSCOM")
                st.image("NASSCOM DATA SCIENCE.jpg", caption="NASSCOM")

        col3, col4 = st.columns(2)
        with col3:
            col3_panel = st.container(border=True)
            with col3_panel:
                st.write("3. Python")
                st.image("Python.png", caption="Python")
        with col4:
            col4_panel = st.container(border=True)
            with col4_panel:
                st.write("4. SQL")
                st.image("SQL.png", caption="SQL")
        col5, col6 = st.columns(2)
        with col5:
            col5_panel = st.container(border=True)
            with col5_panel:
                st.write("5. AWS Basics")
                st.image("AWS_cloud_basic.jpg", caption="AWS Basics")

    elif section == "Education":
        st.markdown("### Education")
      
        education_dict = {
            "Education":['B. Tech (ME)', '12th - Science'],
            "Institute":["NITK Surathkal, India", "JNVK Koppal, India"],
            "Period":["2011-2015", "2009-2011"]
        }

        education_df = pd.DataFrame(education_dict, index=[1, 2])
        st.table(education_df)
    
    elif section == "Skills":
        st.markdown("### Skills")

        skills_dict = {
                "Programming" :     "Python (Pandas, NumPy, SciPy, Scikit-Learn, TensorFlow,  Keras,), SQL",
                "AI / ML"		:	"Machine Learning, Neural Networks, GenAI basics",
                "Visualization Tools": "Tableau, Power BI, Matplotlib, Seaborn, Grafana",
                "MLOPs tools"	:	"Git, Github, Github Actions, DVC, Dagshub, MLflow, Airflow, Docker, Dockerhub",
                "Tools": "VSCode, PyCharm, Google Colab, Jupyter Notebook, Databricks, MySQL",
                "Cloud tool"	:	"AWS basics", 
                "COMMUNICATION"	:	"English (Proficient), Kannada (Native), Hindi (Limited)"
        }

        skills_df = pd.DataFrame(skills_dict, index=['Details'])
        st.table(skills_df.T)

# 3. Portfolio Section
elif choice == "Experience":
    experience = option_menu(
        menu_title='',  # If required
        options=["Current", "Coal India", "Freelancing", "Internship", "Educational"],
        icons=['person-circle', 'file-text-fill', 'book-half', 'tools', 'book'],
        default_index=0,
        styles={
            "container": {"padding": "0!important"},
            "icon": {"color": "#E8751A", "font-size": "18px"},
            "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#90D26D"},
            "nav-link-selected": {"background-color": "green"},
        },
        orientation='horizontal'
    )
    if experience == "Current":
        st.markdown("#### Junior Data Scientist")
        st.write("""                 
            @ Nowon Technologies, Bengaluru, India, since 04.2023\n
        •	Worked with cross-functional teams to understand data needs and deliver solutions.\n
        •	Assisted the Data Science team in analyzing 20+ medium to large data sets of different companies using Python to extract actionable insights 
            which helped companies achieve 10 – 15% improvement in valuable customer holding, employee retention, future movements, and fraud reduction.\n
        •	**Fraud detection**: Contributed to the team in developing projects to detect fraudulent transactions, anomalies in insurance claims, or credit card
             usage using isolation forest and other supervised machine learning algorithms.\n
        •	**Customer Analytics**: part of the team that used to find key features/factors causing customer churning, employees quitting, fraudulent 
            transactions, and customer segmentation for targeted marketing using classification and clustering algorithms.\n 
        •	**Credit scoring & risk**: Helped in developing systems to find the creditworthiness of customers and businesses. Also, prediction of the likelihood
             of loan defaults using regression, classification, and various gradient boosting algorithms such as Xgboost, lightgbm, catboost etc.\n
        •	**Forecasting**: Worked on forecasting and predictive models such as ARIMA, SARIMA, Prophet, and LSTM on time-series data to predict future 
            movements and prices of the stocks/revenues of business.
        ***
        """)
    elif experience== "Freelancing":
        
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
        st.write("***")
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

    elif experience == "Internship":
                
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
        st.write("***")
    elif experience == "Educational":
        st.write("You can find all the project repositories I've worked on Github through below link.")
        st.write("GitHub: [Link to the project repositories](https://github.com/UMESH266?tab=repositories)")

    elif experience=="Coal India":
        st.write("""
                    ***1. Deputy Manager*** 
                                                                                                      
                    • Managed the role of Technical Secretary to the Head of the department successfully and was 
                    In-charge of purchase repair tender cell with an outstanding performance rating for consecutive
                    financial years.
                    Published over 150 and finalized over 100 contracts per annum total valued at approximately 
                    Rs 350 lakhs.
                    
                    • Team achieved an annual coal production target of 10.5 MT.   
                    
                    • As a Technical Manager performed Technical and techno-commercial analysis of Hemm's performance to 
                    manage Budget allocation, Spare parts, Manpower, and Repair works using Excel, E-office, and SAP.

                    *** 
                    ***2. Assistant Manager*** 
                                                                                              
                    • Successfully managed the role of In-charge, Purchase repair tender cell with outstanding 
                    performance ratings. 
                 
                    • Published over 150 and finalized over 100 contracts on average per annum and achieved zero 
                    pending files for tender finalization.
                 
                    • Assisted in the successful implementation of office software such as e-office and SAP in the
                    Excavation department. 
                 
                    • Team achieved 100% of the Annual Coal production target each financial year.  
                    
                    • Forecasting for HEMM spare parts indentation for procurement by analyzing HEMMs working hours 
                    and past consumption of spare parts using traditional statistical methods.

                    • Preventive and predictive maintenance of HEMMs by analyzing and interpreting the working hours, 
                    daily maintenance inspections, and log reports.   
                 ***
        """)

# 4. Resume
elif choice == "Resume": 
    col1, col2, col3 = st.columns(3)
    with open("UMESH_RESUME.pdf", "rb") as file:
        col3.download_button(
             label="Download Resume",
             data=file,
             file_name="UMESH_RESUME.pdf",
             mime="text/pdf"
        )
    
    annotations = [
    {
        # "page": 1,
        # "x": 220,
        # "y": 155,
        # "height": 22,
        # "width": 65,
        # # "color": "red"
    }
    ]
    pdf_viewer("UMESH_RESUME.pdf", annotations=annotations)
    
# 5. Contact Section
elif choice == "Contact":
    st.write("### :handshake: Get in Touch")
    st.write("Feel free to reach out to me! through")
    col1, col2, col3 = st.columns(3)
    col1.write(":mailbox_with_mail: Mail: umeshgouda143@gmail.com")
    col2.write(":link: LinkedIn: [My LinkedIn](https://www.linkedin.com/in/umesh266/)")
    col3.write(":cat: GitHub: [My GitHub](https://github.com/UMESH266)")
    st.write("---")

    # Contact form
    st.write("### :postbox: Message box")
    st.write("Write to me for any collaborations / suggestions to improve")
    
    # google sheets connection
    if 'conn' not in st.session_state:
        st.session_state.conn = st.connection("gsheets", type=GSheetsConnection)

    if "Message_df" not in st.session_state:
       st.session_state.Message_df = st.session_state.conn.read(worksheet="Feedback")

    if "msg_df" not in st.session_state:
       st.session_state.msg_df = pd.DataFrame()

    with st.form(key="contact_form", clear_on_submit=True):
        name = st.text_input("Name")
        email = st.text_input("Email")
        text = st.text_area("Message")
        col1, col2, col3, col4 = st.columns(4)
        submit_button = col4.form_submit_button("Send")

        if submit_button:
            if (name == "") or (email == "") or (text == ""):
                st.error("Please fill all the fields")
            else:
                st.success(f"Thank you, {name}! I'll get back to you soon if any.")
                
                message = [{"Name": name,
                            "Mail ID": email,
                            "Message": text}]
                
                st.session_state.msg_df = pd.DataFrame(message)
                st.session_state.Message_df = pd.concat([st.session_state.Message_df, st.session_state.msg_df], ignore_index = True)
                st.session_state.conn.update(worksheet="Feedback", data=st.session_state.Message_df)