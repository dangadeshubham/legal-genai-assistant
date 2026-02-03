import streamlit as st
import re
from chatbot import format_answer

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Legal GenAI Assistant",
    page_icon="⚖️",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "history" not in st.session_state:
    st.session_state.history = []

if "query" not in st.session_state:
    st.session_state.query = ""

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("ℹ️ About This App")
    st.markdown(
        """
        **Legal GenAI Assistant** explains the  
        **Constitution of India** article by article.

        ✅ PDF-based  
        ✅ Offline  
        ✅ Short & accurate answers  
        ❌ No full Constitution summaries  

        **Example questions:**
        - What is Article 21?
        - Explain Article 19
        """
    )

    st.divider()
    st.markdown("### 📌 Quick Articles")

    if st.button("Article 14"):
        st.session_state.query = "What is Article 14?"
    if st.button("Article 19"):
        st.session_state.query = "What is Article 19?"
    if st.button("Article 21"):
        st.session_state.query = "What is Article 21?"

# ---------------- HEADER ----------------
st.title("⚖️ Legal GenAI Assistant")
st.caption("📘 Constitution of India | PDF-based | Offline | Educational")

st.markdown(
    "Ask questions **only about specific Articles** (e.g., Article 14, 19, 21)."
)

st.divider()

# ---------------- INPUT + SEND BUTTON ----------------
with st.form(key="query_form"):
    query = st.text_input(
        "Ask an Article-based question:",
        placeholder="e.g. Explain Article 21 in simple words"
    )
    send_clicked = st.form_submit_button("Send 🚀")

# ---------------- PROCESS QUERY ----------------
if send_clicked and query:
    st.session_state.query = query  # persist input

    match = re.search(r"Article\s+(\d+[A-Z]?)", query, re.IGNORECASE)

    if not match:
        st.info(
            "ℹ️ **Fundamental Rights** are mainly covered under **Articles 12–35**.\n\n"
            "Please ask about a **specific Article**, such as:\n"
            "- **Article 14** – Equality\n"
            "- **Article 19** – Freedoms\n"
            "- **Article 21** – Life & Liberty"
        )
    else:
        article_number = match.group(1)
        response = format_answer(article_number)

        # Save history
        if article_number not in st.session_state.history:
            st.session_state.history.insert(0, article_number)
            st.session_state.history = st.session_state.history[:5]

        st.success("✅ Article found and explained below")
        st.divider()
        st.markdown(response)

# ---------------- HISTORY ----------------
if st.session_state.history:
    st.divider()
    st.markdown("### 🕘 Recently Viewed Articles")
    st.write(", ".join([f"Article {a}" for a in st.session_state.history]))

# ---------------- FOOTER ----------------
st.divider()
st.caption("⚠️ Educational purpose only | Not legal advice")
