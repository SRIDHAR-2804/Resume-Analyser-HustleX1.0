import streamlit as st 
import PyPDF2
import pdfplumber
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


st.title("TECH PIRATES RESUME ANALYZER")

st.subheader("Revolutionizing Recruitment: The Future of Candidate Evaluation with Our Resume Screener App")

st.caption("Unlock the potential of AI-driven resume screening, revolutionizing how you identify the best-fit candidates effortlessly")

uploadedJD = st.file_uploader("Upload Job Description", type="pdf")

uploadedResume = st.file_uploader("Upload Resume",type="pdf")

ep = st.text_input("Enter the eligiblity percentage ",type="default")

click = st.button("Process")


try:
    global job_description
    with pdfplumber.open(uploadedJD) as pdf:
        pages = pdf.pages[0]
        job_description = pages.extract_text()

except:
    st.write("")
    
    
try:
    global resume
    with  pdfplumber.open(uploadedResume) as pdf:
        pages = pdf.pages[0]
        resume = pages.extract_text()
except:
    st.write("")

try:
    global eligiblity_percentage
    eligiblity_percentage=float(ep)
except:
    st.write("")

    
#logic
def getResult(JD_txt,resume_txt):
    content = [JD_txt,resume_txt]

    cv = CountVectorizer()

    matrix = cv.fit_transform(content)

    similarity_matrix =  cosine_similarity(matrix)

    match = similarity_matrix[0][1] * 100

    return match


#button 

if click:
    match = getResult(job_description,resume)
    match = round(match,2)
    st.write("Match Percentage: ",match,"%")
    if match>=eligiblity_percentage:
        st.success("You are eligible for the position !")
    else:
        st.write("Sorry you are not eligible")
st.caption("~ Made by Tech Pirates")
