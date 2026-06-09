# 🤖 Auto Tagging Support Tickets Using LLM

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![LLM](https://img.shields.io/badge/LLM-OpenAI%2FGPT-orange?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-green?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge\&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

> An AI-powered system that automatically assigns **relevant tags to customer support tickets** using Large Language Models (LLMs) like GPT. This improves ticket routing, prioritization, and response efficiency.

---

# 📌 Table of Contents

* [Overview](#overview)
* [Problem Statement](#problem-statement)
* [Solution Approach](#solution-approach)
* [Dataset](#dataset)
* [System Architecture](#system-architecture)
* [Tech Stack](#tech-stack)
* [Workflow](#workflow)
* [Installation](#installation)
* [Usage](#usage)
* [Example Output](#example-output)
* [Future Improvements](#future-improvements)
* [License](#license)

---

# 📖 Overview

Customer support teams handle thousands of tickets daily. Manually tagging them is:

* Time-consuming
* Error-prone
* Not scalable

This project uses **LLMs (Large Language Models)** to automatically classify and assign tags such as:

* Billing Issue
* Technical Error
* Account Access
* Feature Request
* Bug Report

---

# ❗ Problem Statement

Support tickets often arrive without structure. Without proper tagging:

* Tickets are routed incorrectly
* Response time increases
* Customer satisfaction decreases

---

# 💡 Solution Approach

We use an LLM-based pipeline that:

1. Reads the support ticket text
2. Understands the intent using semantic reasoning
3. Predicts one or more relevant tags
4. Returns structured output

---

# 📂 Dataset

Sample support ticket format:

```text id="q9k2lm"
"I am unable to reset my password. The reset link is not working."
```

Expected output:

```text id="x8n1pl"
Tags: Account Access, Technical Issue
```

You can use:

* Internal company tickets
* Synthetic datasets
* Kaggle support ticket datasets

---

# 🧠 System Architecture

```text id="g3k9aa"
User Input (Support Ticket)
        │
        ▼
Preprocessing (optional cleaning)
        │
        ▼
LLM (GPT / LLaMA / Claude)
        │
        ▼
Prompt Engineering Layer
        │
        ▼
Structured Tag Output
```

---

# 🛠 Tech Stack

* Python
* OpenAI GPT / Claude / LLaMA
* LangChain
* Streamlit (UI)
* Pandas
* Prompt Engineering

---

# 🔄 Workflow

### Step 1: Input Ticket

User enters support query.

### Step 2: Prompt Construction

```text id="t4p1ld"
Classify the following support ticket into relevant tags:
```

### Step 3: LLM Processing

Model understands context and intent.

### Step 4: Output Generation

Returns structured tags.

---

# ⚙️ Installation

Clone the repository:

```bash id="k9x2qp"
git clone <your-repo-url>
cd Auto-Tagging-Support-Tickets
```

Install dependencies:

```bash id="w1x7hh"
pip install -r requirements.txt
```

---

# ▶️ Usage

Run Streamlit app:

```bash id="s2p9oo"
streamlit run app.py
```

---

# 💻 Example

### Input:

```text id="m8v2qk"
"My payment failed but money is deducted from my account"
```

### Output:

```text id="z7n1pp"
Tags:
- Billing Issue
- Payment Failure
```

---

# 🌐 Example Prompt Used

```text id="p3k8ll"
You are an AI assistant that classifies support tickets.

Return only tags from this list:
[Billing, Technical, Account, Bug, Feature Request]

Ticket:
{ticket_text}
```

---

# 🚀 Future Improvements

* Multi-label classification fine-tuning
* Fine-tuned open-source LLM (LLaMA 3 / Mistral)
* Integration with Zendesk / Freshdesk
* Real-time API deployment (FastAPI)
* Dashboard analytics for ticket trends

---

# 📊 Benefits

* Faster ticket routing
* Reduced manual workload
* Improved customer satisfaction
* Scalable support system

---

# 📜 License

MIT License

---

# 👨‍💻 Author

**Your Name**

AI / LLM Engineer

If you like this project, ⭐ the repo and contribute improvements!

