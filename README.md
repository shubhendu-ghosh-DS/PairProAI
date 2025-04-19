# PairProAI - FastAPI Backend

**PairProAI** is a production-ready FastAPI backend designed to assist developers with intelligent code enhancement features. It exposes a clean and efficient RESTful API for AI-powered code analysis and generation. This backend is currently deployed on Hugging Face Spaces using Docker.

## 🔍 Overview

PairProAI leverages Google’s Gemini (via the `google-generativeai` package) to provide advanced code-related utilities such as:

- ✅ Code Translation
- 🛠️ Code Debugging
- ⚙️ Code Optimization
- 🧹 Code Simplification
- 🧪 Test Case Generation
- 🚀 Efficiency Improvements

This backend receives code snippets and developer intents via HTTP requests and returns enhanced code with human-readable explanations.

---

## Live demo
[This](https://shubhendu-ghosh-pairproai.hf.space) is where the APIs are live!

---

## 📁 Project Structure

```
app/
├── main.py
├── routes.py        # API routes (FastAPI endpoints)
├── services.py      # Core logic for interacting with Gemini model
├── utils.py         # Prompt formatting and response parsing helpers
.env                 # Environment variables (API keys)
Dockerfile           # Docker setup for deployment
requirements.txt     # Python dependencies
```

---

## 🚀 API Endpoint

### `POST /generate`

**Request Body:**

```json
{
  "code": "print('Hello, World!')",
  "option": "Code Translation",
  "target_language": "Java",
  "error_message": null
}
```

**Options Available:**
- `"Code Translation"` (requires `target_language`)
- `"Debug Your Code"` (requires `error_message`)
- `"Code Improvements"`
- `"Simplify Code"`
- `"Write Test Cases"`
- `"Improve Efficiency"`

**Response:**

```json
{
  "code": "// Translated Java code here",
  "explanation": "## Translation Details\n- Explanation in markdown..."
}
```

---

## ⚙️ Setup & Deployment

### Prerequisites

- Python 3.10+
- Google Generative AI API key
- Docker (for containerized deployment)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://huggingface.co/spaces/shubhendu-ghosh/PairProAI
   cd PairProAI
   ```

2. **Create a `.env` File**
   ```env
   API_KEY=your_google_genai_api_key
   ```

3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**
   ```bash
   uvicorn app.main:app --reload
   ```

### Docker Deployment

1. **Build Docker Image**
   ```bash
   docker build -t pairproai .
   ```

2. **Run the Container**
   ```bash
   docker run -d -p 7860:7860 --env-file .env pairproai
   ```

---

## 🤖 Technology Stack

- **FastAPI** – High-performance web framework for APIs
- **Google Generative AI (Gemini)** – Natural language generation
- **Docker** – Containerized deployment
- **Hugging Face Spaces** – Hosting platform

---

## 💡 Use Cases

- Enhance developer productivity through intelligent suggestions
- Integrate with IDEs or browser extensions for real-time help
- Build educational tools for programming students
- Debug and understand complex codebases with ease

---

## 📫 Contact

**Author:** Shubhendu Ghosh  
**Role:** AI/ML Engineer  
**LinkedIn:** [https://linkedin.com/in/shubhendu-ghosh](https://linkedin.com/in/shubhendu-ghosh)  
**Portfolio:** [https://shubhenduportfolio.github.io/](https://shubhenduportfolio.github.io/)

---

## 📜 License

This project is for demonstration and educational purposes. For commercial use, please contact the author.
