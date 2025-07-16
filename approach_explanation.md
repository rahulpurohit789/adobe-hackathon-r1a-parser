# Approach Explanation – Round 1A

## Goal
Extract the Title, H1, H2, and H3 headings from PDFs (≤ 50 pages) and output a JSON file with the heading hierarchy.

## Extraction Logic
- **PDF Parsing:** Use PyMuPDF to extract all text spans, capturing their font size, font name, and position.
- **Heading Detection:**
  - Collect all font sizes used in the document.
  - Assign the largest font size as the Title, and the next three largest as H1, H2, and H3, respectively.
  - This is a relative, document-specific approach, not hardcoded to any absolute size.
- **Hierarchy Construction:**
  - As headings are detected, they are structured into a nested hierarchy: Title > H1 > H2 > H3.
  - Handles missing levels gracefully (e.g., if no H3 is present).

## Constraints Handling
- **No Internet:** All dependencies are installed in the Docker image; no online calls are made.
- **CPU Only:** No GPU or external acceleration is required.
- **Runtime:** The script is optimized for ≤ 10 seconds per PDF by using efficient parsing and minimal dependencies.
- **Model Size:** No ML model is used for Round 1A, so the codebase is well under the 200MB limit.
- **Generalization:**
  - The logic adapts to any document by analyzing relative font sizes, not relying on document-specific rules.
  - No hardcoded font names, sizes, or keywords are used.

## Edge Cases
- If a document uses fewer than four font sizes, the script assigns heading levels to as many as possible.
- If no text is found, the output is an empty list.

## Output
- For each PDF, a JSON file is created in the `output/` directory, representing the heading hierarchy. 