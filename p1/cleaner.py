from pathlib import Path
import shutil
from typing import Dict, List
from transformer import normalize_filename

CATEGORIES: Dict[str, List[str]] = {
    "images": ["jpeg", "png", "jpg", "svg"],
    "videos": ["avi", "mp4", "mov", "mkv"],
    "documents": ["doc", "docx", "txt", "pdf", "xlsx", "pptx"],
    "music": ["mp3", "ogg", "wav", "amr"],
    "archives": ["zip", "gz", "tar"],
    "unknown": [],
}


def list_folders(preassigned_path: Path) -> list[Path]:
    folders = []
    folders.append(preassigned_path)
    for file_path in preassigned_path.iterdir():
        if file_path.is_dir():
            folders.append(file_path)
            list_folders(file_path)
    return folders


def define_category(file_path: Path) -> str:
    extension: str = file_path.name.split('.')[-1]
    for category, ext in CATEGORIES.items():
        if extension in ext:
            return category
    CATEGORIES["unknown"].append(extension)
    return "unknown"


def delet_folders(preassigned_path: Path):
    shutil.rmtree(preassigned_path)


def move_to_category_folder(file_path: Path, destination_folder: Path):
    for el in file_path.iterdir():
        if el.is_file():
            category = define_category(el)
            destination_category = destination_folder / category
            destination_category.mkdir(exist_ok=True)
            if category == "archives":
                folder_unpack = destination_category / \
                    el.name.split(".")[0]
                folder_unpack.mkdir()
                shutil.unpack_archive(el, folder_unpack)
                continue
            destination_path = destination_category / \
                normalize_filename(el.name)
            shutil.move(el, destination_path)
