# 🤖 AI Job Recommender App

This Streamlit app allows users to upload their resume (PDF) and receive AI-powered job role recommendations based on their career goals. It uses Azure OpenAI's GPT model to analyze the resume text and recommend roles aligned with the candidate's aspirations.

---

## 🚀 Features

- 📄 Upload your resume (PDF format)
- 🎯 Specify your target career goal (e.g., "Computer Vision Engineer")
- 🧠 Get intelligent job role recommendations
- 💬 Built with Streamlit for an intuitive interface
- 🔒 Secure via environment variables using `.env`

---

## 🛠️ Tech Stack

- **Streamlit** – Frontend UI
- **Langchain** – LLM abstraction
- **Azure OpenAI API** – GPT model
- **PyMuPDF (fitz)** – PDF parsing
- **Python-dotenv** – Environment variable handling

---

## 🧾 How It Works

1. Upload a PDF resume.
2. Provide your desired job direction.
3. App extracts the resume text.
4. GPT-4 processes it with a custom prompt.
5. You receive 3 tailored job suggestions.

---

## 🖥️ Local Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-job-recommender.git
cd ai-job-recommender

2️⃣ **Set Up Environment Variables**  
Create a `.env` file in the root directory and include:

```env
AZURE_OPENAI_API_KEY=your_azure_key  
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/  
AZURE_OPENAI_DEPLOYMENT=your-deployment-name  
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

3️⃣ **Install Requirements**

```bash
pip install -r requirements.txt
```

4️⃣ **Run the App**

```bash
streamlit run app/streamlit-app.py
```

📂 **Project Structure**

```bash
ai-job-recommender/
│
├── app/
│   └── streamlit-app.py         # Streamlit frontend logic
│
├── backend/
│   └── recommender.py           # Resume parser + job recommender logic
│
├── data/
│   └── sample_resume.pdf        # (Optional) Demo resume for testing
│
├── .env                         # Your secret API keys
├── requirements.txt
└── README.md
```

✅ **Requirements**  
Save the following in a `requirements.txt` file:

```text
streamlit  
python-dotenv  
PyMuPDF  
langchain  
langchain-openai
```

## 👨‍💻 About Me

**Ghulam Hussain Khuhro**  
AI/ML Engineer · Data Scientist · Google-Certified Data Analyst  
📬 ghulamhussain.developer@gmail.com  
🌐 [LinkedIn](https://www.linkedin.com/in/ghulamhussainkhuhro/) • [GitHub](https://github.com/ghulamhussainkhuhro/) • [Portfolio](https://ghulamhussainkhuhro.github.io/)

---

If this project interests you or you'd like to collaborate, feel free to connect. Feedback and contributions are always welcome!

📌 **Disclaimer**  
This app is for educational and demonstration purposes. For production usage, ensure data security, model robustness, and deployment best practices.
