# AI Resume Skill Analyzer

A Streamlit web app that scans an uploaded resume (PDF) and checks it against a set of technical skills to give a skill-match score, along with suggestions on what to learn next.

## How it works
1. User uploads their resume as a PDF through the Streamlit interface.
2. The app extracts all text from the PDF using PyPDF2.
3. It checks the extracted text against a predefined list of technical skills (e.g., Python, Java, C++, HTML, CSS, JavaScript, Verilog, VHDL, VLSI).
4. It displays:
   - **Detected Skills** — skills found in the resume
   - **Missing Skills** — skills not found in the resume
   - **Resume Score** — percentage match against the skill list
   - **Suggested Learning Areas** — top missing skills worth learning next

## Tech Stack
- Python
- Streamlit (for the web interface)
- PyPDF2 (for PDF text extraction)

## Skills Applied
- Python programming
- Working with external libraries (Streamlit, PyPDF2)
- Text extraction and keyword matching
- Building a simple, functional web app UI

## What I Learned
This project helped me understand how to build an interactive web app using Streamlit, extract and process text from PDF files, and design simple logic to compare resume content against a target skill set — giving me a practical introduction to text-based analysis tools.

## Future Improvements
- Expand the skill list to cover more domains
- Support additional file formats (DOCX)
- Improve skill matching using NLP techniques instead of exact keyword matching
