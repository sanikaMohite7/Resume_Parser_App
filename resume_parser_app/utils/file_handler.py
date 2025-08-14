from pathlib import Path
from typing import Tuple

def save_upload(upload_dir: Path, uploaded_file) -> Path:
    upload_dir.mkdir(parents=True, exist_ok=True)
    dest = upload_dir / uploaded_file.name
    with open(dest, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return dest

def read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")

def split_ext(path: Path) -> Tuple[str, str]:
    return path.stem, path.suffix.lower()