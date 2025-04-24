import requests
import os, shutil
from pathlib import Path

def download_images(file_ids, image_directory):
    file_ids = file_ids

    downloads_dir = Path(image_directory).resolve()
    shutil.rmtree(downloads_dir, ignore_errors = True)
    Path.mkdir(downloads_dir)

    def download_google_drive_file(file_id, dest_folder=image_directory):
        os.makedirs(dest_folder, exist_ok=True)
        url = f"https://drive.google.com/uc?export=download&id={file_id}"
        file_path = os.path.join(dest_folder, f"{file_id}.jpg")
        r = requests.get(url)
        with open(file_path, "wb") as f:
            f.write(r.content)
        return file_path

# Download files
    local_paths = [download_google_drive_file(fid) for fid in file_ids]