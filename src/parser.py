from pathlib import Path


def read_document(file_path:Path)->str:
    """Reads the content of a file and returns it as a string."""

    if file_path.suffix.lower() == '.pdf':
        from pypdf import PdfReader
        reader = PdfReader(file_path)
        text = ''
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip()

    elif file_path.suffix.lower() == '.txt':
         with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    
    else:
        raise ValueError(f"Unsupported file format: {file_path.suffix}")
