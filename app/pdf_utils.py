from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

def extract_pages(file, ranges):
    reader = PdfReader(file)
    writer = PdfWriter()
    total_pages = len(reader.pages)
    extracted_texts = []

    for start, end in ranges:
        start = max(1, start)
        end = min(total_pages, end)
        for i in range(start - 1, end):
            writer.add_page(reader.pages[i])
            text = reader.pages[i].extract_text()
            if text:
                extracted_texts.append(f"**Page {i+1}:**\n{text[:1000]}...\n")

    output = BytesIO()
    writer.write(output)
    output.seek(0)
    return output, extracted_texts

def parse_ranges(ranges_text):
    ranges = []
    for part in ranges_text.split(','):
        try:
            start, end = map(int, part.strip().split('-'))
            if start <= end:
                ranges.append((start, end))
        except:
            pass
    return ranges
