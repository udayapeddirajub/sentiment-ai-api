# 🧠 AI-Powered Sentiment Analysis Microservice

An end-to-end NLP application that translates text into emotional data points. Built with **Flask**, **TextBlob**, and a clean **REST API** architecture.

---

## 🎯 Overview

This tool automates the process of sentiment extraction for large datasets of customer feedback or social media mentions:

1. **Emotion Categorization:** Labels text as Positive, Negative, or Neutral.
2. **Polarity Scoring:** Quantifies sentiment on a scale from -1.0 to +1.0.
3. **API Integration:** Headless architecture ready for integration with external web or mobile applications.

---

## 🏗️ Technical Stack

* **Backend:** Python 3.13 / Flask
* **NLP Logic:** TextBlob (NLTK-based)
* **Frontend:** HTML5 / CSS3 / Vanilla JS (Fetch API)
* **CI/CD:** GitHub Actions (Flake8 linting & dependency validation)

---

## 🚀 Installation & Usage

### 1. Prerequisites

```bash
python --version  # Ensure Python 3.x is installed

```

### 2. Setup

```bash
git clone https://github.com/your-repo/sentiment-ai
cd sentiment-ai
pip install -r requirements.txt

```

### 3. Execution

```bash
python app.py

```

Visit `http://127.0.0.1:5000` in your browser.

---

## 🔌 API Documentation

External applications can consume the prediction engine via JSON requests.

**Endpoint:** `POST /predict`

**Header:** `Content-Type: application/json`

**Request:**

```json
{
  "text": "The platform is incredibly intuitive and fast."
}

```

**Response:**

```json
{
  "sentiment": "Positive",
  "score": 0.7,
  "status": "success"
}

```

---

## 🛠️ CI/CD Pipeline

The repository uses GitHub Actions for automated quality control:

* **Linting:** Checks for PEP8 compliance via Flake8.
* **Build Check:** Verifies that all dependencies in `requirements.txt` install correctly in an Ubuntu environment.

---

## 📂 Structure

```text
├── .github/workflows/ci.yml  # Pipeline config
├── templates/index.html      # UI components
├── app.py                    # Server & NLP logic
├── requirements.txt          # Dependencies
└── .gitignore                # Environment exclusions

```