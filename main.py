# app.py
import streamlit as st
from PIL import Image

from app.classifier import DeepfakePredictor

# =====================
# 1️⃣ Page Config & Theme
# =====================
st.set_page_config(
    page_title="Deepfake Detector",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS (keep your same CSS block here)
st.markdown("""<style>/* your same CSS styles */</style>""", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    /* Main app styling */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Title styling */
    h1 {
        background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        font-size: 3.5rem !important;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }
    
    /* Subtitle styling */
    .subtitle {
        text-align: center;
        color: #b8b8d4;
        font-size: 1.2rem;
        margin-bottom: 3rem;
        font-weight: 400;
    }
    
    /* Card container */
    .card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2.5rem;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.08);
        margin: 2rem 0;
    }
    
    /* File uploader styling */
    .stFileUploader {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 15px;
        padding: 2rem;
        border: 2px dashed rgba(168, 237, 234, 0.3);
        transition: all 0.3s ease;
    }
    
    .stFileUploader:hover {
        border-color: rgba(168, 237, 234, 0.6);
        background: rgba(255, 255, 255, 0.05);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
        color: #1a1a2e;
        font-weight: 600;
        font-size: 1.1rem;
        padding: 0.75rem 3rem;
        border-radius: 50px;
        border: none;
        box-shadow: 0 4px 15px 0 rgba(168, 237, 234, 0.4);
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 1.5rem;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px 0 rgba(168, 237, 234, 0.6);
    }
    
    /* Info/Success/Warning boxes */
    .stAlert {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        border-left: 4px solid;
        padding: 1rem 1.5rem;
    }
    
    /* Success message */
    .element-container:has(.stSuccess) {
        animation: slideIn 0.5s ease;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Results container */
    .result-box {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 15px;
        padding: 2rem;
        margin-top: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Image/Video preview */
    .stImage, .stVideo {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        margin: 1.5rem 0;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #a8edea !important;
    }
    
    /* JSON viewer */
    .stJson {
        background: rgba(0, 0, 0, 0.3);
        border-radius: 12px;
        padding: 1rem;
        border: 1px solid rgba(168, 237, 234, 0.2);
    }
    
    /* Feature badges */
    .feature-badge {
        display: inline-block;
        background: rgba(168, 237, 234, 0.1);
        color: #a8edea;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.5rem;
        font-size: 0.9rem;
        border: 1px solid rgba(168, 237, 234, 0.3);
    }
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(168, 237, 234, 0.3), transparent);
        margin: 2rem 0;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# =====================
# 2️⃣ Header Section
# =====================
st.markdown("# 🎬 Detectify.AI")
st.markdown(
    '<p class="subtitle">Advanced AI-powered detection for images and videos</p>',
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        '<span class="feature-badge">🖼️ Image Analysis</span>', unsafe_allow_html=True
    )
with col2:
    st.markdown(
        '<span class="feature-badge">🎥 Video Analysis</span>', unsafe_allow_html=True
    )
with col3:
    st.markdown(
        '<span class="feature-badge">⚡ Real-time Results</span>',
        unsafe_allow_html=True,
    )
st.markdown("<hr>", unsafe_allow_html=True)


# =====================
# 3️⃣ Load Predictor
# =====================
@st.cache_resource
def get_predictor():
    with st.spinner("🔄 Loading AI models..."):
        return DeepfakePredictor()


predictor = get_predictor()

# =====================
# 4️⃣ Upload Section
# =====================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📤 Upload Your Media")
st.markdown("Supported formats: JPG, PNG (images) | MP4 (videos)")

uploaded_file = st.file_uploader(
    "Drag and drop or click to browse",
    type=["jpg", "png", "mp4"],
    accept_multiple_files=False,
    label_visibility="collapsed",
)
st.markdown("</div>", unsafe_allow_html=True)

# =====================
# 5️⃣ Analysis Section
# =====================
if uploaded_file:
    file_type = uploaded_file.type
    st.markdown('<div class="card">', unsafe_allow_html=True)

    if "image" in file_type:
        st.markdown("### 🖼️ Image Preview")
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, use_container_width=True)

    elif "video" in file_type:
        st.markdown("### 🎥 Video Preview")
        st.video(uploaded_file)

    if st.button("🔍 Analyze Media"):
        with st.spinner("🧠 AI is analyzing your media..."):
            if "image" in file_type:
                results = predictor.analyze_image(image)
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.success("✅ Analysis Complete!")
                st.markdown("### 📊 Detection Results")
                for res in results:
                    st.markdown(
                        f"**{res['emoji']} {res['label']}** — Confidence: {res['score'] * 100:.2f}%"
                    )
                    st.progress(res["score"])
                st.markdown("</div>", unsafe_allow_html=True)

            elif "video" in file_type:
                result = predictor.analyze_video(uploaded_file)
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.success("✅ Analysis Complete!")
                st.markdown("### 📊 Detection Results")
                st.write(result)
                st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.info("👆 Upload an image or video to get started")
    st.markdown("""
    **How it works:**
    1. Upload your media file (image or video)
    2. Click the analyze button
    3. Get instant AI-powered detection results
    """)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    '<p style="text-align: center; color: #7d7d9e; font-size: 0.9rem;">Powered by Advanced AI | Deepfake Detection Technology</p>',
    unsafe_allow_html=True,
)
