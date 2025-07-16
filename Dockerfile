# Minimal Dockerfile for Adobe Hackathon Round 1A
FROM python:3.10-slim

WORKDIR /app

COPY src/ src/
COPY input/ input/
COPY output/ output/
COPY README.md ./

RUN pip install --no-cache-dir pymupdf

CMD ["python", "src/extract_outline.py", "--input_dir", "input", "--output_dir", "output"] 