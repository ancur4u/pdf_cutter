import streamlit as st
from PyPDF2 import PdfReader
from app.pdf_utils import extract_pages, parse_ranges

def main():
    st.set_page_config(page_title="Advanced PDF Cutter", layout="centered")
    st.title("PDF Cutter with Page Range Support")
    st.markdown("Upload a PDF and input one or more page ranges (e.g., 1-2, 5-6, 10-12) to extract and preview.")

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file:
        pdf_reader = PdfReader(uploaded_file)
        total_pages = len(pdf_reader.pages)
        st.success(f"Uploaded PDF with {total_pages} pages.")

        page_ranges_input = st.text_input("Enter page ranges (e.g. 1-2, 5-6, 10-12):", "1-2")
        ranges = parse_ranges(page_ranges_input)

        if not ranges:
            st.error("Please enter valid page ranges like 1-2, 4-5")
            return

        if st.button("Extract Pages"):
            output_pdf, preview_texts = extract_pages(uploaded_file, ranges)
            st.success("Pages extracted successfully.")

            with st.expander("Preview Extracted Text"):
                for text in preview_texts:
                    st.markdown(text)

            st.download_button(
                label="Download Extracted PDF",
                data=output_pdf,
                file_name="extracted_pages.pdf",
                mime="application/pdf"
            )
