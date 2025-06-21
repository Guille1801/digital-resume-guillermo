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
PAGE_TITLE = "ディジタルCV | Guillermo Anhuaman"
PAGE_ICON = "👨‍💻"
NAME = "Guillermo Anhuaman"
DESCRIPTION = "データサイエンティスト | Python開発者"
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
with open(resume_file_jp, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

#--- HERO SECTION ---
col1, col2 = st.columns([1, 2])
with col1:
    st.image(profile_pic, width = 230)
with col2:
    st.title("Guillermo Anhuaman")
    st.write(DESCRIPTION)


    st.download_button(
        label="📄履歴書ダウンロード",
        data=PDFbyte,
        file_name=resume_file_jp.name,
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
st.subheader("【スキル】")
st.write("---")
st.markdown("<h4>🛠️ ハードスキル</h4>", unsafe_allow_html=True)
st.write("- ✅ **道具**: Microsoft Excel, Canva, Power BI, GitHub, Visual Studio Code, Jupyter Notebook, Google Colab")
st.write("- ✅ **データ可視化**: Matplotlib, Seaborn, Power BI")
st.write("- ✅ **プログラミング言語**: Python, R, SQL, HTML, CSS, JavaScript, C++ (beginner)")
st.write("- ✅ **フレームワークとライブラリー**: Pandas, NumPy, Scikit-learn, BeautifulSoup, Streamlit, Requests, Django, SQLite, Selenium")
st.write("- ✅ **データベース**: PostgreSQL, SQLite")
st.markdown("<h4>🤝 ソフトスキル</h4>", unsafe_allow_html=True)
st.write("- ✔️ 学ぶ意欲、チームワーク、積極的なコミュニケーション、問題解決力、適応力、時間管理能力、主体性、リーダーシップ")
st.markdown("<h4>🌐 言語</h4>", unsafe_allow_html=True)

st.write("- ✅ **スペイン語**: ネイティブ")
st.write("- ✅ **英語**: ネイティブ")
st.write("- ✅ **日本語**: N3 (会話のレベル)")



# --- WORK EXPERIENCE ---
st.write("#")
st.subheader("【職務経験】")
st.write("---")

#--- JOB 1 ---
st.write("**🏢テックリクルート | Spotted Staffing**")
st.write("2025年4月 - 現在")
st.write(
    """
- ➤ LinkedInのプロフィールリンクだけで、データを自動的に取得するツールを作成しました。
- ➤ クライアントの求人要件を分析して、最適な候補者を見つけるサポートをしました。
- ➤ GitHubやLinkedIn Recruiterなどのツールを使って、条件に合う候補者を検索しました。
- ➤ クライアントと候補者の間で円滑なコミュニケーションができるように、採用マネージャーと密に連携しました。

""")

#--- JOB 2 ---
st.write("#")
st.write("**🏢ウェブマスターインターン | TRG International**")
st.write("2024年4月 - 2025年3月")
st.write(
    """
- ➤ WordPressを使って会社のウェブサイトを開発・管理し、使いやすい体験を提供しました。
- ➤ SEO戦略を実施し、ウェブサイトの検索エンジンでの表示順位を向上させました。
- ➤ マーケティングチームと協力して、魅力的なコンテンツを作成し、ウェブサイトのパフォーマンスを最適化しました。
- ➤ ウェブサイトの分析データをモニタリングし、パフォーマンスを追跡して改善点を見つけました。
""")

#--- JOB 3 ---
st.write("#")
st.write("**🏢Python基礎科目のティーチングアシスタント｜| 東京国際大学**")
st.write("2024年8月 - 2024年12月")
st.write(
    """
- ➤ 1年生の学生にPythonの基礎を教える先生をサポートしました。学生がよく分かるように手伝いました。
- ➤ スライド、練習問題、テストなどの授業の資料を作りました。
- ➤ ラボの時間に学生のプログラムの課題をサポートしました。
- ➤ 学生の進み具合をチェックして、もっと分かるようにアドバイスをしました。
""")