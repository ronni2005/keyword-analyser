# 📄 Resume Keyword Analyzer

A Python-based application that analyzes how well a resume matches a job description using Natural Language Processing (NLP). The project calculates similarity scores, extracts technical skills, identifies missing skills, and presents the results through a Streamlit web application.

---

## Features

- 📄 Supports Resume and Job Description in:
  - PDF
  - DOCX
  - TXT

- 🧹 Text preprocessing
  - Lowercasing
  - Punctuation removal
  - Stopword removal
  - Lemmatization

- 📊 Resume similarity using TF-IDF and Cosine Similarity

- 🔍 Skill extraction using a predefined skill database

- 🔤 N-gram based phrase matching
  - Unigrams
  - Bigrams
  - Trigrams

- 📈 Weighted Resume Score combining:
  - Resume similarity
  - Skill match score

- 🌐 Interactive Streamlit web interface

---

## Tech Stack

- Python
- Streamlit
- Scikit-learn
- NLTK
- pypdf
- python-docx

---

## Project Structure

```
resume-keyword-analyzer/
│
├── app.py                 # Streamlit application
├── main.py                # CLI version
│
├── data/
│   ├── resume.txt
│   ├── job_description.txt
│   └── skills.txt
│
├── src/
│   ├── parser.py
│   ├── preprocess.py
│   ├── similarity.py
│   ├── skills.py
│   ├── scoring.py
│   └── utils.py
│
├── requirements.txt
└── README.md
```

---

## How It Works

1. Upload a resume and a job description.
2. Documents are parsed and preprocessed.
3. Skills are extracted using a predefined skill database.
4. TF-IDF and Cosine Similarity calculate textual similarity.
5. Skill Match Score is calculated based on matched skills.
6. A weighted Final Resume Score is generated.
7. The application displays-:
   - Similarity Score
   - Skill Match Score
   - Final Resume Score
   - Matched Skills
   - Missing Skills

---

## Example Output

```
Similarity Score : 67.42%

Skill Match Score : 80.00%

Final Resume Score : 71.19%

Matched Skills
• Python
• SQL
• AWS
• NumPy

Missing Skills
• Azure
• Machine Learning
```

---

## Future Enhancements (Version 2)

- Semantic similarity using Sentence-BERT / Transformers
- Skill synonym mapping (e.g., ML → Machine Learning)
- Resume keyword highlighting
- Export analysis as a PDF report
- Deploy the application online

---

## Learning Outcomes

This project helped me gain hands-on experience with:

- Natural Language Processing fundamentals
- TF-IDF Vectorization
- Cosine Similarity
- Text preprocessing
- N-gram generation
- Feature engineering
- Modular Python project structure
- Streamlit application development

---

