# Adobe India Hackathon 2025 – Round 1A

## Challenge: Connecting the Dots

### Objective
Extract the Title, H1, H2, and H3 headings from a PDF (≤ 50 pages) and output a JSON file representing the heading hierarchy.

### Constraints
- Use only CPU, no internet access during execution.
- Runtime ≤ 10 seconds per PDF.
- Model size ≤ 200MB.
- Use relative font size/style for heading detection (not hardcoded values).
- Generalize for any document, avoid document-specific logic.
- Input/output via `/input` and `/output` folders.

### Tech Stack
- Python 3.10+
- PyMuPDF (fitz) for PDF parsing
- JSON for output
- Docker (for offline, reproducible execution)

### Usage
1. Place PDF files in the `input/` directory.
2. Run the extraction script (see below).
3. Find the results in the `output/` directory as JSON files.

### Project Structure
```
📁 adobe-hackathon
├── 📁 input
├── 📁 output
├── 📁 src
│   ├── extract_outline.py
│   └── utils.py
├── Dockerfile
├── README.md
```

### How to Run (Locally)
```bash
python src/extract_outline.py --input_dir input --output_dir output
```

### How to Build & Run with Docker
```bash
docker build -t adobe-hackathon .
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output adobe-hackathon
``` 