# AI Customer Support Chatbot using Llama 3.2

An AI-powered customer support chatbot built using **Streamlit** and **Llama 3.2 Large Language Model**.

The chatbot uses a locally deployed Large Language Model through **Ollama** to generate intelligent responses while keeping user data private by running the model locally.

---

## Features

✨ Natural language conversations  
✨ Local LLM inference using Llama 3.2  
✨ Interactive Streamlit-based chatbot UI  
✨ Fast AI-generated responses  
✨ Privacy-focused AI assistant  
✨ Runs completely on local machine  

---

## Tech Stack

- Python
- Streamlit
- Ollama
- Llama 3.2
- Large Language Models (LLMs)
- Generative AI
- Prompt Engineering

---

## Architecture

```text
User
  │
  ▼
Streamlit UI
  │
  ▼
Python Backend
  │
  ▼
Ollama API
  │
  ▼
Llama 3.2
  │
  ▼
Generated Response
```
---

## Project Structure

```text
AI-Customer-Support-Chatbot
│
├── app.py
├── chatbot.py
├── requirements.txt
├── README.md
├── .gitignore
├── screenshots
│   └── chatbot-ui.png
└── docs
```


---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Pradnyachavan1/AI-Customer-Support-Chatbot.git
```

### 2. Navigate to the project

```bash
cd AI-Customer-Support-Chatbot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

---

## Application Preview

![AI Customer Support Chatbot](screenshots/chatbot-ui.png)

---

## Future Improvements

- Add conversation memory
- Implement Retrieval-Augmented Generation (RAG)
- Support PDF knowledge base
- Add chat history export
- Improve UI/UX
- Deploy on Streamlit Cloud or Hugging Face Spaces

---

## Author

**Pradnya Chavan**

GitHub: https://github.com/Pradnyachavan1