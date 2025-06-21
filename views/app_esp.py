from pathlib import Path

import streamlit as st
from PIL import Image

#--- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file_sp = current_dir / "assets" / "Guillermo CV.pdf"
resume_file_en = current_dir / "assets" / "David CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
with open("views/assets/linkedin.svg", "r", encoding="utf-8") as f:
    linkedin_icon = f.read()
with open("views/assets/github.svg", "r", encoding="utf-8") as f:
    github_icon = f.read()
with open("views/assets/twitter.svg", "r", encoding="utf-8") as f:
    twitter_icon = f.read()

#---GENERAL SETTINGS---
PAGE_TITLE = "CV Digital | Guillermo Anhuaman"
PAGE_ICON = "👨‍💻"
NAME = "Guillermo Anhuaman"
DESCRIPTION = "Data Scientist y Ingeniero especializado en Python, SQL y visualización de datos."
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
    st.title("Guillermo Anhuaman")
    st.write(DESCRIPTION)


    st.download_button(
        label="📄Descargar curriculum",
        data=PDFbyte,
        file_name=resume_file_sp.name,
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
st.write("- ✅ **Herramientas**: Microsoft Excel, Canva, Power BI, GitHub, Visual Studio Code, Jupyter Notebook, Google Colab")
st.write("- ✅ **Visualización de datos**: Matplotlib, Seaborn, Power BI")
st.write("- ✅ **Lenguajes de programación**: Python, R, SQL, HTML, CSS, JavaScript, C++ (beginner)")
st.write("- ✅ **Frameworks & Librerias**: Pandas, NumPy, Scikit-learn, BeautifulSoup, Streamlit, Requests, Django, SQLite, Selenium")
st.write("- ✅ **Bases de datos**: PostgreSQL, SQLite")
st.markdown("<h4>🤝 Soft Skills</h4>", unsafe_allow_html=True)
st.write("- ✔️ Ganas de aprender, Trabajo en equipo, Comunicación activa, Solucionador de problemas, Adaptabilidad, Gestión de tiempo, Proactividad, Liderazgo")
st.markdown("<h4>🌐 Idiomas</h4>", unsafe_allow_html=True)

st.write("- ✅ **Español**: Nativo")
st.write("- ✅ **Inglés**: Avanzado")
st.write("- ✅ **Japones**: N3 (Intermedio)")



# --- WORK EXPERIENCE ---
st.write("#")
st.subheader("Experiencia Laboral")
st.write("---")

#--- JOB 1 ---
st.write("**🏢Reclutador Tecnológico | Spotted Staffing**")
st.write("Abril 2025 - Presente")
st.write(
    """
- ➤ Automatizar la extracción de datos de perfiles de LinkedIn utilizando solo el enlace del perfil.
- ➤ Analizar los requisitos del cliente para diferentes puestos que desean cubrir, con el fin de encontrar candidatos que sean el ajuste perfecto para su empresa.
- ➤ Utilizar herramientas como GitHub y LinkedIn Recruiter para buscar candidatos que cumplan con los requisitos del cliente.
- ➤ Colaborar estrechamente con los Gerentes de Contratación para garantizar una comunicación clara entre el cliente y el candidato.

""")

#--- JOB 2 ---
st.write("#")
st.write("**🏢Web Master Intern | TRG International**")
st.write("Agosto 2024 - Marzo 2025")
st.write(
    """
- ➤ Desarrollar y mantener el sitio web de la empresa utilizando WordPress, asegurando una experiencia fácil de usar.
- ➤ Implementar estrategias de SEO para mejorar la visibilidad del sitio web y el posicionamiento en los motores de búsqueda.
- ➤ Colaborar con el equipo de marketing para crear contenido atractivo y optimizar el rendimiento del sitio web.
- ➤ Monitorear las analíticas del sitio web para rastrear el rendimiento e identificar áreas de mejora.
""")

#--- JOB 3 ---
st.write("#")
st.write("**🏢Estudiante Asistente de Fundamentos de Python| Tokyo International University**")
st.write("Agosto 2024 - Diciembre 2025")
st.write(
    """
- ➤ Asistir al profesor en la enseñanza de los fundamentos de Python a estudiantes de primer año, asegurando una comprensión sólida de los conceptos básicos.
- ➤ Preparar y presentar materiales de clase, incluyendo diapositivas, ejercicios prácticos y exámenes.
- ➤ Facilitar sesiones de laboratorio y ayudar a los estudiantes con sus proyectos de programación.
- ➤ Evaluar el progreso de los estudiantes y proporcionar retroalimentación constructiva para mejorar su comprensión de Python.
""")