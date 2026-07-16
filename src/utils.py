from pathlib import Path
import tempfile

def save_uploaded_file(uploaded_file)->Path:
    """Saves the uploaded file to a temporary location and returns the path."""
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as temp_file:
            temp_file.write(uploaded_file.getbuffer())
            return Path(temp_file.name)
    return None