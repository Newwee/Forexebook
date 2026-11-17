import json
import os

with open(r"C:\Users\New JA\Downloads\EbookFOREX\pdf_extracted\extracted_content.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

print(f"Loaded {len(pages)} pages")

with open(r"C:\Users\New JA\Downloads\EbookFOREX\all_pages_summary.txt", "w", encoding="utf-8") as out:
    for p in pages:
        pnum = p["page"]
        text = p["text"].strip()
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        header = lines[0] if lines else "NO_TEXT"
        out.write(f"=== PAGE {pnum} ===\n")
        out.write(f"Header/First: {header}\n")
        out.write(f"Raw Images: {len(p['raw_images'])}\n")
        out.write("Content:\n")
        out.write(text + "\n\n")

print("Saved all_pages_summary.txt")
