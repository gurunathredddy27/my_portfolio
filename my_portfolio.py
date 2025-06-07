import streamlit as st
# import PyPDF2

# --- Page config ---
st.set_page_config(page_title="Gurunath | Portfolio", layout="wide")

# --- Helper to Extract PDF Text ---
# @st.cache_data
# def extract_text_from_pdf(pdf_path):
#     text = ""
#     with open(pdf_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         for page in reader.pages:
#             text += page.extract_text()
#     return text

# resume_path = r"C:\Users\91944\Downloads\resume\Guru2025.pdf"
# resume_text = extract_text_from_pdf(resume_path)

# --- Personal Info ---
personal_info = {
    "name": "Gurunath Tokala",
    "title": "AI/ML Enthusiast & Data Science | Python Developer",
    "summary": (
        "Summary:\n\n"
        "👉 Driven by curiosity and precision, I build intelligent systems using Python, ML, and SQL. \n\n"
        "👉 I love exploring datasets, uncovering hidden insights, and using AI to make smart, data-driven decisions\n\n"
        "👉 Skilled in NLP, Neural Networks, and solving real-world problems with data.\n\n"
    ),
    "email": "gurunathreddy2727@gmail.com",
    "linkedin": "https://www.linkedin.com/in/gurunath-tokala/",
    "github": "https://github.com/gurunathredddy27"
}

# --- Education ---
education = [
    {
        "degree": "B.Tech in Computer Science",
        "institution": "👉 College: Visvesvaraya College of Engineering and Technology",
        "year": "2018 - 2022",
        "details": "- Completed core coursework in Data Structures, Algorithms, and Object-Oriented Programming. \n\n"
        "- Gained hands-on experience with Java and Python. \n\n"
        "- Worked on mini-projects and final year project focused on practical applications of computer science concepts."
    },
    {
        "degree": "Full Stack Development",
        "institution": "👉 Institution: BridgeLab",
        "year": "2023",
        "details": "- Basic and Advance Object-Oriented Programming with Java.\n\n - Web Applications with HTML, CSS, JS."
    }
]

# --- Skills ---
# skills = {
#     "Python": 90,
#     "Machine Learning": 85,
#     "Deep Learning": 70,
#     "HTML/CSS": 70,
#     "SQL": 65,
#     "Streamlit": 80,
#     "Pandas/Numpy": 85
# }

# --- Experience ---
experience = [
    {
        "year": "Feb 2025 - Present",
        "role": "Software Engineer",
        "company": "Lyrostech",
        "description": "Handled data analysis, developed ML models, and executed end-to-end projects."
    },
    {
        "year": "Feb 2024 - Nov 2024",
        "role": "Freelance Content Reviewer",
        "company": "Centific",
        "description": "Reviewed and evaluated machine-generated content for accuracy and quality."
    },
    {
        "year": "Sep 2022 - May 2023",
        "role": "Technical Assistant",
        "company": "RACEnergy",
        "description": "Handled data entry, troubleshooting, and technical documentation."
    }
]

# --- Projects ---
projects = [
    {
        "name": "🎓 Student Grading System",
        "desc": (
            "- Developed a Tkinter-based GUI to manage student marks\n"
            "- Implemented role-based access for admins and teachers\n"
            "- Used Pandas for data handling and predictive grade analysis"
        )
    },
    {
        "name": "🏠 Airbnb Price Prediction",
        "desc": (
            "- Built regression models to predict listing prices\n"
            "- Analyzed key features affecting price fluctuations\n"
            "- Enabled data-driven pricing recommendations"
        )
    },
    {
        "name": "🎬 Movie Recommendation System",
        "desc": (
            "- Utilized NLP techniques like CountVectorizer and TF-IDF\n"
            "- Calculated cosine similarity for personalized recommendations\n"
            "- Created a scalable model to suggest movies based on user preferences"
        )
    },
    {
        "name": "🔍 Customer Segmentation using Machine Learning",
        "desc": (
            "- Applied K-Means clustering to group customers\n"
            "- Analyzed behavioral patterns and demographics\n"
            "- Supported targeted marketing and business strategies"
        )
    }
]

# --- Sidebar Branding ---
# st.sidebar.image("https://easydrawingguides.com/wp-content/uploads/2019/01/how-to-draw-thors-hammer-featured-image-1200.png"
# , width=140)

# st.sidebar.image("https://www.vectorkhazana.com/assets/images/products/Pokemon_Pikachu_Logo.png", width=140)





# --- Sidebar Navigation Buttons ---
st.sidebar.title("📌 Navigation")
st.sidebar.markdown("""
    <style>
    .stButton>button {
        display: block;
        width: 100%;
        margin-bottom: 0.5rem;
        font-weight: bold;
        background-color: #f0f2f6;
        color: #000;
        border-radius: 6px;
        
    }
    .stButton>button:hover {
        background-color: #ffeecc;
        color: #000;
    }
    </style>
""", unsafe_allow_html=True)

# Set page from session
if 'page' not in st.session_state:
    st.session_state.page = "About Me"

pages = ["About Me", "Skills", "Experience", "Education", "Projects", "Contact"]
for p in pages:
    if st.sidebar.button(p):
        st.session_state.page = p

page = st.session_state.page

# --- About Me ---
if page == "About Me":
    st.title(f"👋 Hi, I'm {personal_info['name']}")
    st.markdown(f"### {personal_info['title']}")
    st.info(personal_info['summary'])

    st.markdown(f"""
    **📧 Email:** [{personal_info['email']}](mailto:{personal_info['email']})  
    **🔗 LinkedIn:** [{personal_info['linkedin']}]({personal_info['linkedin']})  
    **💻 GitHub:** [{personal_info['github']}]({personal_info['github']})
    """)

# --- Skills ---
elif page == "Skills":
    st.header("🧠 Skills Overview")
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 💻 Programming")
        st.markdown("- **Java**, **Python**")

        st.markdown("#### 🌐 Web Technologies")
        st.markdown("- **HTML/CSS**")

        # st.markdown("#### 🖥️ Operating Systems")
        # st.markdown("- **Windows**")

        st.markdown("#### 🔄 Version Control")
        st.markdown("- **Git**")

        st.markdown("#### 🗄️ Databases")
        st.markdown("- **MySQL**, **SQL**")

 

    with col2:
        # 📊 Visualization Tools & IDEs
        st.markdown("#### 📊 Visualization Tools & IDEs")
        st.markdown("- **Power BI**, **Matplotlib**, **Seaborn**")
        st.markdown("- **Visual Studio Code**,  **Jupyter**,  **IntelliJ**, **Colab**")

        # 🧠 Data Science & AI
        st.markdown("#### 🧠 Data Science & AI")
        # st.markdown("#### 📊 Data Science & AI")
        # st.markdown("- **AI/ML**, **Data Science**")
        st.markdown("- **Machine Learning**")
        st.markdown("-  **Deep Learning**")
        st.markdown("-  **NLP**")
        st.markdown("-  **Pandas**, **NumPy**")
        st.markdown("-  **Streamlit**")

# --- Experience ---
elif page == "Experience":
    st.header("💼 Experience Timeline")
    for exp in experience:
        with st.container():
            st.subheader(f"{exp['role']} @ {exp['company']}")
            st.markdown(f"**📅 {exp['year']}**")
            st.write(exp['description'])
            st.markdown("---")

# --- Education ---
elif page == "Education":
    st.header("🎓 Education")
    for edu in education:
        st.subheader(f"{edu['institution']}")
        st.markdown(f"{edu['degree']}")
        st.markdown(f"**📅 {edu['year']}**")
        st.info(edu['details'])
        st.markdown("---")

# --- Projects ---
elif page == "Projects":
    st.header("🛠 Projects Showcase")
    for proj in projects:
        st.markdown(f"#### {proj['name']}")
        st.success(proj['desc'])

# --- Contact ---
elif page == "Contact":
    st.header("📬 Contact Me")
    contact_form = """
    <form action="https://formsubmit.co/gurunathreddy2727@gmail.com" method="POST">
         <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 10px;"><br><br>
         <input type="email" name="email" placeholder="Your email" required style="width: 100%; padding: 10px;"><br><br>
         <textarea name="message" placeholder="Your message" required style="width: 100%; padding: 10px;"></textarea><br><br>
         <button type="submit" style="padding: 10px 20px; background-color: teal; color: white;">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
    st.markdown("💡 Tip: Replace your email with the one you want to receive messages on.")

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align:center; font-size:16px;">
    Data speaks, Python listens, and I build — with love 💖 and passion. <br>  © 2025 Gurunath Tokala
</div>
""", unsafe_allow_html=True)
