import streamlit as st
import pdfplumber
import requests

# ---- Extract text from PDF ----
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for i, page in enumerate(pdf.pages[:10]):  # limit to 10 pages
            page_text = page.extract_text()
            if page_text:
                text += f"\n--- Page {i+1} ---\n{page_text}"
    return text


# ---- Call Ollama (Mistral) ----
def analyze_sow(text):
    prompt = f"""
You are an expert SOW (Statement of Work) auditor.

Analyze the document and FLAG issues under these categories:
- Logical inconsistency
- Missing information
- Incorrect values (dates, pricing, resource mismatch)
- Contract risks

Return output strictly in this format:

Issue:
Severity (High/Medium/Low):
Page:
Explanation:

Document:
{text[:8000]}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


# ---- Streamlit UI ----
st.title("📄 SOW Analyzer (Open Source MVP)")

uploaded_file = st.file_uploader("Upload SOW PDF", type=["pdf"])

if uploaded_file:
    st.info("Extracting text...")
    text = extract_text(uploaded_file)

    st.success("Text extracted successfully ✅")

    if st.button("Analyze SOW"):
        with st.spinner("Analyzing..."):
            result = analyze_sow(text)

        st.subheader("🚩 Flagged Issues")
        st.write(result)