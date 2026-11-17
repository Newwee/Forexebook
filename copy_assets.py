import os
import shutil

dest_renders = r"C:\Users\New JA\Downloads\EbookFOREX\public\extracted\page_renders"
dest_images = r"C:\Users\New JA\Downloads\EbookFOREX\public\extracted\images"

os.makedirs(dest_renders, exist_ok=True)
os.makedirs(dest_images, exist_ok=True)

src_renders = r"C:\Users\New JA\Downloads\EbookFOREX\pdf_extracted\page_renders"
src_images = r"C:\Users\New JA\Downloads\EbookFOREX\pdf_extracted\images"

for f in os.listdir(src_renders):
    shutil.copy2(os.path.join(src_renders, f), os.path.join(dest_renders, f))

for f in os.listdir(src_images):
    shutil.copy2(os.path.join(src_images, f), os.path.join(dest_images, f))

print("Assets copied to public/extracted successfully!")
