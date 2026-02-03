📘 Legal GenAI Assistant (RAG)

A lightweight Legal GenAI Assistant that answers article-based questions from the Constitution of India using a PDF-based Retrieval Augmented Generation (RAG) approach.

This system provides short, accurate, and educational explanations without using heavy language models.

🎯 Project Objective

To build an offline, fast, and safe legal assistant that:

Reads data only from the Constitution PDF

Answers specific Article-based questions

Produces short and clear explanations

Avoids hallucination and long text dumping

Is suitable for college projects and demonstrations

🧠 Key Features

📘 PDF-based (Constitution of India)

⚡ Fast & lightweight (no heavy LLMs)

🧠 Controlled generative explanations

🔁 Slightly different wording for the same question

📴 Works offline

❌ No full Constitution summaries

🎓 Educational purpose only

🏗️ Project Architecture
Legal-GenAI-Assistant/
│
├── app.py              # Streamlit frontend
├── chatbot.py          # Answer formatting & generative explanations
├── rag_engine.py       # PDF reading & article extraction
├── requirements.txt    # Dependencies
└── data/
    └── constitution.pdf

🔄 How It Works (RAG Flow)
User Question
     ↓
Article Number Detection
     ↓
PDF Article Extraction
     ↓
Short Official Text Selection
     ↓
Controlled Generative Explanation
     ↓
Final Answer (No Hallucination)

💡 Example Questions
What is Article 21?
Explain Article 19.
What does Article 14 guarantee?
Article 21 in simple words.


❌ Not Supported:

Explain the whole Constitution
Give me all Fundamental Rights
Summarize the Constitution

🚀 Deployment

This project is deployed using Streamlit Cloud and GitHub.

Steps:

Upload project to GitHub

Connect GitHub repo to Streamlit Cloud

Set app.py as the main file

Deploy 🚀

🛠️ Installation (Local)
pip install -r requirements.txt
streamlit run app.py

⚠️ Disclaimer

⚠️ This application is for educational purposes only.
It does not provide legal advice.

👨‍🎓 Author

Shubham Dangade
College Project – Legal GenAI Assistant using RAG

📜 License

This project is intended for academic and educational use only.
