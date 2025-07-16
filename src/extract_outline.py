import os
import sys
import json
import argparse
import fitz  # PyMuPDF
from collections import defaultdict

print("[DEBUG] Script started.")

LEVELS = ['title', 'h1', 'h2', 'h3']
H3_KEYWORDS = [
    'note', 'key points', 'key takeaway', 'takeaway', 'summary', 'important', 'tip', 'reminder', 'caution', 'warning'
]

def is_h3_keyword(text):
    t = text.lower().strip(':').strip()
    return any(t.startswith(kw) for kw in H3_KEYWORDS)


def extract_headings(pdf_path):
    print(f"Opening PDF: {pdf_path}")
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error opening PDF: {e}")
        return {"title": None, "outline": []}
    font_sizes = defaultdict(int)
    blocks = []

    # Pass 1: Collect all text blocks and font sizes
    for page_num, page in enumerate(doc):
        for block in page.get_text("dict")['blocks']:
            if block['type'] == 0:  # text block
                for line in block['lines']:
                    for span in line['spans']:
                        text = span['text'].strip()
                        if not text:
                            continue
                        size = span['size']
                        font_sizes[size] += 1
                        blocks.append({
                            'text': text,
                            'size': size,
                            'font': span['font'],
                            'flags': span['flags'],
                            'page': page_num + 1,  # 1-indexed page
                            'bbox': span['bbox']
                        })

    print(f"Font sizes found: {dict(font_sizes)}")
    if not font_sizes:
        print("No font sizes found. Returning empty outline.")
        return {"title": None, "outline": []}

    # Heuristic: Largest font = title, next 3 = h1, h2, h3
    sorted_sizes = sorted(font_sizes.keys(), reverse=True)
    print(f"Sorted font sizes: {sorted_sizes}")
    size_to_level = {}
    if len(sorted_sizes) >= 4:
        size_to_level[sorted_sizes[0]] = 'title'
        size_to_level[sorted_sizes[1]] = 'h1'
        size_to_level[sorted_sizes[2]] = 'h2'
        size_to_level[sorted_sizes[3]] = 'h3'
    else:
        for i, sz in enumerate(sorted_sizes):
            size_to_level[sz] = LEVELS[i]
    print(f"Size to level mapping: {size_to_level}")

    # Pass 2: Assign heading levels
    title = None
    outline = []
    h2_size = None
    for sz, lvl in size_to_level.items():
        if lvl == 'h2':
            h2_size = sz
            break

    for block in blocks:
        level = size_to_level.get(block['size'])
        if not level:
            continue
        # Heuristic: If h2 size but matches h3 keyword, treat as h3
        if level == 'h2' and h2_size and is_h3_keyword(block['text']):
            level = 'h3'
        if level == 'title' and not title:
            title = block['text']
        elif level in ['h1', 'h2', 'h3']:
            outline.append({
                'level': level,
                'text': block['text'],
                'page': block['page']
            })

    print(f"Title: {title}")
    print(f"Outline: {outline}")
    return {"title": title, "outline": outline}


def process_pdfs(input_dir, output_dir):
    print(f"Processing PDFs in {input_dir}")
    for fname in os.listdir(input_dir):
        print(f"[DEBUG] Found file: {fname}")
        if not fname.lower().endswith('.pdf'):
            print(f"Skipping non-PDF file: {fname}")
            continue
        print(f"[DEBUG] Processing file: {fname}")
        pdf_path = os.path.join(input_dir, fname)
        result = extract_headings(pdf_path)
        out_name = os.path.splitext(fname)[0] + '.json'
        out_path = os.path.join(output_dir, out_name)
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"Processed {fname} -> {out_name}")


def main():
    parser = argparse.ArgumentParser(description="Extract Title, H1, H2, H3 from PDFs.")
    parser.add_argument('--input_dir', type=str, default='input', help='Input directory with PDFs')
    parser.add_argument('--output_dir', type=str, default='output', help='Output directory for JSONs')
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    process_pdfs(args.input_dir, args.output_dir)

if __name__ == '__main__':
    main() 