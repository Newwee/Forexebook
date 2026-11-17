import fitz
import json
import os

pdf_path = r"C:\Users\New JA\Downloads\EbookFOREX\Trade.pdf"
doc = fitz.open(pdf_path)

output_dir = r"C:\Users\New JA\Downloads\EbookFOREX\pdf_extracted"
os.makedirs(output_dir, exist_ok=True)
images_dir = os.path.join(output_dir, "images")
os.makedirs(images_dir, exist_ok=True)
page_renders_dir = os.path.join(output_dir, "page_renders")
os.makedirs(page_renders_dir, exist_ok=True)

pages = []
for i, page in enumerate(doc):
    page_num = i + 1
    text = page.get_text()
    
    img_list = page.get_images(full=True)
    extracted_imgs = []
    
    for img_idx, img in enumerate(img_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        img_filename = f"p{page_num}_img{img_idx+1}.{image_ext}"
        img_save_path = os.path.join(images_dir, img_filename)
        with open(img_save_path, "wb") as f:
            f.write(image_bytes)
        extracted_imgs.append(img_filename)
        
    pix = page.get_pixmap(dpi=150)
    page_render_filename = f"page_{page_num:03d}.png"
    pix.save(os.path.join(page_renders_dir, page_render_filename))
    
    pages.append({
        "page": page_num,
        "text": text,
        "raw_images": extracted_imgs,
        "page_render": page_render_filename
    })

with open(os.path.join(output_dir, "extracted_content.json"), "w", encoding="utf-8") as f:
    json.dump(pages, f, ensure_ascii=False, indent=2)

print(f"Extraction complete! Total pages: {len(pages)}")
