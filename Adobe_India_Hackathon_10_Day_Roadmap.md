# Adobe India Hackathon – 10-Day Roadmap with Tech Stack

This document outlines a complete 10-day development roadmap along with the required tech stack for the Adobe India Hackathon 2025 – 'Connecting the Dots' Challenge.

---

## 📌 Project Goal Summary

| Round | Objective                                                      | Output                        |
|-------|---------------------------------------------------------------|-------------------------------|
| 1A    | Extract Title + H1, H2, H3 from PDFs (≤ 50 pages)             | `output.json` with heading hierarchy |
| 1B    | Extract relevant sections/subsections based on persona/job     | Ranked JSON output            |

---

## 🧰 Tech Stack Overview

| Layer            | Tools / Libraries                                 | Purpose                        |
|------------------|---------------------------------------------------|--------------------------------|
| PDF Parsing      | PyMuPDF (fitz), pdfplumber, pdfminer.six          | Text + layout extraction       |
| Heading Detection| PyMuPDF + heuristics                              | Identify title/headings        |
| ML/NLP (optional)| sentence-transformers, scikit-learn, nltk/spacy   | Embeddings, similarity, text processing |
| Ranking          | Cosine similarity, keyword matching               | Score relevance                |
| Containerization | Docker                                            | Offline execution              |
| Language         | Python 3.10+                                      | Primary programming language   |
| Storage          | JSON                                              | Input/output format            |
| Execution        | CPU only, no internet                             | Offline resource compliance    |

---

## 🗓️ 10-Day Development Plan

| Day    | Tasks                                                                 |
|--------|-----------------------------------------------------------------------|
| Day 1  | Set up project structure; install PyMuPDF/pdfminer; test basic PDF read |
| Day 2  | Extract title and heading candidates using font/style/position        |
| Day 3  | Structure headings into JSON format (H1, H2, H3)                     |
| Day 4  | Test edge cases with messy PDFs; add fallback logic                  |
| Day 5  | Finalize Round 1A; write Dockerfile; test `/input → /output`         |
| Day 6  | Start Round 1B; read + merge multi-PDF content                       |
| Day 7  | Use MiniLM or rule-based methods to match persona+job                |
| Day 8  | Rank sections/subsections and create relevance logic                 |
| Day 9  | Finalize Docker for Round 1B; simulate full test                     |
| Day 10 | Write README, approach doc, final testing                            |

---

## ✅ Best Practices & Constraints

- Use relative font size difference, not absolute, for heading detection.
- Avoid hardcoded logic; generalize for any document.
- Use sentence-transformers like `all-MiniLM-L6-v2` (80MB) for relevance ranking.
- Keep Docker images minimal (python:3.10-slim).
- Ensure offline execution; no internet/API calls allowed.
- Round 1A: ≤ 10 sec runtime; Round 1B: ≤ 60 sec runtime.
- Round 1A model ≤ 200MB; Round 1B model ≤ 1GB.

---

## 📁 Suggested Project Structure

```
📁 adobe-hackathon
├── 📁 input
├── 📁 output
├── 📁 src
│   ├── extract_outline.py
│   ├── persona_analysis.py
│   └── utils.py
├── Dockerfile
├── README.md
├── approach_explanation.md
``` 