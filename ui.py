
import re
import streamlit as st
from youtube_video_analyzer import build_youtube_agent

# To run the file: python -m streamlit run "file_path"

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="TubeNotes | YouTube Analyzer",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background: #0b0d12;
        color: #f1f3f9;
    }

    [data-testid="stHeader"] {
        background: rgba(11, 13, 18, 0.85);
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #11141b;
        border-right: 1px solid #252936;
    }

    /* Typography */
    h1, h2, h3 {
        color: #f6f7fb !important;
        letter-spacing: -0.5px;
    }

    p, label {
        color: #b3b9c8;
    }

    /* Hero section */
    .hero {
        padding: 1.5rem 0 1.8rem 0;
    }

    .eyebrow {
        color: #ff565f;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
    }

    .hero-title {
        font-size: clamp(2.2rem, 5vw, 3.6rem);
        line-height: 1.1;
        font-weight: 800;
        letter-spacing: -2px;
        margin: 0;
        color: #ffffff;
    }

    .hero-title span {
        color: #ff525b;
    }

    .hero-subtitle {
        max-width: 650px;
        color: #9ca4b5;
        font-size: 1.05rem;
        line-height: 1.8;
        margin-top: 1rem;
    }

    /* Cards */
    .feature-card {
        background: linear-gradient(145deg, #171b25, #11141b);
        border: 1px solid #292e3a;
        border-radius: 16px;
        padding: 1.25rem;
        min-height: 150px;
    }

    .feature-icon {
        font-size: 1.5rem;
        margin-bottom: 0.7rem;
    }

    .feature-title {
        color: #f5f6fa;
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 0.45rem;
    }

    .feature-desc {
        color: #969fb1;
        font-size: 0.88rem;
        line-height: 1.6;
    }

    /* Input */
    div[data-testid="stTextInput"] input {
        background: #121620;
        border: 1px solid #343b4b;
        color: #ffffff;
        border-radius: 10px;
        min-height: 3.1rem;
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: #ff525b;
        box-shadow: 0 0 0 1px #ff525b;
    }

    /* Buttons */
    .stButton > button,
    .stDownloadButton > button {
        border-radius: 10px;
        min-height: 3rem;
        font-weight: 700;
        transition: all 0.2s ease;
    }

    .stButton > button[kind="primary"] {
        background: #ff414b;
        border: 1px solid #ff414b;
        color: white;
    }

    .stButton > button[kind="primary"]:hover {
        background: #e92e3a;
        border-color: #e92e3a;
        transform: translateY(-1px);
    }

    /* Report containers */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-color: #292e3a;
        border-radius: 15px;
    }

    hr {
        border-color: #292e3a;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #727b8e;
        font-size: 0.8rem;
        padding-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# AGENT INITIALIZATION
# --------------------------------------------------
@st.cache_resource
def get_agent():
    return build_youtube_agent()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:
    st.markdown("## 🎬 TubeNotes")
    st.caption("YOUTUBE INTELLIGENCE")

    st.divider()

    st.markdown("### ✨ What you can do")
    st.markdown(
        """
        - 📋 Video summaries
        - ⏱️ Topic timestamps
        - 🧠 Key learning points
        - 💻 Technical explanations
        - 📚 Organized notes
        """
    )

    st.divider()

    st.markdown("### 🚀 How to use")
    st.markdown(
        """
        **01** — Copy a YouTube link

        **02** — Paste it into the analyzer

        **03** — Click Analyze Video

        **04** — Read or download your report
        """
    )

    st.divider()

    st.caption("Powered by Python · Streamlit · Agno")


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">YOUR PERSONAL VIDEO RESEARCHER</div>
        <div class="hero-title">
            Watch less.<br>
            <span>Understand more.</span>
        </div>
        <div class="hero-subtitle">
            Turn long YouTube videos into structured insights,
            meaningful timestamps, and actionable learning notes
            with your AI-powered video analyst.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# --------------------------------------------------
# VIDEO INPUT
# --------------------------------------------------
st.markdown("### 🔗 Analyze a video")
st.caption("Paste a public YouTube video link to get started.")

with st.form("video_analysis_form"):
    video_url = st.text_input(
        "YouTube URL",
        placeholder="https://www.youtube.com/watch?v=...",
        help="Paste the URL of the video you want to analyze.",
    )

    submitted = st.form_submit_button(
        "Analyze Video",
        type="primary",
        use_container_width=True,
    )

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "analysis_report" not in st.session_state:
    st.session_state.analysis_report = None

if "analyzed_url" not in st.session_state:
    st.session_state.analyzed_url = None

# --------------------------------------------------
# VALIDATION + ANALYSIS
# --------------------------------------------------
if submitted:
    if not video_url.strip():
        st.warning("Please paste a YouTube video URL first.")

    elif not re.match(
        r"^(https?://)?(www\.)?"
        r"(youtube\.com/(watch\?.*v=|shorts/|embed/)|youtu\.be/)"
        r"[\w-]+",
        video_url.strip(),
    ):
        st.error("That doesn't look like a valid YouTube URL. Please check it.")

    else:
        try:
            with st.spinner(
                "🎬 Analyzing your video... This may take a little while."
            ):
                agent = get_agent()

                response = agent.run(
                    f"""
                    Analyze this YouTube video: {video_url.strip()}

                    Provide a structured report with:
                    1. Video overview and available metadata
                    2. Main topics and their progression
                    3. Meaningful timestamps, if supported by the transcript
                    4. Key learning points
                    5. Practical demonstrations and references

                    Do not invent video details or timestamps.
                    Clearly state if the transcript is unavailable.
                    """
                )

                report = getattr(response, "content", None)

                if not report:
                    st.error(
                        "The agent returned no report. "
                        "Check the terminal for errors."
                    )
                else:
                    st.session_state.analysis_report = str(report)
                    st.session_state.analyzed_url = video_url.strip()

        except Exception as error:
            st.error(
                "Something went wrong while analyzing the video. "
                "Please check your API configuration and terminal logs."
            )
            with st.expander("Technical error details"):
                st.exception(error)

# --------------------------------------------------
# FEATURE CARDS
# --------------------------------------------------
st.markdown("### Built for smarter learning")
st.write("Everything you need to get more value from every video.")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">⏱️</div>
            <div class="feature-title">Smart Timestamps</div>
            <div class="feature-desc">
                Navigate key topics and important moments
                without watching every second.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <div class="feature-title">Deep Insights</div>
            <div class="feature-desc">
                Extract core concepts, key takeaways,
                and important explanations.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">📚</div>
            <div class="feature-title">Learning Notes</div>
            <div class="feature-desc">
                Transform video content into organized
                notes for revision and future reference.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --------------------------------------------------
# ANALYSIS REPORT
# --------------------------------------------------
if st.session_state.analysis_report:
    st.divider()

    st.markdown("## 📑 Your Analysis Report")
    st.caption(f"Video: {st.session_state.analyzed_url}")

    st.link_button(
        "▶ Open Original Video",
        st.session_state.analyzed_url,
    )

    with st.container(border=True):
        st.markdown(st.session_state.analysis_report)

    st.download_button(
        label="⬇️ Download Analysis Report",
        data=st.session_state.analysis_report,
        file_name="youtube_analysis_report.md",
        mime="text/markdown",
        use_container_width=True,
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown(
    """
    <div class="footer">
        Built with ❤️ using Python, Streamlit and Agno<br>
        AI-generated insights may require verification.
    </div>
    """,
    unsafe_allow_html=True,
)
