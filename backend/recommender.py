import os
import fitz  # PyMuPDF
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# 1. Load and extract text from resume PDF
def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

# 2. Set up LLM + Chain
llm = AzureChatOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
)

prompt = PromptTemplate(
    input_variables=["resume", "goal"],
    template="""
    Based on the resume below and the user's career goal, suggest 3 ideal job roles in AI/ML they should consider:

    Resume:
    {resume}

    Career Goal:
    {goal}

    Respond with a clear bullet list.
    """
)

chain = prompt | llm | StrOutputParser()

# 3. Call this to get job recommendations
def recommend_roles(resume_text, goal):
    return chain.invoke({"resume": resume_text, "goal": goal})
