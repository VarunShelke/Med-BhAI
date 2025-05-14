import streamlit as st
from PIL import Image
import pytesseract
from bedrock_utility import summarize_with_bedrock

#pytesseract.pytesseract.tesseract_cmd = r"D:\Software Installations\Tesseract-OCR\tesseract.exe"

st.set_page_config(page_title="Med-BhAI – Clinical Note Summarizer", layout="centered")
st.title("🧠 Med-BhAI")
st.markdown("Your AI buddy for simplifying clinical notes.")

note_input = st.text_area("Paste your clinical note here:", height=250)

st.markdown("#### 📸 Or upload an image of the note:")
uploaded_file = st.file_uploader("Upload an image (JPG, PNG)", type=["png", "jpg", "jpeg"])

extracted_text = ""

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Note", use_container_width=True)

    with st.spinner("🧠 Reading the image..."):
        extracted_text = pytesseract.image_to_string(image)

    st.success("✅ Text extracted from image:")
    st.text_area("Extracted Text", extracted_text, height=200)

# Tone style selector
st.markdown("#### 🎨 Select Tone Style:")
tone_styles = {
    "Question-and-Answer Format": "qna_style",
    "Summarize in Bullet Points": "structured_style",
    "Friendly": "friendly",
    "Simplified Explanation": "layman",
}

selected_tone = st.selectbox("Choose the style for the summary:", list(tone_styles.keys()))

if st.button("Summarize"):
    final_input = extracted_text if extracted_text else note_input

    if not final_input.strip():
        st.warning("Please enter or upload a clinical note.")
    else:
        with st.spinner("🧠 Summarizing using Bedrock..."):
            try:
                # Pass the selected tone's backend key
                summary = summarize_with_bedrock(final_input, tone_styles[selected_tone])
                st.markdown("### 🩺 Simplified Summary")
                st.success(summary)
            except Exception as e:
                st.error(f"Bedrock API call failed: {e}")

st.markdown("---")

st.markdown(
    """
    <div style="text-align: center; margin-top: 20px;">
        <img src="https://d0.awsstatic.com/logos/powered-by-aws-white.png" alt="Powered by AWS Cloud Computing">
    </div>
    """,
    unsafe_allow_html=True,
)
