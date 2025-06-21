from pathlib import Path

import streamlit as st
from PIL import Image

#--- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file_sp = current_dir / "assets" / "Guillermo_CV_es.pdf"
resume_file_en = current_dir / "assets" / "Guillermo_CV_en.pdf"
resume_file_jp = current_dir / "assets" / "Guillermo_Anhuaman履歴書.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
with open("views/assets/linkedin.svg", "r", encoding="utf-8") as f:
    linkedin_icon = f.read()
with open("views/assets/github.svg", "r", encoding="utf-8") as f:
    github_icon = f.read()
with open("views/assets/twitter.svg", "r", encoding="utf-8") as f:
    twitter_icon = f.read()

#---GENERAL SETTINGS---
PAGE_TITLE = "Digital CV | Guillermo Anhuaman"
PAGE_ICON = "👨‍💻"
NAME = "Guillermo Anhuaman"
DESCRIPTION = "Data Scientist & Engineer specializing in Python development and data-driven solutions"
EMAIL = "guillermoanhuaman18@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": ["https://www.linkedin.com/in/guillermoanhuaman/", linkedin_icon],
    "GitHub": ["https://github.com/Guille1801", github_icon],
    "Twitter": ["https://x.com/Guiller38746059", twitter_icon],
}

PROJECTS = {
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#--- LOAD CSS, PROFILE PIC, AND RESUME ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file_en, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

#--- HERO SECTION ---
col1, col2 = st.columns([1, 2])
with col1:
    st.image(profile_pic, width = 230, use_container_width= True)
with col2:
    st.markdown(f"<h1 align= 'center'>{NAME}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p align = 'center'>{DESCRIPTION}</p>", unsafe_allow_html=True)


    st.download_button(
        label="📄Download Resume",
        data=PDFbyte,
        file_name=resume_file_en.name,
        mime="application/octet-stream")


    st.write(f"📧 {EMAIL}")

    #--- SOCIAL MEDIA LINKS ---
st.write("#")

col1, col2, = st.columns([1, 7], gap="small")
with col1:
    st.write("")

with col2:

    cols = st.columns(3, gap="small")
    for index, (platform, (link, icon)) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].markdown(
        f"""
        <div style="display: flex; align-items: center; gap: 6px;">
            <div style="width: 20px; height: 20px; display: flex; align-items: center;">
                {icon}
            </div>
            <a href="{link}" target="_blank" style="text-decoration: none; font-weight: 500; font-size: 16px;">
                {platform}
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
# --- SKILLS SECTION ---
st.write("#")
st.subheader("Skills")
st.write("---")
st.markdown("<h4>🛠️ Hard Skills</h4>", unsafe_allow_html=True)
st.write("- ✅ **Tools**: Microsoft Excel, Canva, Power BI, GitHub, Visual Studio Code, Jupyter Notebook, Google Colab")
st.write("- ✅ **Data Visualization**: Matplotlib, Seaborn, Power BI")
st.write("- ✅ **Programming Languages**: Python, R, SQL, HTML, CSS, JavaScript, C++ (beginner)")
st.write("- ✅ **Frameworks & Libraries**: Pandas, NumPy, Scikit-learn, BeautifulSoup, Streamlit, Requests, Django, SQLite, Selenium")
st.write("- ✅ **Databases**: PostgreSQL, SQLite")
st.markdown("<h4>🤝 Soft Skills</h4>", unsafe_allow_html=True)
st.write("- ✔️ Eager to Learn, Teamwork, Communication, Problem Solving, Adaptability, Time Management, Leadership")
st.markdown("<h4>🌐 Languages</h4>", unsafe_allow_html=True)

st.write("- ✅ **Spanish**: Native")
st.write("- ✅ **English**: Native")
st.write("- ✅ **Japanese**: N3 (Intermediate)")



# --- WORK EXPERIENCE ---
st.write("#")
st.subheader("Work Experience")
st.write("---")

#--- JOB 1 ---
st.write("**🏢Tech Recruiter Intern | Spotted Staffing**")
st.write("April 2025 - Present")
st.write(
    """
- ➤ Automate data extraction from LinkedIn profiles using just the profile link. 
- ➤ Analyze client requirements for different positions they want to fill, in order to find candidates who are the perfect fit for their company. 
- ➤ Use tools such as GitHub and LinkedIn Recruiter to search for candidates that meet client requirements. 
- ➤ Collaborate closely with Hiring Managers to ensure clear communication between client and candidate. 
- ➤ Collaborate closely with hiring managers to ensure a smoothly screening process.

""")

#--- JOB 2 ---
st.write("#")
st.write("**🏢Web Master Intern | TRG International**")
st.write("August 2024 - March 2025")
st.write(
    """
- ➤ Develop and maintain the company's website using WordPress, ensuring a user-friendly experience.
- ➤ Implement SEO strategies to improve website visibility and search engine rankings.
- ➤ Collaborate with the marketing team to create engaging content and optimize website performance.
- ➤ Monitor website analytics to track performance and identify areas for improvement.
""")

#--- JOB 3 ---
st.write("#")
st.write("**🏢Student Assistant of Foundations of Python| Tokyo International University**")
st.write("August 2024 - December 2025")
st.write(
    """
- ➤ Offer one-on-one tutoring and group study sessions to reinforce key Python concepts. 
- ➤ Help the professor if any student has a question or problems in their PC 
- ➤ Collaborate with faculty to develop course materials, assignments, and provide feedback. 
- ➤ Design interactive practical exercises to boost engagement and deepen students understanding.
""")