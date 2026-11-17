import json
import re

with open(r"C:\Users\New JA\Downloads\EbookFOREX\pdf_extracted\extracted_content.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

def deduplicate_thai(text):
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    cleaned_lines = []
    for line in lines:
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)

catalog = []
for p in pages:
    catalog.append({
        "page": p["page"],
        "text": deduplicate_thai(p["text"]),
        "images": p["raw_images"],
        "render": p["page_render"]
    })

with open(r"C:\Users\New JA\Downloads\EbookFOREX\cleaned_catalog.json", "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

print("Saved cleaned_catalog.json")
