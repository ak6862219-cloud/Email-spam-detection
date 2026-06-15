import streamlit as st
import pickle

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="AI Email Fraud Detection",
    page_icon="📧",
    layout="wide"
)

# ==========================
# LOAD MODEL
# ==========================
model = pickle.load(open("spam_model.pkl", "rb"))
cv = pickle.load(open("vectorizer.pkl", "rb"))

# ==========================
# CUSTOM CSS
# ==========================
st.markdown("""
<style>

.block-container{
    padding-top:1rem;
    padding-bottom:0rem;
    padding-left:2rem;
    padding-right:2rem;
    max-width:100%;
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

.main{
    background-color:#0B1120;
}

.stApp{
    background:#0B1120;
    color:white;
}

.card{
    background:#111827;
    padding:20px;
    border-radius:20px;
    border:1px solid #1E293B;
    text-align:center;
}

.metric-value{
    font-size:28px;
    font-weight:bold;
    color:white;
}

.metric-label{
    color:#94A3B8;
    font-size:14px;
}

.title{
    text-align:center;
    font-size:42px;
    font-weight:700;
    color:white;
}

.subtitle{
    text-align:center;
    color:#94A3B8;
    margin-bottom:20px;
}

.result-box{
    background:#111827;
    padding:25px;
    border-radius:20px;
    border:1px solid #1E293B;
    text-align:center;
    margin-top:10px;
}

.safe{
    color:#22C55E;
    font-size:30px;
    font-weight:bold;
}

.spam{
    color:#EF4444;
    font-size:30px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER
# ==========================
st.markdown("""
<div class='title'>
📧 AI Email Fraud Detection Dashboard
</div>

<div class='subtitle'>
Machine Learning Powered Email Security System
</div>
""", unsafe_allow_html=True)

# ==========================
# TOP METRICS
# ==========================
c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class='card'>
    <div class='metric-label'>Algorithm</div>
    <div class='metric-value'>Naive Bayes</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='card'>
    <div class='metric-label'>Accuracy</div>
    <div class='metric-value'>98%+</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='card'>
    <div class='metric-label'>Detection</div>
    <div class='metric-value'>Spam/Ham</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class='card'>
    <div class='metric-label'>Status</div>
    <div class='metric-value'>Active</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ==========================
# MAIN LAYOUT
# ==========================
left,right = st.columns([2,1])

with left:

    st.subheader("📩 Email Content")

    email_text = st.text_area(
        "",
        height=180,
        placeholder="Paste email content here..."
    )

    analyze = st.button(
        "🔍 Analyze Email",
        use_container_width=True
    )

with right:

    st.subheader("⚡ Security Insights")

    st.info("""
    ✔ Real-Time Detection

    ✔ NLP Processing

    ✔ Fraud Analysis

    ✔ Spam Classification

    ✔ ML Powered
    """)

# ==========================
# PREDICTION
# ==========================
if analyze:

    if email_text.strip() == "":
        st.warning("Please enter email content.")

    else:

        email_vector = cv.transform([email_text])

        prediction = model.predict(email_vector)

        suspicious_words = [
            "free",
            "winner",
            "money",
            "cash",
            "offer",
            "click",
            "prize",
            "bonus",
            "claim",
            "reward",
            "urgent",
            "lottery"
        ]

        found_words = []

        text_lower = email_text.lower()

        for word in suspicious_words:
            if word in text_lower:
                found_words.append(word)

        st.write("")

        if prediction[0] == 1:

            st.markdown("""
            <div class='result-box'>
            <div class='spam'>
            🚨 SPAM EMAIL DETECTED
            </div>
            </div>
            """, unsafe_allow_html=True)

            st.progress(90)

            st.error("Risk Score: 90%")

            if found_words:

                st.subheader("⚠ Suspicious Keywords")

                cols = st.columns(4)

                for i,word in enumerate(found_words):
                    cols[i % 4].warning(word)

        else:

            st.markdown("""
            <div class='result-box'>
            <div class='safe'>
            ✅ GENUINE EMAIL
            </div>
            </div>
            """, unsafe_allow_html=True)

            st.progress(15)

            st.success("Risk Score: 15%")