import streamlit as st
from streamlit_option_menu import option_menu
import requests 
from streamlit_lottie import st_lottie
from PIL import Image
import pandas as pd
import numpy as np
import time

# Setting Page Config, must remain at top
st.set_page_config(page_title="My Portfolio ", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Creating Functions for differet Sections
# Home Function --------------------------------------------------------------------------------------------------------------
def Home():
    st.markdown("""
    ## Hi, I'm :rainbow[Yash Sharma] 👋
    """)

    # Create two columns
    col1, col2 = st.columns([1, 2])  # Adjust column width as needed

    with col1:
        image_path = "C:/Users/Yash Sharma/Dropbox/PC/Desktop/Pictures/XeBit/IMG_7122.JPG"
        image = Image.open(image_path)

        rotated_image = image.rotate(90, expand=True)

        width = 350
        height = int((float(rotated_image.size[1]) / float(rotated_image.size[0])) * width)
        resized_image = rotated_image.resize((width, height))

        st.image(resized_image)

    with col2:
        st.markdown("""
        # A Data Analyst and Web Developer
        By day, I'm diving deep into :red[**Data Analytics and Insights**], and by night, I'm exploring the vast worlds of Data Science, including :blue[**Machine Learning**], :blue[**Deep Learning**], and :blue[**Many upcoming technologies helpful in data analysis**]. 
        
        My journey also includes working on cutting-edge *Large Language Models*, bringing innovative ideas to fruition. My technical skills include :orange[**Python**], :orange[**MySQL**], :orange[**Prompting**], :orange[**Exploratory Data Analysis**], :orange[**Streamlit**], :orange[**pandas**], :orange[**numpy**], :orange[**matplotlib**], :orange[**plotly**], and :orange[**seaborn**], to name a few. 
        
        My portfolio is a treasure trove of diverse projects, from building :grey[*Gradio interface to find the best jewellery comparator out of the stock available*] to :grey[*performing exploratory data analysis to find useful insights and implement ideas helpful in growth of company*]. 
        
        Whether it's performing complex tasks or designing captivating user interfaces, I'm your go-to person for all things development. When I'm not coding, you can find me exploring the latest tech trends or honing my problem-solving skills or roaming around and exploring the world. 
        """)

    st.write("""
             :green[I'm always eager to learn and grow, and I'm excited about where my passion for Data Analysis and Web Development will take me next. If you're looking to bring your ideas to life, let's collaborate and create something extraordinary together!]

        📂 :violet[Refer sidebar to navigate yourself to a collection of my **projects**, **achievements**, and **insights** into the world of data science and web development.]
        
        🌐 :violet[Explore and feel free to reach out if you have any questions or collaboration ideas!]

        📫 Connect with me on [LinkedIn](https://www.linkedin.com/in/yashsharma-dataanalyst/) || [GitHub](https://github.com/SharmaYash2423) || [Email](mailto:sharmayash394@gmail.com)
        """)
    
    st.write("### Here's my resume:")
    with open("C:/Users/Yash Sharma/Dropbox/PC/Desktop/Advance Python Programming/streamlit-portfolio-main/Yash Sharma Final Resume.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume",
            data=file,
            file_name="Yash Sharma Data Analyst Resume.pdf",
            mime="application/pdf"
        )
        
    with st.form('User Registration Form'):
        st.write('Please fill in the following details so that I can get your contact information to collaborate in future projects:')
        
        name = st.text_input('Full Name')
        email = st.text_input('Email')
        country = st.selectbox("Country", ["India", "USA", "UK", "Canada", "Australia", "Others"])
        linkedin = st.text_input('Provide your LinkedIn Profile Link')
        age = st.number_input('Age', min_value=0, max_value=100)
        gender = st.radio("Gender", ("Male", "Female", "Other"))
        slider_val = st.slider('How keen are you to collaborate on the scale of 1-10?', 1, 10)
        checkbox_val = st.checkbox('I agree to the Terms and Conditions')
    
        submitted = st.form_submit_button('Submit')
        if submitted:
            errors = []
            if not name:
                errors.append("Name cannot be empty.")
            if not email or "@" not in email or "." not in email:
                errors.append("Enter a valid email address.")
            if age < 18:
                errors.append("You must be at least 18 years old to register.")
            if not checkbox_val:
                errors.append("You must agree to the Terms and Conditions.")
    
            if errors:
                for error in errors:
                    st.error(error)
    
            else:
                st.success("Registration Successful!")
                st.write("### Submitted Details: ###")
                st.write(f"**Name:** {name}")
                st.write(f"**Email:** {email}")
                st.write(f"**Country:** {country}")
                st.write(f"**LinkedIn Profile:** {linkedin}")
                st.write(f"**Age:** {age}")
                st.write(f"**Gender:** {gender}")
                st.write(f"**Interest Level:** {slider_val}")
                st.write(f"**Agreed to Terms:** {'Yes' if checkbox_val else 'No'}")
    

# Projects Function --------------------------------------------------------------------------------------------------------------
def Projects():
    st.title('My Projects')
    # Project 1 Container
    with st.container():
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/eee3dbab-2db1-47ff-8517-bbe523b2e542/DJxtNRMpWw.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="project1")
            else:
                st.error("Failed to load Lottie animation.")
        with text_col:
            # Enter Desctipion
            st.write("### :red[Red] Katana - Game Vault Engine")
            st.write("""
                    - Developed a responsive gaming web application using HTML, Tailwind, CSS, MongoDB, News API and JavaScript.
                    - Utilised for displaying recent gaming news, secure user authentication, and buying/selling of games.
                    - Helps users to interact with the gaming community, share their experiences, and stay connected from all over the world.
                    """)
            if st.button("Know More ➡️"):
                with st.expander("### Technologies Used", expanded=False):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.write("- HTML")
                        st.write("- CSS")
                        st.write("- JavaScript")
                    with col2:
                        st.write("- MongoDB")
                        st.write("- NewsAPI")
                        st.write("- Python")
                        
                with st.expander("### Project Link", expanded = False):
                    st.write("[Red Katana's Repo](https://github.com/SharmaYash2423/Gaming-Vault-Project)")
                    
                with st.expander("Features", expanded = False):
                    st.write("""
                            - **Interactive UI**: User-friendly interface for easy navigation and understanding gaming community. 
                            - **Regular Updation**: Regular updates on gaming news and events happening all around the world. 
                            - **Fraud Detection**: Secure user authentication and buying/selling of games through an online dataset managed.
                            - **Added Features**: Added features like chatbot, user interaction platform like discord and many more.
                            """)
    
    # Project 2 Container
    with st.container():
        st.write("---")
        st.write("##")
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/01132fcd-221d-4491-8c99-6ce0f1127dd7/lJxZcH3eAt.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="project2")
            else:
                st.error("Failed to load Lottie animation.")
        with text_col:
            st.write("### :blue[Jewellery Comparator and Analysis]")
            st.write("""
                    - Developed a gradio interface to successfully compare the jewellery and provide the best output out of the stock available.
                    - Help Reduce the time of the user to find the best jewellery available throughout the dataset by integrating OpenAI API keys.
                    """)
            if st.button("Know More 🚀"):
                with st.expander("### Technologies Used", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("- Python")
                        st.write("- Gradio")
                        st.write("- MySQL")
                    with col2:
                        st.write("- Prompting")
                        st.write("- OpenAI API Keys")
                
                with st.expander("### Project Link", expanded = False):
                    st.write("[Jewellery Comparator's Repo](https://github.com/SharmaYash2423/Jewellery-Comparator-and-Analysis-)")
                    
                with st.expander("Features", expanded = False):
                    st.write("""
                            - **Enhanced UI**: Interactive UI for easy navigation and understanding output.
                            - **Stock Overview**: Results based on present stock available at particular locations. 
                            - **Logical Reasoning**: Provides the best jewellery comparatively with the proper reasoning. 
                            - **AI Comparision Tools**: Uses AI to compare the jewellery and its features to provide the best output jewellery in comparision with the jewellery image provided by the user. 
                            """)
    
    # Project 3 Container
    with st.container():
        st.write("---")
        st.write("##")
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/26387e36-3492-4465-9f16-fbf9db4a4807/YuzVL6WIpe.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="project3")
            else:
                st.error("Failed to load Lottie animation.")
        with text_col:
            st.write("### EDA Projet on Titan Company Dataset")
            st.write("""
                    - Analyzed lifetime dataset of Tanishq stores at multiple regions, identifying insights to drive business growth by 5%.
                    - Conducted exploratory data analysis to uncover trends and patterns such as people of particular region are interested in buying which type of jewellery, enabling data-driven decision-making.
                    - Visualized key metrics to analyze where the company is performing well and where it needs improvement.
                    """)
            if st.button("Know More 🎂"):
                with st.expander("### Technologies Used", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("- Python")
                        st.write("- Pandas")
                        st.write("- Numpy")
                    with col2:
                        st.write("- Matplotlib")
                        st.write("- Seaborn")
                        st.write("- Plotly")
    
    # Project 4 Container
    with st.container():
        st.write("---")
        st.write("##")
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/f2e469ad-fe3c-471c-a817-b1768ab0312f/Yh7qlSV0Uq.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="project5")
            else:
                st.error("Failed to load Lottie animation.")
                
        with text_col:
            st.write("### RON Seat Booking System")
            st.write("""
                    - Developed a responsive 2D web application using HTML, CSS, JavaScript, and MySQL.
                    - Utilized for booking seats in the office, displaying available seats, and providing a seamless booking experience.
                    - Helps users to check availability, manage their bookings with ease and plan accordingly there trips.
                    """)
            if st.button("Know More 😄"):
                with st.expander("### Technologies Used", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("- HTML")
                        st.write("- CSS")
                        st.write("- JavaScript")
                    with col2:
                        st.write("- MySQL")
                        st.write("- Python")
                
                with st.expander("### Project Link", expanded = False):
                    st.write("[Click Here to Check the Source Code](https://github.com/SharmaYash2423/RON-Seat-Booking-System)")
                    
# Achievements Function --------------------------------------------------------------------------------------------------------------
def Achievements():
    with st.container():
        st.write("# 🏆 My Achievements")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
                        - 🧠 Helped the company getting most useful insights for future growth and enhancements.
                        - 🌟 Help many events as a team lead and recieved many rewards for the same.
                        - ⚽ Winner of multiple District Level Basketball Tournaments. Go team!
                    """)
            st.markdown("""
                        I believe that every achievement, big or small, is a stepping stone towards success. I am always eager to learn and grow, and I am excited to see what the future holds for me. 🚀
                        """)
        with col2:
            lottie_url = "https://lottie.host/a7990eb1-5152-4cd1-a7fd-e0c592683b97/KOvlwaJ4uL.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="achievements")
            else:
                st.error("Failed to load Lottie animation.")
        st.write("---")
        st.write("# 📚 I Like To Talk About")
        st.markdown("""
                    - **Data Science**
                    - **Machine Learning**
                    - **Deep Learning**
                    - **Artificial Intelligence**
                    - **Python Programming**
                    - **Web Development**
                    - **Data Analytics and Insights**
                    - **Computer Vision**
                    - **Natural Language Processing**
                    - **Data Structures & Algorithms**
                    - **Self-Improvement** 
                    """) 

# Skills Function --------------------------------------------------------------------------------------------------------------
def Skills():
    
    with st.container():
        st.write("### 💼 My Skills")
        col1, col2 = st.columns(2)
        with col1:
            st.write("""
                    - **Languages**: Python, SQL, CSS, HTML, JavaScript, JSON
                    - **Libraries**: Pandas, Numpy, Matplotlib, Plotly, Seaborn
                    - **Frameworks**: Streamlit, Tailwind CSS, Bootstrap CSS
                    - **Tools**: Git, Jupyter Notebook, VS Code, Gradio
                    - **Databases**: MySQL, MongoDB Databases
                    - **Deep Learning**: Tensorflow, OpenCV, NLP & it's Libraries 
                    - **Soft Skills**: Teamwork, Communication, Problem-Solving, Time Management, Adaptability
                    - **Others**: Data Structures & Algorithms, Computer Vision, Natural Language Processing
                """)
        with col2:
            lottie_url = "https://lottie.host/e0f72cc9-db24-4eac-a85e-19bb821629f9/mumuEVoTHL.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="skills")
            else:
                st.error("Failed to load Lottie animation.")

# Setting Sidebar Main Menu ------------------------------------------------------------------------------------------------------------
with st.sidebar:
    selected_page = option_menu(
        "Navigate Here", 
        ["Home", "Projects", "Achievements","Skills"],
        icons = ['house', 'braces', 'trophy', 'code'],
        menu_icon = "cast",
        default_index = 0,
        )

# Displaying Selected Page --------------------------------------------------------------------------------------------------------------

if selected_page == "Home":
    Home()
elif selected_page == "Projects":
    Projects()
elif selected_page == "Achievements":
    Achievements()
elif selected_page == "Skills":
    Skills()