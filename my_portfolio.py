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
        "Summary:\n"
        "👉 I love exploring datasets, uncovering hidden insights, and using AI to make smart, data-driven decisions\n\n"
        "👉 Driven by curiosity and precision, I build intelligent systems using Python, ML, and SQL\n\n"
        "👉 Skilled in NLP, Neural Networks, and solving real-world problems with data\n\n"
        "👉 Automating tasks and integrating AI into DevOps pipelines to improve efficiency, reliability, and scalability\n\n"
        "👉 Documenting project progress and sharing insights to ensure continuous improvement"
    ),
    "contact": {
        "email": "gurunathreddy2727@gmail.com",
        "linkedin": "https://www.linkedin.com/in/gurunath-tokala/",
        "github": "https://github.com/gurunathredddy27"
    }
}


# --- Education ---
education = [
    {
        "degree": "B.Tech in Computer Science",
        "institution": "👉 College: Visvesvaraya College of Engineering and Technology",
        "year": "2018 - 2022",
        "details": "- Completed core coursework in Data Structures, Algorithms, DBMS, OS, CN and Object-Oriented Programming. \n\n"
        "- Gained hands-on experience with Java and Python for software development and problem solving \n\n"
        "- Final year project focused on developing a real-world software solution using ML concepts\n\n "
        "- Additionally, I actively participated in sports, given presentations on emerging technologies, and co-ordinated several events, which helped enhance my leadership and collaboration skills."
    },
    {
        "degree": "Full Stack Development",
        "institution": "👉 Institution: BridgeLab",
        "year": "2023",
        "details": "- Mastered Basic and Advanced Object-Oriented Programming (OOP) concepts using Java.\n\n - Built responsive web applications using HTML, CSS, and JavaScript.\n\n - Gained hands-on experience with version control (Git & GitHub)\n\n - Learned basic database operations using SQL for full-stack integration"
    }
]

# --- Skills ---
 
# --- Experience ---
experience = [
    {
    "year": "Feb 2025 - Present",
    "role": "Software Engineer",
    "company": "Lyrostech",
    "description": (
        "- Handled data analysis, developed ML models, and executed end-to-end projects\n"
        "- Built and deployed regression and classification models using Scikit-learn\n"
        "- Designed and trained deep learning models and neural networks using TensorFlow/Keras\n"
        "- Applied NLP techniques including text classification and sentiment analysis\n"
        "- Experimented with transformer-based models (BERT, LLMs) for advanced language tasks\n"
        "- Integrated machine learning pipelines with Streamlit and Flask for real-time user interaction\n"
    )
}
,
    {
        "year": "Feb 2024 - Nov 2024",
        "role": "Freelance Content Reviewer",
        "company": "Centific",
        "description": (
            "- Evaluated AI-generated responses for factual accuracy and clarity\n"
            "- Assessed language fluency, tone, and coherence of machine outputs\n"
            "- Ensured alignment with brand guidelines and ethical standards\n"
            "- Provided detailed feedback to improve AI language models"
        )
    },
     {
        "year": "Sep 2021 - May 2023",
        "role": "Technical Assistant",
        "company": "RACEnergy",
        "description": (
            "- Maintained technical documentation and prepared standard operating procedures (SOPs)\n"
            "- Assisted in troubleshooting and repairing EV infrastructure equipment\n"
            "- Maintained equipment logs and collaborated with engineering teams\n"
            "- Coordinated with engineering teams for hardware testing and diagnostics"
        )
    }
]

# --- Personal Projects ---
personal_projects = [{
        "name": "🔍 Customer Segmentation using Machine Learning",
        "desc": (
            "- Applied K-Means clustering to group customers\n"
            "- Analyzed behavioral patterns and demographics\n"
            "- Supported targeted marketing and business strategies"
        )
    },
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
    "name": "🩺 Diabetes Prediction with Classification Models",
    "desc": (
        "- Developed classification models (Logistic Regression, Random Forest, SVM, etc.) to predict diabetes likelihood\n"
        "- Performed data preprocessing, EDA, and handled class imbalance where necessary\n"
        "- Evaluated models using accuracy, precision, recall, and F1-score to select the best-performing classifier\n"
        "- Successfully deployed the final model using Flask as a web application"
    )
}

]

# --- Professional Projects ---
professional_projects = [
    {
        "name": "🎬 Movie Recommendation System",
        "desc": (
            "- Utilized NLP techniques like CountVectorizer and TF-IDF\n"
            "- Calculated cosine similarity for personalized recommendations\n"
            "- Created a scalable model to suggest movies based on user preferences"
        )
    },
    {
    "name": "🏡 House Price Prediction with Regression Models",
    "desc": (
        "- Built multiple regression models (Linear, SVR, Randomforest, etc.) for predicting house prices\n"
        "- Evaluated models using R² score and selected the best-performing algorithm\n"
        "- Performed EDA and feature engineering for better prediction accuracy\n"
        "- Successfully deployed the model using Flask as a web app"
    )
}

    
]

# --- Sidebar Branding ---
# st.sidebar.image("https://easydrawingguides.com/wp-content/uploads/2019/01/how-to-draw-thors-hammer-featured-image-1200.png"
# , width=140)

st.sidebar.image("https://www.vectorkhazana.com/assets/images/products/Pokemon_Pikachu_Logo.png", width=140)





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

pages = ["About Me", "Education","Skills", "Experience", "Projects", "Contact"]
for p in pages:
    if st.sidebar.button(p):
        st.session_state.page = p

page = st.session_state.page

# --- About Me ---
if page == "About Me":
    st.title(f"👋 Hi, I'm {personal_info['name']}")
    st.markdown(f"### {personal_info['title']}")
    # st.success(personal_info['summary'])
    st.markdown(f"""
        <div style="
            border: 1px solid #444444;
            padding: 16px;
            border-radius: 10px;
            font-size: 15.5px;
            line-height: 1.7;
            color: #dddddd;
        ">
        {personal_info['summary'].replace('\n', '<br>')}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    # st.write("Contact:")
    st.markdown(f"""
        **📧 Email:** [{personal_info['contact']['email']}](mailto:{personal_info['contact']['email']})  
        **🔗 LinkedIn:** [{personal_info['contact']['linkedin']}]({personal_info['contact']['linkedin']})  
        **💻 GitHub:** [{personal_info['contact']['github']}]({personal_info['contact']['github']})
        """)
    

 
#skills ------------

elif page == "Skills":
    st.header("🧠 Skills Overview")
    st.markdown("---")
 # --- Categorized Grid Layout ---
    st.subheader("📂 Skills Breakdown")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 💻 Programming Languages")
        st.markdown("- Java\n- Python\n- SQL")

        st.markdown("#### 📊 Data Science & AI")
        st.markdown("""
        - Machine Learning  
        - Deep Learning  
        - NLP  
        - Transformers  
        - LLMs  
        - Pandas / NumPy  
        """)

    with col2:
        st.markdown("#### 🧰 Frameworks & Libraries")
        st.markdown("""
        - Scikit-Learn
        - TensorFlow  
        - Keras  
        - Streamlit  
        - Flask  
        """)

        st.markdown("#### 🧠 Visualization Tools")
        st.markdown("""
        - Power BI  
        - Matplotlib  
        - Seaborn  
        """)

    with col3:
        st.markdown("#### ⚙️ IDEs & Development Tools")
        st.markdown("""
        - VS Code  
        - Jupyter  
        - Colab  
        - IntelliJ  
        """)

        st.markdown("#### 🚀 Deployment & DevOps")
        st.markdown("""
        - Docker  
        - Kubernetes  
        - CI/CD Pipelines  
        - GitHub Actions  
        - Render  
        - Supabase  
        """)
    st.markdown("---")

    # --- Technical Skills Rating with Dimmed Colors ---
    st.subheader("📌 Technical Skills Rating (Out of 10)")
    tech_skills = {
        "Python": (9, "#e57373"),           # Soft Red
        "Machine Learning": (8.5, "#ffb74d"),  # Soft Orange
        "Deep Learning": (7, "#aed581"),     # Soft Green
        "Pandas/Numpy": (8.5, "#ce93d8"),    # Soft Purple
        "Streamlit": (8, "#81d4fa"),         # Soft Blue
        "SQL": (6.5, "#80deea"),             # Soft Cyan
        "NLP": (7, "#b39ddb"),               # Soft Violet
        "LLM / Transformers": (6.5, "#fff176")  # Soft Yellow
    }

    for skill, (value, color) in tech_skills.items():
        filled = int((value / 10) * 100)
        st.markdown(f"""
            <div style="margin-bottom: 3px;">
                <strong>{skill}</strong>
                <div style="background-color: #e0e0e0; border-radius: 5px; height: 15px; width: 100%;">
                    <div style="width: {filled}%; background-color: {color}; height: 100%; border-radius: 5px;"></div>
                </div>
                <small>{value} / 10</small>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")



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
        st.success(edu['details'])
        st.markdown("---")


# --- Projects ---
elif page == "Projects":
    st.header("🛠 Projects Showcase")

    # Dropdown to select project type
    proj_type = st.selectbox("📂 Select Project Type", ["Personal", "Professional"], index=0)

    # Style for project box
    box_style = """
    <div style="
        border: 1px solid #888888;
        border-radius: 18px;
        padding: 15px;
        margin-bottom: 30px;   /* Increased from 15px to 30px */
        ">
        <h4 style="margin-bottom: 8px; color: #f2f2f2;">{name}</h4>
        <ul style="margin: 0; padding-left: 20px; font-size: 15px; color: #dddddd;">
            {desc_items}
        </ul>
    </div>
            """


    # Function to convert desc into HTML list
    def format_description(desc):
        return ''.join([f"<li>{line.strip('- ')}</li>" for line in desc.split('\n') if line.strip()])


    # Render projects
    projects = personal_projects if proj_type == "Personal" else professional_projects

    for proj in projects:
        desc_html = format_description(proj["desc"])
        st.markdown(box_style.format(name=proj["name"], desc_items=desc_html), unsafe_allow_html=True)

 

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
