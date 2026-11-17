import json
import re

with open(r"C:\Users\New JA\Downloads\EbookFOREX\pdf_extracted\extracted_content.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

def clean_stutter(text):
    return text

sections = [
    ("Forex Basics & Market Structure", 1, 10),
    ("Demand & Supply Zones", 11, 18),
    ("Impulse, Pullback & Valid Pullback", 19, 28),
    ("BOS: Break of Structure", 29, 32),
    ("IDM: Inducement (Comprehensive)", 33, 52),
    ("BOS + IDM Combination", 53, 55),
    ("CHoCH & MSS Reversal Dynamics", 56, 65),
    ("Liquidity, BSL & SSL", 66, 72),
    ("Order Flow (OF) Mechanics", 73, 77),
    ("Order Block (OB) & SCOB", 78, 90),
    ("Breaker Block (BB & BRK)", 91, 95),
    ("POI: Point of Interest & FVG", 96, 105),
    ("Fibonacci & Premium/Discount", 106, 111),
    ("Trading Psychology & Complete Entry Models", 112, 116)
]

for title, start_p, end_p in sections:
    print(f"\n==================== {title} (Pages {start_p}-{end_p}) ====================")
    for p in range(start_p, end_p + 1):
        page_obj = pages[p - 1]
        raw_txt = page_obj["text"].strip()
        lines = [l.strip() for l in raw_txt.split("\n") if l.strip()]
        first_lines = " | ".join(lines[:3]) if lines else "EMPTY"
        print(f"P{p}: {first_lines[:120]}")
